from flask import request,redirect,url_for,session, g
from .models import CmsPermission
from functools import wraps

#若当前网页session中没有user_id属性（只有登录才有该属性），则会跳转到登陆页面
def login_required(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if not request.path.endswith(url_for('cms.login')):
            # user_id = session.get('cmsuser_id')
            # if not user_id:
            if 'cmsuser_id' not in session:
                return redirect(url_for('cms.login'))
            else:
                return func(*args,**kwargs)
    return inner


def auth_permission(permission):
    def outer(func):
        @wraps(func)
        def inner(*args,**kwargs):
            user = g.cms_user
            if user.has_permissions(permission):
                return func(*args,**kwargs)
            else:
                return redirect(url_for('cms.index'))
        return inner
    return outer