from flask import Blueprint, views, render_template, make_response, request, session, g,redirect,url_for
from utils.captcha import Captcha
from io import BytesIO
from utils import bbscache, restful, safe_url
from .forms import SignupForm, SigninForm, AddPostForm,AddCommentForm
from .models import FrontUser, PostModel, CommentModel
from exts import db
from apps.cms.models import BannerModel, BoardModel, HighLightPostModel
from apps.front.decorators import login_required
from flask_paginate import Pagination, get_page_parameter
import config
from sqlalchemy.sql import func

front_bp = Blueprint('front', __name__)
from .hooks import before_request


# 首页
@front_bp.route('/')
def index():
    banners = BannerModel.query.order_by(BannerModel.priority.desc()).limit(4).all()
    boards = BoardModel.query.all()
    board_id = request.args.get('board_id', type=int)
    sort_id = request.args.get('sort_id',type=int)

    page = request.args.get(get_page_parameter(), type=int, default=1)

    #定义每页需要展示的数据的条数
    start = (page-1)*config.PER_PAGE
    end = start + config.PER_PAGE

    query_obj = None

    #首页帖子
    if sort_id == None:
        query_obj = PostModel.query

    # 最新帖子
    if sort_id == 1:
        query_obj = PostModel.query.order_by(PostModel.create_time.desc())

    # 精华帖
    if sort_id == 2:
        # query_obj = PostModel.query.filter(PostModel.id==HighLightPostModel.post_id).order_by(PostModel.create_time.desc())
        # print(query_obj)
        query_obj = db.session.query(PostModel).join(HighLightPostModel).order_by(PostModel.create_time.desc())

    #点赞最多
    if sort_id == 3:
        query_obj = PostModel.query.order_by(PostModel.create_time.desc())

    # 评论最多
    if sort_id == 4:
        query_obj = db.session.query(PostModel).join(CommentModel).group_by(PostModel.id).order_by(func.count(CommentModel.id).desc())
        # print(query_obj)

    if board_id:
        # posts = query_obj.filter_by(board_id=board_id).slice(start,end).all()
        posts = query_obj.filter(PostModel.board_id==board_id).slice(start,end).all()
        # total = query_obj.filter_by(board_id=board_id).count()
        total = query_obj.filter(PostModel.board_id==board_id).count()
    else:
        posts = query_obj.slice(start,end).all()
        total = query_obj.count()



    pagination = Pagination(page=page, total=total, bs_version=3,outer_window=1,inner_window=2,per_page=config.PER_PAGE)

    context = {
        'banners': banners,
        'boards': boards,
        'current_board': board_id,
        'posts': posts,
        'pagination': pagination,
        'current_sort': sort_id,
    }
    return render_template('front/front_index.html', **context)



# 图形验证码
@front_bp.route('/captcha/')
def graph_captcha():
    try:
        text, image = Captcha.gene_graph_captcha()
        bbscache.redis_set(text.lower(), text.lower())
        # BytesIO字节流
        out = BytesIO()
        # 把图片保存到字节流中，并指定格式png
        image.save(out, 'png')
        # 文件指针流，改变流的位置
        out.seek(0)
        # 生成响应用于返回
        resp = make_response(out.read())
    except:
        return graph_captcha()
    return resp


# 跳转测试页面
@front_bp.route('/test_return/')
def test_return():
    return render_template('front/test.html')


# 注册页面
class SignupView(views.MethodView):
    def get(self):
        return_to = request.referrer
        # print(return_to)
        # print(request.url)
        # print(safe_url.is_safe_url(return_to))
        if return_to and return_to != request.url and safe_url.is_safe_url(return_to):
            return render_template('front/front_signup.html', return_to=return_to)
        return render_template('front/front_signup.html')

    def post(self):
        form = SignupForm(request.form)
        if form.validate():
            # 将注册信息保存到数据库中
            telephone = form.telephone.data
            username = form.username.data
            password1 = form.password1.data
            front_user = FrontUser(telephone=telephone, username=username, password=password1)
            db.session.add(front_user)
            db.session.commit()
            return restful.success()
        else:
            return restful.param_error(message=form.get_error())


# 登录页面
class SigninView(views.MethodView):
    def get(self):
        return_to = request.referrer
        # print(return_to)
        # print(request.url)
        # print(safe_url.is_safe_url(return_to))
        if return_to and return_to != request.url and safe_url.is_safe_url(return_to):
            return render_template('front/front_signin.html', return_to=return_to)
        else:
            return render_template('front/front_signin.html')

    def post(self):
        form = SigninForm(request.form)
        if form.validate():
            telephone = form.telephone.data
            password = form.password.data
            remember = form.remember.data
            user = FrontUser.query.filter_by(telephone=telephone).first()
            if user and user.check_password(password):
                session['frontuser_id'] = user.id
                if remember:
                    session.permanent = True
                return restful.success()
            else:
                return restful.param_error(message='账号或密码错误')
        else:
            return restful.param_error(message=form.get_error())


# 登出
@front_bp.route('/logout/')
def logout():
    # 删除session
    del session['frontuser_id']
    # 跳转到登陆页面
    return redirect(url_for('front.signin'))

# 发布帖子
class PostView(views.MethodView):
    decorators = [login_required]

    # @login_required
    def get(self):
        boards = BoardModel.query.all()
        context = {
            'boards': boards
        }
        return render_template('front/front_apost.html', **context)

    def post(self):
        form = AddPostForm(request.form)

        if form.validate():
            title = form.title.data
            board_id = form.board_id.data
            content = form.content.data
            board = BoardModel.query.get(board_id)
            if not board:
                return restful.param_error(message='没有这个板块')
            post = PostModel(title=title, content=content)
            post.board = board
            post.author = g.front_user
            db.session.add(post)
            db.session.commit()
            return restful.success()
        else:
            print(form.errors)
            return restful.param_error(message=form.get_error())


# 帖子详情页面
@front_bp.route('/p/<post_id>')
def post_detail(post_id):
    post = PostModel.query.get(post_id)
    if post:
        post.read_count += 1
        db.session.commit()
        return render_template('front/front_pdetail.html',post=post)
    else:
        return restful.param_error(message='该帖子不存在')


# 发表评论
@front_bp.route('/acomment/', methods=['POST'])
@login_required
def acomment():
    form = AddCommentForm(request.form)
    if form.validate():
        post_id = form.post_id.data
        content = form.content.data
        post = PostModel.query.get(post_id)
        if post:
            comment = CommentModel(content=content)
            comment.post = post
            comment.author = g.front_user
            db.session.add(comment)
            db.session.commit()
            return restful.success()
        else:
            return restful.param_error('该板块不存在')
    else:
        return restful.param_error(form.get_error())

front_bp.add_url_rule('/signup/', view_func=SignupView.as_view('signup'))
front_bp.add_url_rule('/signin/', view_func=SigninView.as_view('signin'))
front_bp.add_url_rule('/apost/', view_func=PostView.as_view('apost'))
