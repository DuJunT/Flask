from flask import request,url_for,session,redirect,g,current_app
from .views import front_bp
from .models import FrontUser


# 前端页面使用钩子函数，判断是否有登录，有登录则在首页右上角显示个人信息
@front_bp.before_request
def before_request():
    if 'frontuser_id' in session:
        # print('login_page')
        user = FrontUser.query.get(session.get('frontuser_id'))
        g.front_user = user
        # g.front_username = session.get('user_name')
