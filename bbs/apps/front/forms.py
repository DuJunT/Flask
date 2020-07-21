from wtforms import Form, StringField, ValidationError, BooleanField, TextAreaField, IntegerField
from wtforms.validators import Regexp, Length, EqualTo, InputRequired
from apps.common.forms import BaseError
from utils import bbscache
from .models import FrontUser


class SignupForm(BaseError):
    telephone = StringField(validators=[Regexp(r'1[345789]\d{9}',message='请输入正确的手机号')])
    sms_captcha = StringField(validators=[Regexp(r'\w{4}',message='请输入正确的短信验证码')])
    username = StringField(validators=[Length(min=2,max=20,message='用户名长度位2-20')])
    password1 = StringField(validators=[Regexp(r'[0-9a-zA-Z]',message='密码只允许数字和字母组合'),Length(min=6,max=20,message='密码长度位6-20')])
    password2 = StringField(validators=[EqualTo('password1',message='两次密码输入不一致')])
    graph_captcha = StringField(validators=[Regexp(r'\w{4}',message='请输入正确的图形验证码')])

    def validate_sms_captcha(self,field):
        telephone = self.telephone.data
        sms_captcha = self.sms_captcha.data
        sms_captcha_redis = bbscache.redis_get(telephone)

        if not sms_captcha_redis or sms_captcha_redis.lower() != sms_captcha.lower():
            raise ValidationError('短信验证码不正确')

    def validate_graph_captcha(self,field):
        graph_captcha = self.graph_captcha.data
        graph_captcha_redis = bbscache.redis_get(graph_captcha)

        if not graph_captcha_redis or graph_captcha.lower() != graph_captcha.lower():
            raise ValidationError('图形验证码不正确')


class SigninForm(BaseError):
    telephone = StringField(validators=[Regexp(r'1[345789]\d{9}',message='请输入正确的手机号')])
    password =  StringField(validators=[Length(min=6,max=20,message='密码长度位6-20')])
    remember =  BooleanField(validators=[InputRequired()])

    # 判断用户输入的手机号在数据库中有没有注册
    def validate_telephone(self,field):
        telephone = self.telephone.data
        user = FrontUser.query.filter_by(telephone=telephone).first()
        if not user:
            raise ValidationError(message='该手机号未注册')


class AddPostForm(BaseError):
    title = StringField(validators=[InputRequired(message='请输入标题')])
    board_id = IntegerField(validators=[InputRequired(message='请选择对应的板块ID')])
    content = StringField(validators=[InputRequired(message='请输入文本内容')])


class AddCommentForm(BaseError):
    post_id = IntegerField(validators=[InputRequired(message='请输入评论对应的板块ID')])
    content = StringField(validators=[InputRequired(message='请输入评论内容')])