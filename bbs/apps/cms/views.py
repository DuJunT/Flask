from flask import Blueprint, views, render_template, request, redirect, url_for, session, jsonify, g
from apps.cms.forms import LoginForm, ResetPwdForm, ResetEmailForm, AddBannerForm, UpdateBannerForm, AddBoardForm, \
    UpdateBoardForm
from apps.front.models import PostModel
from apps.cms.models import CmsUser, CmsPermission, BannerModel, BoardModel,HighLightPostModel
from .decorators import login_required, auth_permission
from exts import db, mail
from utils import restful, email_captcha, bbscache
from flask_mail import Message
from flask_paginate import Pagination, get_page_parameter
import config
# from task import celery_send_mail


cms_bp = Blueprint('cms', __name__, url_prefix='/cms')
from .hooks import before_request


# 首页
@cms_bp.route('/')
# @login_required  #decorators.py中定义的装饰器,这里通过钩子函数来完成session的验证功能
def index():
    # print(session.get('cmsuser_id'))
    # print(url_for('cms.index'))
    return render_template('cms/cms_index.html')


# 登录
class LoginView(views.MethodView):

    def get(self, message=None):
        # print('login_get')
        return render_template('cms/cms_login.html', message=message)

    def post(self):
        login_form = LoginForm(request.form)
        # print('login_post')
        if login_form.validate():
            # 验证成功后去数据库中验证数据

            email = login_form.email.data  # 前端提交上来的数据
            password = login_form.password.data
            remember = login_form.remember.data
            user = CmsUser.query.filter_by(email=email).first()  # 数据库中验证数据

            # 验证用户是否存在以及密码是否正确
            if user and user.check_password(password):
                # print('login_session')
                session['cmsuser_id'] = user.id
                # session['user_name'] = user.username
                if remember:
                    # session持久化
                    session.permanent = True

                    # 登录成功跳转cms首页
                return redirect(url_for('cms.index'))
            else:
                return self.get(message='此用户未注册')
        else:
            # print(login_form.data)
            # print(login_form.errors.popitem())
            # print(login_form.password.errors.pop())
            # return login_form.password.errors.pop()
            # return '密码长度最少5位，最多18位'
            # return self.get(message=login_form.errors.popitem()[1][0])
            return self.get(message=login_form.get_error())


# 注销
@cms_bp.route('/logout/')
def logout():
    # 删除session
    del session['cmsuser_id']
    # 跳转到登陆页面
    return redirect(url_for('cms.login'))


# 个人中心简介
@cms_bp.route('/profile/')
def profile():
    return render_template('cms/cms_profile.html')


# 重新设置密码
class ResetPwdView(views.MethodView):
    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):
        resetpwd_form = ResetPwdForm(request.form)
        if resetpwd_form.validate():
            oldpwd = resetpwd_form.oldpwd.data
            newpwd = resetpwd_form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                return restful.success(message='密码修改成功')
            else:
                return restful.param_error(message='旧密码错误')
        else:
            # 没认证通过(即密码长度不通过，或者两次密码输入不一致)
            # message = resetpwd_form.errors
            print(resetpwd_form.get_error())
            return restful.param_error(message=resetpwd_form.get_error())


# 设置邮件
class ResetEmailView(views.MethodView):
    def get(self):

        return render_template('cms/cms_resetemail.html')

    def post(self):
        form = ResetEmailForm(request.form)
        if form.validate():
            email = form.email.data
            # 将email更新到数据库中
            g.cms_user.email = email
            db.session.commit()

            return restful.success()
        else:

            return restful.param_error(form.get_error())


# 邮件发送测试函数/与项目无关
@cms_bp.route('/send_mail/')
def send_mail():
    message = Message('验证码邮件', recipients=['719106933@qq.com'], body='测试邮件')
    mail.send(message)
    return '邮件发送成功'


# 邮件发送
class SendEmailView(views.MethodView):
    def get(self):
        recipients_mail = request.args.get('email')  # 获取html中name为email对应的邮箱号
        if not recipients_mail:
            return restful.param_error('请重新输入邮箱号')
        email_code = email_captcha.generate_random_str(4)  # 生成一个随机四位的数字和字母组合

        message = Message(subject='bbs论坛', recipients=[recipients_mail],
                          body='您的captcha_Code：%s' % (email_code))  # 通过邮件将验证码发送给指定的邮箱号

        try:  # 做异常处理，因为不一定可以发送成功
            mail.send(message)
            # celery_send_mail.delay(subject='bbs论坛', recipients=[recipients_mail],body='您的captcha_Code：%s' % (email_code))
        except:
            return restful.server_error('请输入正确的邮箱号')
        bbscache.redis_set('captcha_code', email_code)  # 邮箱验证码保存到redis
        return restful.success()


# 帖子管理
@cms_bp.route('/posts/')
@auth_permission(CmsPermission.POSTER)
def posts():
    page = request.args.get(get_page_parameter(), type=int, default=1)

    # 定义每页需要展示的数据的条数
    start = (page - 1) * config.PER_PAGE
    end = start + config.PER_PAGE

    posts = PostModel.query.slice(start,end).all()
    total = PostModel.query.count()
    pagination = Pagination(page=page, total=total, bs_version=3, outer_window=1, inner_window=2,
                            per_page=config.PER_PAGE)
    context = {
        'posts':posts,
        'pagination':pagination,
    }
    return render_template('cms/cms_posts.html',**context)


# 让帖子被选为精华帖
@cms_bp.route('/hpost/',methods=['POST'])
@auth_permission(CmsPermission.POSTER)
def hpost():
    post_id = request.form.get('post_id')
    post = PostModel.query.get(post_id)
    if not post:
        return restful.param_error('该帖子不存在')

    highlight_post = HighLightPostModel()
    highlight_post.post = post
    db.session.add(highlight_post)
    db.session.commit()
    return restful.success()


# 让帖子被选为非精华帖  cancelhighlight
@cms_bp.route('/chpost/', methods=['POST'])
@auth_permission(CmsPermission.POSTER)
def chpost():
    post_id = request.form.get('post_id')
    post = PostModel.query.get(post_id)
    if not post:
        return restful.param_error('该帖子不存在')
    highlight_post = HighLightPostModel.query.filter_by(post=post).first()
    db.session.delete(highlight_post)
    db.session.commit()
    return restful.success()

# 评论管理
@cms_bp.route('/comments/')
@auth_permission(CmsPermission.COMMENTER)
def comments():
    return render_template('cms/cms_comments.html')


# 板块管理
@cms_bp.route('/boards/')
@auth_permission(CmsPermission.BOARDER)
def boards():
    boards = BoardModel.query.all()
    return render_template('cms/cms_boards.html', boards=boards)


# 板块添加
@cms_bp.route('/aboard/', methods=['POST'])
@auth_permission(CmsPermission.BOARDER)
def aboard():
    form = AddBoardForm(request.form)
    if form.validate():
        name = form.name.data
        board = BoardModel(name=name)
        db.session.add(board)
        db.session.commit()
        return restful.success()
    else:
        return (restful.param_error(message=form.get_error()))


# 编辑板块
@cms_bp.route('/uboard/', methods=['POST'])
@auth_permission(CmsPermission.BOARDER)
def uboard():
    form = UpdateBoardForm(request.form)
    if form.validate():
        board_id = form.board_id.data
        # print(board_id)
        name = form.name.data
        # print(name)
        board = BoardModel.query.filter_by(id=board_id).first()
        if board:
            # print(board)
            board.name = name
            db.session.commit()
            return restful.success()
        else:
            return restful.param_error(message='这个板块不存在')
    else:
        return restful.param_error(form.get_error())


# 删除板块
@cms_bp.route('/dboard/', methods=['POST'])
@auth_permission(CmsPermission.BOARDER)
def dboard():
    board_id = request.form.get('board_id')
    if not board_id:
        return restful.param_error('该板块不存在')

    board = BoardModel.query.get(board_id)
    if not board:
        return restful.param_error('该板块不存在')
    db.session.delete(board)
    db.session.commit()
    return restful.success()


# 前台用户管理
@cms_bp.route('/frontuser/')
@auth_permission(CmsPermission.FRONTUSER)
def frontuser():
    return render_template('cms/cms_frontuser.html')


# 后台用户管理
@cms_bp.route('/cmsuser/')
@auth_permission(CmsPermission.CMSUSER)
def cmsuser():
    return render_template('cms/cms_cmsuser.html')


# CMS组管理
@cms_bp.route('/cmsrole/')
@auth_permission(CmsPermission.ALL_PERMISSION)
def cmsrole():
    return render_template('cms/cms_cmsrole.html')


# 轮播图管理
@cms_bp.route('/banners/')
def banners():
    banners = BannerModel.query.order_by(BannerModel.priority.desc()).all()
    return render_template('cms/cms_banners.html', banners=banners)


# 添加
@cms_bp.route('/abanner/', methods=['POST'])
def abanner():
    form = AddBannerForm(request.form)
    if form.validate():
        name = form.name.data
        image_url = form.image_url.data
        link_url = form.link_url.data
        priority = form.priority.data

        banner = BannerModel(name=name, image_url=image_url, link_url=link_url, priority=priority)
        db.session.add(banner)
        db.session.commit()
        return restful.success()
    else:
        return restful.param_error(message=form.get_error())


# 修改
@cms_bp.route('/ubanner/', methods=['POST'])
def ubanner():
    form = UpdateBannerForm(request.form)
    if form.validate():
        banner_id = form.banner_id.data
        name = form.name.data
        image_url = form.image_url.data
        link_url = form.link_url.data
        priority = form.priority.data
        banner = BannerModel.query.get(banner_id)
        if banner:
            banner.name = name
            banner.image_url = image_url
            banner.link_url = link_url
            banner.priority = priority
            db.session.commit()
            return restful.success()
        else:
            return restful.param_error(message='轮播图不存在')
    else:
        return restful.param_error(message=form.get_error())


# 删除
@cms_bp.route('/dbanner/', methods=['POST'])
def dbanner():
    # post方式
    banner_id = request.form.get('banner_id')
    if not banner_id:
        return restful.param_error('该轮播图已经删除，请重新刷新页面')

    banner = BannerModel.query.get(banner_id)
    if banner:
        banner.is_delete = 0
        # db.session.delete(banner)
        db.session.commit()
        return restful.success(data={'delete': 0})
    else:
        return restful.param_error(message='轮播图不存在')


cms_bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
cms_bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))
cms_bp.add_url_rule('/resetemail/', view_func=ResetEmailView.as_view('resetemail'))
cms_bp.add_url_rule('/email_captcha/', view_func=SendEmailView.as_view('email_captcha'))
