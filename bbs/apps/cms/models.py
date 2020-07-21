from exts import db
from datetime import datetime
from werkzeug.security import  generate_password_hash,check_password_hash
from apps.front.models import PostModel

# 每种权限对应着不一样的二进制数值
class CmsPermission(object):
    # 用255的二进制方式来表示权限
    # 所有权限
    ALL_PERMISSION      =   0b11111111

    # 访问者
    VISITOR             =   0b00000001

    # 管理帖子
    POSTER              =   0b00000010

    # 管理评论
    COMMENTER           =   0b00000100

    # 管理板块
    BOARDER             =   0b00001000

    # 管理前台用户
    FRONTUSER           =   0b00010000

    # 管理后台用户
    CMSUSER             =   0b00100000

    # 管理前后台用户
    ADMIN             =   0b01000000

cms_role_user = db.Table(
    'cms_role_user',
    db.Column('cms_role_id',db.Integer,db.ForeignKey('cms_role.id'),primary_key=True),
    db.Column('cms_user_id',db.Integer,db.ForeignKey('cms_user.id'),primary_key=True),
)

# 角色模型
class CmsRole(db.Model):
    __tablename__ = 'cms_role'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(50),nullable=True)
    desc = db.Column(db.String(200),nullable=True)
    create_time = db.Column(db.DateTime,default=datetime.now())
    permissions = db.Column(db.Integer,default=CmsPermission.VISITOR)

    users = db.relationship('CmsUser',secondary=cms_role_user,backref='roles')


# 后台用户模型
class CmsUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(50),nullable=True)
    _password = db.Column(db.String(200),nullable=True)  #加“_”是为了不想让外界直接通过类名.属性名的方式来调用这个密码属性
    email = db.Column(db.String(50),nullable=True,unique=True)
    join_time = db.Column(db.DateTime,default=datetime.now())

    def __init__(self,username,password,email):
        self.username = username
        self.password = password   #这里的self.password指的是下面的被property装饰过的password方法
        self.email = email

    @property    #用property装饰器装饰password
    def password(self):
        return self._password

    @password.setter   #外界对password设置值（赋值）时会调用这个方法
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)  #用于加密密码

    def check_password(self,raw_password):
        result = check_password_hash(self.password,raw_password) #将传入的密码通过一样的算法加密，然后加密后的密码和数据库的密码对比，此函数用于在视图的登录类中验证前端提交上来的密码是否在数据库中
        return result


    # 获取用户本身有哪些权限，通过查看用户对应着哪些角色
    @property
    def permissions(self):
        self_permissions = 0     # 定义一个变量来接收下面的值 #

        if not self.roles:      # 查看当前用户的roles关系中是否有对应的角色，没有则返回0，代表该用户没有权限
            return 0
        for role in self.roles: # 有对应的角色则遍历，得到对应的角色对象
            permissions = role.permissions  # 将角色中的permissons对应的二进制转为十进制的值提取出来
            self_permissions |= permissions  # 赋值到本身的权限变量中，用于返回
        return self_permissions         # 这是一个十进制的数值，可以自己通过计算机转为二进制来判断有哪些权限

    #判断用户是否有对应的权限
    def has_permissions(self,permissions:int) -> int:# 参数permissions  是数值
        self_permission = self.permissions
        result = self_permission&permissions == permissions
        return result

    @property
    def is_developer(self):
        return self.has_permissions(CmsPermission.ALL_PERMISSION)


# 轮播图模型
class BannerModel(db.Model):

    __tablename__ = 'banner'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    link_url = db.Column(db.String(255), nullable=False)
    priority = db.Column(db.Integer, default=0)
    create_time = db.Column(db.DateTime, default=datetime.now)

    #1代表未删除
    is_delete = db.Column(db.Integer,default=1)


#板块模型
class BoardModel(db.Model):
    __tablename__ = 'cms_board'
    id = db.Column(db.Integer,primary_key=True, autoincrement=True)
    name = db.Column(db.String(255),nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)


# 高亮帖子
class HighLightPostModel(db.Model):
    __tablename__ = 'highlight_post'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'))
    create_time = db.Column(db.DateTime,default=datetime.now)

    post = db.relationship('PostModel',backref='highlight')