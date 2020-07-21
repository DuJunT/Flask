HOSTNAME = '127.0.0.1'
PORT = 3306
DATABASE = 'flask_bbs'
USERNAME = 'root'
PASSWORD = 'root'

DB_URL = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)


SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False

# celery配置项
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'


import os
# 用来加密CSRF的
# SECRET_KEY = os.urandom(15)
SECRET_KEY = 'asdasdas'

# 分页功能的配置项
PER_PAGE = 7

# flask-mail发送邮件
# 发送邮箱服务器地址
MAIL_SERVER = 'smtp.qq.com'
#465或587
MAIL_PORT =  '587'
MAIL_USE_TLS =  True
MAIL_USE_SSL =  False
MAIL_USERNAME =  '947141993@qq.com'
# 这个是授权码
MAIL_PASSWORD =  'tvpkpahobhjgbfch'
MAIL_DEFAULT_SENDER =  '947141993@qq.com'


# 用来自动更新模板的
TEMPLATES_AUTO_RELOAD = True