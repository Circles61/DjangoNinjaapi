# 原来DjangoNinjaAPI项目中序列化器的名字是Pydantic
#但实际内容基于 Ninja 的 Schema。
from ninja import Schema

class UserSchema(Schema):
    name: str
    email: str
# DjangoNinjaAPI/trunk/schemas.py


class RegisterSchema(Schema):
    name: str
    email: str
    password: str

class LoginSchema(Schema):
    email: str
    password: str

# 此外，也可以保留用户信息的 Schema 用于 CRUD（如果尚未定义）

