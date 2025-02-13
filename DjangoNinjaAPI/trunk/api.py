# API 实例注册文件
# 将各个具体业务模块的路由（通常通过 Router 定义）挂载进去。
from ninja import NinjaAPI

from trunk.views import router  # 从 views.py 中导入定义好的 Router

# 创建 API 实例并启用 JWT 认证
api = NinjaAPI(title="Django Ninja API", version="1.0")
# 将 router 中所有路由接口挂载到当前根路径
api.add_router("", router)

#路由创建新增方式二：
# 除了挂载原来已有的 Router，还要额外挂载新的 study_router
#如：api.add_router("/study", study_router)

'''
新增路由接口
'''
#下面的接口是模块化管理，也就是新增路由接口时，然后新增一个py文件
# api.add_router("/users", user_router)
# api.add_router("/orders", order_router)