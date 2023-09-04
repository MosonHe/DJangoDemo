from django.db import models

# Create your models here.
class Department(models.Model):
    '''部门表'''
    title = models.CharField(verbose_name='部门名称', max_length=32)
    depart_id = models.SmallIntegerField(unique=True, verbose_name='部门ID')
    desc = models.CharField(verbose_name='描述信息',max_length=128, null=True, blank=True)


class UserInfo(models.Model):
    '''用户信息表'''
    name = models.CharField(verbose_name='姓名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.SmallIntegerField(verbose_name='年龄')
    # 定义一个元组，存储gender的对应关系，这个是DJango中的约束，和数据库无关
    gedner_choices = (
        (1, '男'),
        (2, '女')
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices= gedner_choices)
    # decimal准确的小数值，max_digits代表数字总个数（负号不算），decimal_places是小数点后个数。（max_digits最大值为65，decimal_places最大值为30）
    account = models.DecimalField(verbose_name='账户余额', max_digits=10, decimal_places=2, default=0)
    crate_time = models.DateTimeField(verbose_name='入职时间')
    # 这样去创建depart_id列是没有约束的
    # depart_id = models.BigIntegerField(verbose_name='部门ID')
    # 1.有约束、带外键的创建方法
    #  - to表示与哪一张表关联
    #  - to_field表示与表中的那一列关联
    # 2.DJango会自动将depart转换为depart_id，生成数据列`name`_id，_id是固定的增加的
    # 3.当外键关联的父类表格（列）被删除了，有多种处理方式,例如:
    #  - 级联删除子表格中所有数据
    # depart = models.ForeignKey(to="Department", to_field="depart_id", unique=True, on_delete=models.CASCADE)
    #  - 在允许列为空的条件下，将子表中数据置空
    # depart = models.ForeignKey(to="Department", to_field="depart_id", null=True, blank=True, on_delete=models.SET_NULL)
    #  - 在有默认值的情况下，设置被删除的值为默认值
    # depart = models.ForeignKey(to="Department", to_field="depart_id", default= 10, on_delete=models.SET_DEFAULT)
    depart = models.OneToOneField(to="Department", to_field="depart_id", default= 10, on_delete=models.SET_DEFAULT)

