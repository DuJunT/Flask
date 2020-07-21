from qiniu import Auth, put_file, etag
import qiniu.config

#需要填写你的 Access Key 和 Secret Key
access_key = 'PoFZ5zsNAssJp20uiNuATgsf2uXS8QGjcoz1bhRW'
secret_key = 'QiaHnr2O1zQzyO79FcEZfOTrglM9BZ7S6oMwkOkv'

#构建鉴权对象
q = Auth(access_key, secret_key)

#要上传的空间
bucket_name = 'flask-storage'

#上传后保存的文件名
key = 'my-python-logo.png'

#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)

#要上传文件的本地路径
localfile = 'D:\Python_Study\Flask项目\\bbs\static\common\images\logo.png'
ret, info = put_file(token, key, localfile)

print('ret:',ret)
print('info:',info)

assert ret['key'] == key
assert ret['hash'] == etag(localfile)