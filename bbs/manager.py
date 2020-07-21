from flask_script import Manager
from bbs import app
from flask_migrate import MigrateCommand, Migrate
from exts import db
from apps.cms.models import CmsUser, CmsRole, CmsPermission, BoardModel,HighLightPostModel
from apps.front.models import FrontUser, PostModel,CommentModel
import random

manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)


# 添加后台的用户
@manager.option('-u ', '--username', dest='username')
@manager.option('-p ', '--password', dest='password')
@manager.option('-e ', '--email', dest='email')
def create_cms_user(username, password, email):
    user = CmsUser(username=username, password=password, email=email)
    db.session.add(user)
    db.session.commit()
    print('后台用户添加成功')


#添加后台用户
@manager.option('-t','--telephone',dest='telephone')
@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
def create_front_user(telephone,username,password):
    user = FrontUser(telephone=telephone,username=username,password=password)
    db.session.add(user)
    db.session.commit()
    print('前台用户添加成功')


@manager.command
def create_role():
    # 访问者
    visitor = CmsRole(name='访问者', desc='只能查看数据，不能修改数据')
    visitor.permissions = CmsPermission.VISITOR

    # 运营人员
    operator = CmsRole(name='运营人员', desc='管理帖子，管理评论，管理前台用户')
    operator.permissions = CmsPermission.VISITOR | CmsPermission.POSTER | CmsPermission.COMMENTER | CmsPermission.FRONTUSER

    # 管理员
    admin = CmsRole(name='管理员', desc='拥有本系统大部分权限')
    admin.permissions = CmsPermission.VISITOR | CmsPermission.POSTER | CmsPermission.COMMENTER | CmsPermission.FRONTUSER | CmsPermission.BOARDER | CmsPermission.CMSUSER

    # 开发人员
    developer = CmsRole(name='开发者', desc='拥有所有权限')
    developer.permissions = CmsPermission.ALL_PERMISSION
    db.session.add_all([visitor, operator, admin, developer])
    db.session.commit()


@manager.command
def test_permission():
    user = CmsUser.query.get(4)
    result = user.has_permissions(20)  # 判断该用户是否含有权限
    print(result)
    print(user)
    if user:
        user_permissions = user.permissions
        print(user_permissions)
    else:
        print('该用户不存在')


@manager.option('-e', '--email', dest='email')
@manager.option('-n', '--name', dest='name')
def add_user_role(email, name):
    user = CmsUser.query.filter_by(email=email).first()
    # print(user)
    if user:
        role = CmsRole.query.filter_by(name=name).first()
        if role:
            # user.roles.append(role)
            role.users.append(user)
            db.session.commit()
            print('用户{}成功获得了{}的权限'.format(email, name))
        else:
            print('没有找到对应的角色')
    else:
        print('该用户不存在')


@manager.command
def create_post_data():
    for i in range(1,50):
        title = '标题：%s'%(i)
        content = '内容：%s'%(i)
        author = FrontUser.query.first()

        post = PostModel(title=title,content=content)
        post.author = author
        post.board_id = random.randint(1,6)
        db.session.add(post)
        db.session.commit()
    print('帖子添加成功')

if __name__ == '__main__':
    manager.run()
