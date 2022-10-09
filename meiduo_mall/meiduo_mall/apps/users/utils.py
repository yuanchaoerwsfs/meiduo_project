from django.contrib.auth.backends import ModelBackend
from django.conf import settings
# from itsdangerous import TimedSerializer as Serializer, BadData
from .constants import VERIFY_EMAIL_TOKEN_EXPIRES
from .models import User
import re
from authlib.jose import jwt, JoseError


def check_verify_email_token(token):
    # serializer = Serializer(settings.SECRET_KEY, VERIFY_EMAIL_TOKEN_EXPIRES)
    key = settings.SECRET_KEY
    try:
        data_dirt = jwt.decode(token,key)
    except JoseError:
        return None
    else:
        user_id = data_dirt.get('user_id')
        email = data_dirt.get('email')
        try:
            user = User.objects.get(id=user_id, email=email)
        except User.DoesNotExist:
            return None
        else:
            return user


# 反序列化邮件认证返回的token


# 生成邮件认证url并加密
def generate_verify_email_url(user):
    # serializer = Serializer(settings.SECRET_KEY, VERIFY_EMAIL_TOKEN_EXPIRES)  #此方法已经弃用
    key = settings.SECRET_KEY
    data = {"user_id": user.id, "email": user.email}
    header = {"alg": 'HS256'}
    # token = serializer.dumps(data)
    token = jwt.encode(header=header, payload=data, key=key).decode()
    verify_url = settings.EMAIL_VERIFY_URL + '?token=' + token
    return verify_url


def get_user_by_account(account):
    try:
        if re.match('^1[3-9]\d{9}$', account):
            user = User.objects.get(mobile=account)
            print(user)
        else:
            user = User.objects.get(username=account)
    except User.DoesNotExist:
        return None
    else:
        print(user)
        return user


class UsernameMobileAuthBackend(ModelBackend):
    """
    class ModelBackend(BaseBackend):

        Authenticates against settings.AUTH_USER_MODEL.


        def authenticate(self, request, username=None, password=None, **kwargs):
            if username is None:
                username = kwargs.get(UserModel.USERNAME_FIELD)
            if username is None or password is None:
                return
            try:
                user = UserModel._default_manager.get_by_natural_key(username)
            except UserModel.DoesNotExist:
                # Run the default password hasher once to reduce the timing
                # difference between an existing and a nonexistent user (#20760).
                UserModel().set_password(password)
            else:
                if user.check_password(password) and self.user_can_authenticate(user):
                    return user
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_account(username)
        if user and user.check_password(password):
            return user
