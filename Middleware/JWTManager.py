import os
from datetime import datetime, timedelta, timezone

import jwt
from typing import Optional
from dotenv import load_dotenv

# load variables from .env file
load_dotenv()

SECRECT_KEY = os.getenv('SECRECT_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')


class JWTManager:

    @staticmethod
    def generate_token(data:dict, expires_delta:Optional[timedelta]=None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(tz=timezone.utc) + expires_delta
        else:
            expire = datetime.now(tz=timezone.utc) + timedelta(minutes=float(ACCESS_TOKEN_EXPIRE_MINUTES))
        
        to_encode.update({'exp': expire})
        encode_jwt = jwt.encode(to_encode, SECRECT_KEY, ALGORITHM)
        return encode_jwt
    
    @staticmethod
    def verify_jwt(token:str):
        try:
            decode_token = jwt.decode(token, SECRECT_KEY, algorithms=[ALGORITHM])
            current_timestamp = datetime.now(tz=timezone.utc).timestamp()
            if not decode_token:
                raise ValueError('Invalid token!')
            elif decode_token['exp'] <= current_timestamp:
                raise ValueError('Token expired!')
            
            return True
        except ValueError as error:
            print(error)
            return False
