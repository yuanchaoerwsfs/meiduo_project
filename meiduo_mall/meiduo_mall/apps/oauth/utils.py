# from itsdangerous import TimedSerializer as Serializer
from django.conf import settings

from authlib.jose import jwt, JoseError

from .constants import ACCESS_TOKEN_EXPIRES


def check_access_token(access_token):
    # 反序列划token
    # serializer = Serializer(settings.SECRET_KEY, ACCESS_TOKEN_EXPIRES)
    key = settings.SECRET_KEY
    data = access_token
    # access_token = serializer.loads(access_token)
    access_token = jwt.decode(access_token, key)
    return access_token


def generate_eccess_token(openid):
    """
    签名openid
    :param openid: 用户的openid
    :return: access_token
    """
    # serializer = Serializer(settings.SECRET_KEY, ACCESS_TOKEN_EXPIRES)
    key = settings.SECRET_KEY
    data = {'openid': openid}
    heard = {"alg": "HS256"}
    # token = serializer.dumps(data)
    token = jwt.encode(heard=heard, payload=data, key=key)
    return token.decode()


"""
生成签验
from authlib.jose import jwt,JoseError
def generate_token()
    #签名算法
    heard={"alg":"HS256"}
    #用于签名的密钥
    key=settings.SECRET_KEY
    #待签名负载
    data={"id":user.id,"email":user.email}
    token=jwt.encode(header=header,payload=data,key=key)  #加密后为byte类型需decode()

反序列化解签
def check_token()
    #签名的密钥与加密是一致
    key=settings.SECRET_KEY
    data=jwt.decode(token,key)  
"""
