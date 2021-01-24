from django.contrib import admin

from .models import Asset, AssetType, AssetStatus
from ..users.models import Department


class AssetAdmin(admin.ModelAdmin):
    pass


class AssetTypeAdmin(admin.ModelAdmin):
    pass


class AssetStatusAdmin(admin.ModelAdmin):
    pass


class DepartmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Asset, AssetAdmin)
admin.site.register(AssetType, AssetTypeAdmin)
admin.site.register(AssetStatus, AssetTypeAdmin)
admin.site.register(Department, AssetTypeAdmin)
