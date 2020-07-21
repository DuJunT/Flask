from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient
# 初始化client,apikey作为所有请求的默认值


def send_mobile_msg(mobile,code):
    clnt = YunpianClient('e8abe129a4e9f9a7c8c9adc8ece9ebc9')
    param = {YC.MOBILE:mobile,YC.TEXT:'【于成令】您的验证码是{}'.format(code)}
    r = clnt.sms().single_send(param)
    # 获取返回结果, 返回码:r.code(),返回码描述:r.msg(),API结果:r.data(),其他说明:r.detail(),调用异常:r.exception()
    # print(r.code())
    # print(r.msg())
    # print(r.data())
    return r.code()
    # 短信:clnt.sms() 账户:clnt.user() 签名:clnt.sign() 模版:clnt.tpl() 语音:clnt.voice() 流量:clnt.flow()

# if __name__ == '__main__':
#     status = send_mobile_msg(13714160953,1234)
#     print(status)