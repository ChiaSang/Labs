from datetime import datetime

from django.db import models

from apps import asset, users


ASSETSTATUS = (('1', '正常'), ('2', '损坏'), ('2', '报废'))
# SERVERTYPE = (('1', '台式服务器'), ('2', '机架式服务器'), ('2', '刀片式服务器'))


class Asset(models.Model):
    """
    资产表
    """
    asset_type = models.ForeignKey('asset.AssetType', on_delete=models.CASCADE)
    asset_id = models.AutoField(primary_key=True, verbose_name='资产ID')
    asset_name = models.CharField(max_length=64,verbose_name='资产名称',null=True, blank=False)
    asset_model = models.CharField(max_length=16,verbose_name='型号',blank=True)
    specification = models.CharField(max_length=4,verbose_name='规格',blank=True)
    quantity = models.IntegerField(verbose_name='数量', default=0, blank=True)
    manufacture = models.CharField(max_length=32, verbose_name='制造商', null=True, blank=True)
    server_type = models.CharField(max_length=8, verbose_name='计算机/服务器机箱类型', null=True, blank=True)
    power = models.CharField(max_length=4, verbose_name='功率', null=True,blank=True)
    asset_holder = models.ForeignKey('users.UserProfile',
                                     verbose_name='所有人',
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True)
    asset_status = models.ForeignKey('asset.AssetStatus',
                                     verbose_name='资产状态',
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     blank=True)
    asset_dep = models.ForeignKey('users.Department',
                                  verbose_name='所属部门',
                                  on_delete=models.SET_NULL,
                                  null=True,
                                  blank=True)
    purchase_time = models.DateField(default=datetime.now,verbose_name='采购时间',blank=True)
    used_time = models.CharField(max_length=8, verbose_name='使用年限', default=0, blank=True)
    asset_uuid = models.CharField(max_length=64,
                                  verbose_name='唯一标示',
                                  unique=True,
                                  null=True,
                                  blank=True)
    comment = models.CharField(max_length=512, verbose_name='备注', blank=True)
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        db_table = 'Asset'
        verbose_name = '资产表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.asset_name


class AssetType(models.Model):
    """
    资产类型表
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )
    asset_type = models.CharField(max_length=16, verbose_name='资产类型名')
    code = models.CharField(default="",
                            max_length=8,
                            verbose_name="类别code",
                            help_text="类别code")
    category_type = models.IntegerField(choices=CATEGORY_TYPE,
                                        verbose_name="类目级别",
                                        help_text="类目级别",
                                        default=1)
    parent_category = models.ForeignKey("self",
                                        null=True,
                                        blank=True,
                                        verbose_name="父类目级别",
                                        help_text="父目录",
                                        related_name="sub_cat",
                                        on_delete=models.CASCADE)

    class Meta:
        db_table = 'AssetType'
        verbose_name = '资产类型表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.asset_type


class AssetStatus(models.Model):
    """
    资产状态表
    """
    asset_status = models.CharField(max_length=16,  choices=ASSETSTATUS, verbose_name='资产状态')

    class Meta:
        db_table = 'AssetStatus'
        verbose_name = '资产状态表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.asset_status


class AssetHistory(models.Model):
    """
    资产历史表
    """
    modify_operation = models.CharField(max_length=8, null=True, blank=True)
    asset_type = models.CharField(max_length=8, null=True, blank=True)
    asset_id = models.CharField(max_length=4, null=True, blank=True)
    asset_name = models.CharField(max_length=64, null=True, blank=True)
    asset_model = models.CharField(max_length=32, blank=True)
    specification = models.CharField(max_length=256, blank=True)
    asset_holder = models.CharField(max_length=32, blank=True)
    asset_status = models.CharField(max_length=32, blank=True)
    asset_dep = models.CharField(max_length=32, blank=True)
    purchase_time = models.DateField(default=datetime.now,
                                     verbose_name='采购时间',
                                     blank=True)
    comment = models.CharField(max_length=512, verbose_name='备注', blank=True)
    modify_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    class Meta:
        db_table = 'AssetHistory'
        verbose_name = '资产历史表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.asset_name


class AssetMaintenance(models.Model):
    """
    资产维修表
    """
    asset_id = models.CharField(max_length=4, null=True, blank=True)
    maintenance_info = models.CharField(max_length=256, null=True, blank=True)
    date = models.DateField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'AssetMaintenance'
        verbose_name = '资产维修表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.asset_id