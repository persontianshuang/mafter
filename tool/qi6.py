# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
#需要填写你的 Access Key 和 Secret Key
access_key = '2Cr1NjNXhoWJpZ3NRtAbJw2yPhP7f0Qa_q0DfJcq'
secret_key = 'bJWSEUKLU1xBmMZPEnT9qUKeBp_ZutBkkH5UEW9g'
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = 'kindle'
#上传到七牛后保存的文件名
key = 'ddsas.mp3'
#生成上传 Token，可以指定过期时间等
token = q.upload_token(bucket_name, key, 3600)
#要上传文件的本地路径
localfile = '/Users/user/Desktop/wq.mp3'
ret, info = put_file(token, key, localfile)
print(info)
assert ret['key'] == key
assert ret['hash'] == etag(localfile)
