from django.urls import path
from trunk.api import api
#业务内app的路由局部 URL 路径，这里是空的，因为我们只需要挂载api的urls
#相当于访问http://127.0.0.1:8000/api/
urlpatterns = [
    path('', api.urls),#这个是默认的路由，挂载到api的urls上,一般保持不动即可
]

