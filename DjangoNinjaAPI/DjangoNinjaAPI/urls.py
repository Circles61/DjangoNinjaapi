"""
URL configuration for DjangoNinjaAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
from django.urls import path, include
from trunk.api import api
#
'''全局路由配置'''
urlpatterns = [
    
    #path("admin/", admin.site.urls),
    path('api/', include('trunk.urls')),  # 绑定trunk应用的url
# path('', include('trunk.urls'))   避免出现/api/的情况，直接绑定trunk应用的url
]


