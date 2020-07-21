from flask import Blueprint, request, jsonify
from utils import restful, send_msg, email_captcha
from .forms import SmsCaptchaForm
from utils import bbscache
from apps.front.models import FrontUser
from qiniu import Auth, put_file, etag
import qiniu.config


common_bp = Blueprint('common', __name__, url_prefix='/c')


@common_bp.route('/')
def index():
    return 'common_index'

#验证码发送
# @common_bp.route('/sms_captcha/', methods=['POST'])
# def sms_captcha():
#     telephone = request.form.get('telephone')
#
#     if not telephone:
#         return restful.param_error(message='请输入正确的手机号')
#
#     # 生成4位验证码
#     captcha = email_captcha.generate_random_str(4)
#
#     if send_msg.send_mobile_msg(telephone, captcha) == 0:
#         return restful.success()
#     else:
#         return restful.param_error(message='发送失败')


@common_bp.route('/sms_captcha/', methods=['POST'])
def sms_captcha():
    form = SmsCaptchaForm(request.form)
    if form.validate():
        telephone = request.form.get('telephone')

        # 如果手机号在数据库中已存在，则返回信息
        exist_user = FrontUser.query.filter_by(telephone=telephone).first()
        print(exist_user)
        if exist_user:
            return restful.param_error(message='用户已存在，请直接登录')

        #生成4位验证码用于发送给用户
        captcha = email_captcha.generate_random_str(4)
        # 调用发送验证码函数
        if send_msg.send_mobile_msg(telephone,captcha) == 0:
            #将验证码保存到redis中
            bbscache.redis_set(telephone,captcha.lower())
            return restful.success()
        else:
            return restful.param_error(message='发送失败，请重新发送')
    else:
        # print(form.errors)
        return restful.param_error(message='发送失败，请重新发送')


@common_bp.route('/uptoken/')
def uptoken():
    # 需要填写你的 Access Key 和 Secret Key
    access_key = 'PoFZ5zsNAssJp20uiNuATgsf2uXS8QGjcoz1bhRW'
    secret_key = 'QiaHnr2O1zQzyO79FcEZfOTrglM9BZ7S6oMwkOkv'

    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = 'flask-images'

    # 上传后保存的文件名
    # key = 'my-python-logo.png'

    # 生成上传 Token，可以指定过期时间等
    # token = q.upload_token(bucket_name, key, 3600)
    token = q.upload_token(bucket_name)

    return jsonify({'uptoken':token})
