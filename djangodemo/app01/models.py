from django.db import models

# Create your models here.
# 创建模型类，继承models.Model
class UserInfo(models.Model):
    # 类属性，对应着数据库中每一个字段的具体数据类型
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()

class Department(models.Model):
    title = models.CharField (max_length=16)