from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, verbose_name="名称", default="初始用户")

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # 生产环境请使用密码哈希
    auth_token = models.CharField(max_length=64, blank=True, null=True)  # 存放登录后生成的 token
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

