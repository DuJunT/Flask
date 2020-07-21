from flask import request,redirect,url_for,session, g
from functools import wraps

#若当前网页session中没有frontuser_id属性（只有登录才有该属性），则会跳转到登陆页面
def login_required(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if not request.path.endswith(url_for('front.signin')):
            if 'frontuser_id' not in session:
                return redirect(url_for('front.signin'))
            else:
                return func(*args,**kwargs)
    return inner

