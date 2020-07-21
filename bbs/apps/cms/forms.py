from wtforms import Form, StringField, IntegerField, BooleanField
from wtforms.validators import Email, InputRequired, Length, EqualTo, ValidationError, URL
from utils import bbscache
from apps.common.forms import BaseError


class LoginForm(BaseError):
    email = StringField(validators=[Email(message='请输入正确的邮箱格式'), InputRequired()])
    password = StringField(validators=[Length(min=5, max=18, message='密码长度为5到18')])
    remember = BooleanField()


class ResetPwdForm(BaseError):
    oldpwd = StringField(validators=[Length(min=6, max=18, message='密码长度为6-18')])
    newpwd = StringField(validators=[Length(min=6, max=18, message='密码长度为6-18')])
    newpwd2 = StringField(validators=[EqualTo('newpwd', message='两次输入的密码不一致')])


class ResetEmailForm(BaseError):
    email = StringField(validators=[Email(message='请输入正确格式的邮箱')])
    captcha = StringField(validators=[Length(min=4, max=4, message='请输入正确的验证码')])

    def validate_captcha(self, field):
        email = self.email.data
        captcha = field.data  # 这里的field 等于form.name因为validate_captcha是指定字段验证器,这里也可以写self.captcha.data

        redis_captcha = bbscache.redis_get(email)
        if not redis_captcha or redis_captcha.lower() != captcha.lower():
            return ValidationError(message='请输入正确的验证码')


class AddBannerForm(BaseError):
    name = StringField(validators=[InputRequired(message='请输入轮播图名字')])
    image_url = StringField(validators=[InputRequired(message='请输入图片链接'),URL(message='图片链接有误')])
    link_url = StringField(validators=[InputRequired(message='请输入跳转链接'),URL(message='图片链接有误')])
    priority = StringField(validators=[InputRequired(message='请输入轮播图优先级')])


class UpdateBannerForm(AddBannerForm):
    banner_id = IntegerField(validators=[InputRequired(message='轮播图不存在')])


class AddBoardForm(BaseError):
    name =  StringField(validators=[InputRequired(message='请输入板块名字')])


class UpdateBoardForm(BaseError):
    name = StringField(validators=[InputRequired(message='请输入板块名字')])
    board_id = IntegerField(validators=[InputRequired(message='请输入板块ID')])