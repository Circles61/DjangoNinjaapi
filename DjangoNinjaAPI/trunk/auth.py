# trunk/auth.py
# 可以在此处定义自定义认证函数或 JWT 处理逻辑
from ninja_jwt.authentication import JWTAuth

jwt_auth = JWTAuth()  # JWT 认证实例
