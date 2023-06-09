from datetime import datetime, timedelta
import jwt
from config.settings import SECRET_KEY


def encode_jwt(data):
    return jwt.encode(data, SECRET_KEY, 'HS256')


def decode_jwt(access_token):
    access_token = str.replace(str(access_token), 'Bearer ', '')
    access_token = access_token[1:-1]
    return jwt.decode(access_token, SECRET_KEY, algorithms='HS256', options={"verify_aud": False},)


def generate_access_token(user_id):
    iat = datetime.now()
    data = {
        "iat": iat.timestamp(),
        "exp": iat + timedelta(days=7),
        "user_id": user_id,
    }
    return encode_jwt(data)
