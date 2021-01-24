from django.urls import path

from apps.asset.views import AssetEditView, AssetHistoryView, AssetItemInfoView, AssetListEditView, AssetAddView, AssetDetailView,AssetModifyView, AssetDeleteView, \
    AssetExportView, AssetMaintenanceDetailView, AssetMaintenanceView, TypeListView, TypeAddView, TypeDetailView, TypeModifyView, TypeDeleteView, PrintQrcodeView

urlpatterns = [
    # 资产url
    path('list/', AssetListEditView.as_view(), name='asset_list'),
    path('edit/', AssetEditView.as_view(), name='asset_edit'),
    path('add/', AssetAddView.as_view(), name='asset_add'),
    path('detail/<int:asset_id>/', AssetDetailView.as_view(), name='asset_detail'),
    path('item/info/<int:asset_id>/', AssetItemInfoView.as_view(), name='asset_item_info'),
    path('modify/', AssetModifyView.as_view(), name='asset_modify'),
    path('delete/<int:asset_id>/', AssetDeleteView.as_view(), name='asset_delete'),
    path('export/', AssetExportView.as_view(), name='asset_export'),
    path('printqrcode/<int:asset_id>/', PrintQrcodeView.as_view(), name='asset_qrcode'),
    path('history/', AssetHistoryView.as_view(), name='asset_history'),
    path('maintenance/list/', AssetMaintenanceView.as_view(), name='asset_maintenance'),
    path('maintenance/<int:asset_id>/', AssetMaintenanceDetailView.as_view(), name='asset_maintenance_detail'),

    # 资产类型url
    path('type/list/', TypeListView.as_view(), name='type_list'),
    path('type/add/', TypeAddView.as_view(), name='type_add'),
    path('type/detail/<int:type_id>/', TypeDetailView.as_view(), name='type_detail'),
    path('type/modify/', TypeModifyView.as_view(), name='type_modify'),
    path('type/delete/<int:type_id>/', TypeDeleteView.as_view(), name='type_delete'),
]
