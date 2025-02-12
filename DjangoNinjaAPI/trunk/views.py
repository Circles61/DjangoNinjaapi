from ninja import Router
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from ninja.errors import HttpError
from trunk.models import User
from trunk.serializers import UserSchema, RegisterSchema, LoginSchema

router = Router()#实例化一个Router对象，统一管理API接口
#后面只需使用装饰器@router.get、@router.post、@router.put、@router.delete等来定义API接口即可

# ==========================
# 用户信息 CRUD 接口
# ==========================

@router.get("/users/", response=list[UserSchema])#对返回的数据进行序列化
def list_users(request):
    """
    GET /api/users/
    获取所有用户的信息
    """
    return User.objects.all()

@router.get("/users/{user_id}", response=UserSchema)#对返回的数据进行序列化
def get_user(request, user_id: int):
    """
    GET /api/users/{user_id}
    根据用户ID获取用户信息
    """
    return get_object_or_404(User, id=user_id)

@router.post("/users/", response={201: dict})
def create_user(request, user: UserSchema):
    """
    POST /api/users/
    创建新用户
    请求体数据使用 Pydantic Schema 校验（UserSchema）
    请求体示例 JSON:
    {
        "name": "张三",
        "email": "test@example.com",
        "password": "<PASSWORD>",
        "age": 25
        }
    """
    new_user = User.objects.create(**user.dict())
    return {"message": "用户创建成功", "user_id": new_user.id}

@router.put("/users/{user_id}", response={200: dict})
def update_user(request, user_id: int, user: UserSchema):
    """
    PUT /api/users/{user_id}
    更新用户信息，覆盖所有字段
    """
    user_obj = get_object_or_404(User, id=user_id)
    for key, value in user.dict().items():
        setattr(user_obj, key, value)
    user_obj.save()
    return {"message": "用户更新成功"}

@router.delete("/users/{user_id}", response={200: dict})
def delete_user(request, user_id: int):
    """
    DELETE /api/users/{user_id}
    删除指定用户
    """
    user_obj = get_object_or_404(User, id=user_id)
    user_obj.delete()
    return {"message": "用户删除成功"}

# ==========================
# 认证相关接口
# ==========================

@router.post("/auth/register", response={201: dict})
def register(request, data: RegisterSchema):
    """
    POST /api/auth/register
    用户注册接口
    请求体示例 JSON:
    {
        "name": "张三",
        "email": "test@example.com",
        "password": "password123"
    }
    """
    if User.objects.filter(email=data.email).exists():
        raise HttpError(400, "该邮箱已被注册")
    new_user = User.objects.create(name=data.name, email=data.email, password=data.password)
    return {"message": "注册成功", "user_id": new_user.id}

@router.post("/auth/login", response={200: dict})
def login(request, data: LoginSchema):
    """
    POST /api/auth/login
    用户登录接口
    请求体示例 JSON:
    {
        "email": "test@example.com",
        "password": "password123"
    }
    """
    user = get_object_or_404(User, email=data.email)
    # 注意：实际项目应使用密码哈希验证，此处为示例（明文比较）
    if user.password != data.password:
        raise HttpError(401, "用户名或密码错误")
    token = get_random_string(32)
    user.auth_token = token
    user.save()
    return {"message": "登录成功", "token": token}

#接口新增方式一：此时访问的路由为：http://127.0.0.1:8000/api/StudyUserDataApi/
'''

# 新增一个“学习用户数据”接口：
@router.get("/StudyUserDataApi/", response=list[UserSchema])
def list_study_user_data(request):
    # 假设你在 User 模型中有区分学习用户的数据，或根据其它逻辑筛选数据
    study_users = User.objects.filter(name__icontains="study")
    return study_users
'''
