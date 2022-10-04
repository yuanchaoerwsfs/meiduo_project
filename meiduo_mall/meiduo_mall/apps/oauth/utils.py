from itsdangerous import TimedSerializer as Serializer
from django.conf import settings
from .constants import ACCESS_TOKEN_EXPIRES


def generate_eccess_token(openid):
    """
    签名openid
    :param openid: 用户的openid
    :return: access_token
    """
    serializer = Serializer(settings.SECRET_KEY, ACCESS_TOKEN_EXPIRES)
    data = {'openid': openid}
    token = serializer.dumps(data)
    return token.decode()
