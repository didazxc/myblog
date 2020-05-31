from flask import current_app
from sqlalchemy import Column, Integer, String, JSON, Float, Boolean
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from dataclasses import dataclass
from . import db


@dataclass
class User(db.Model):
    __tablename__ = 'users'
    id:int = Column(Integer, primary_key=True)
    name:str = Column(String(127), unique=True, nullable=False)
    password = Column(String(255))

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns if c.name!='password'}

    @classmethod
    def from_dict(cls,dt):
        obj = cls()
        for name in dt:
            if hasattr(obj,name):
                setattr(obj,name,dt[name])
        return obj

    # 获取token，有效时间1d
    def generate_auth_token(self, expiration = 86400):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in = expiration)
        token = s.dumps({ 'id': self.id })
        return str(token,encoding='utf-8')

    # 解析token，确认登录的用户身份
    @staticmethod
    def verify_auth_token(token):
        token = bytes(token, encoding = "utf8")
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['id'])
        return user
