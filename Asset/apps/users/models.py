from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import CharField
from apps import asset

GENDER_CHOICE = (('male', '男'), ('female', '女'))
isADMIN = (('1', '是'), ('0', '否'))


# 定义用户模型，添加额外的字段
class UserProfile(AbstractUser):
    name = models.CharField(max_length=8, verbose_name='姓名', default='')
    sex = models.CharField(max_length=4, verbose_name='性别', choices=GENDER_CHOICE, default='')
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)
    isadmin = models.CharField(max_length=4, choices=isADMIN, verbose_name='是否管理员', default='0', blank=True)
    bg_telephone = models.CharField(max_length=16, verbose_name='办公电话', blank=True)
    mobile = models.CharField(max_length=16, verbose_name='手机号码', blank=True)
    is_superuser = models.IntegerField(verbose_name='是否超级管理员', default=0)
    modify_time = models.DateTimeField(default=datetime.now, verbose_name='修改时间')

    class Meta:
        db_table = 'User'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.username


class Department(models.Model):
    dp_name = models.CharField(max_length=8, verbose_name='部门', default='默认')

    class Meta:
        db_table = 'Department'
        verbose_name = '用户部门'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.dp_name


# 定义用户操作日志模型
class UserOperateLog(models.Model):
    username = models.CharField(max_length=10, verbose_name='人员')
    type = models.CharField(max_length=10, verbose_name='操作类型')
    content = models.CharField(max_length=20, verbose_name='操作资产')
    asset_id = models.CharField(max_length=4, verbose_name='资产ID', null=True, blank=True)
    modify_time = models.DateTimeField(default=datetime.now, verbose_name='操作时间')

    class Meta:
        db_table = 'UserOperateLog'
        verbose_name = '用户操作日志'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username + '.' + self.type
