from datetime import datetime

from django import forms

from .models import Asset, AssetType


# 定义资产表单验证
class AssetForm(forms.ModelForm):
    # asset_name = forms.CharField(max_length=64)
    # asset_model = forms.CharField(max_length=32, required=False)
    # specification = forms.CharField(max_length=256, required=False)
    # asset_holder = forms.CharField(required=False)
    # department = forms.CharField(max_length=16)
    # purchase_time = forms.CharField(max_length=16)
    # used_time = forms.CharField(max_length=16, required=False)
    # asset_uuid = forms.CharField(max_length=128, required=False)
    # comment = forms.CharField(max_length=512, required=False)

    class Meta:
        model = Asset
        fields = ['asset_type', 'asset_name', 'asset_model', 'specification', 'asset_holder', 'asset_dep',
                  'purchase_time', 'comment']


# 定义资产类型表单验证
class AssetTypeForm(forms.ModelForm):
    # type_id = forms.IntegerField()
    # asset_type = forms.CharField(required=True)
    #
    # def clean(self):
    #     cleaned_data = super(AssetTypeForm, self).clean()
    #     return self.cleaned_data

    class Meta:
        model = AssetType
        fields = ['asset_type']
