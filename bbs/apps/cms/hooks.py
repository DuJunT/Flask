from .views import cms_bp
from flask import request,url_for,session,redirect,g,current_app
from .models import CmsUser,CmsPermission

#通过钩子函数去判断后台其他网页有没有session（有session代表登录了），没有则跳转到后台登录页面
@cms_bp.before_request
def before_request():
    # print('before_request')
    if not request.path.endswith(url_for('cms.login')):
        # print(request.path)
        # print('before_request_not_login_page')
        user_id = session.get('cmsuser_id')
        if not user_id:
            return redirect(url_for('cms.login'))

    if 'cmsuser_id' in session:
        # print('login_page')
        user = CmsUser.query.get(session.get('cmsuser_id'))
        g.cms_user = user
        # g.cms_username = session.get('user_name')

@cms_bp.context_processor
def context_processor():
    return {'CmsPermission':CmsPermission}