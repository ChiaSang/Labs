import base64
from datetime import date, datetime, timedelta, time
from django.utils.six import BytesIO

import qrcode
from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.db.models import Q
from pure_pagination import Paginator, PageNotAnInteger
import csv, uuid

from apps.asset.models import Asset, AssetHistory, AssetMaintenance, AssetType, AssetStatus
from apps.asset.forms import AssetForm
from apps.users.models import UserOperateLog, UserProfile, Department
from assetadmin.settings import per_page
from apps.utils.mixin_utils import LoginRequiredMixin


class IndexView(LoginRequiredMixin, View):
    """
    首页概览
    """
    def get(self, request):
        total = Asset.objects.count()
        normal = Asset.objects.filter(
            asset_status__asset_status__icontains='正常').count()
        broken = Asset.objects.filter(
            asset_status__asset_status__icontains='损坏').count()
        discarded = Asset.objects.filter(
            asset_status__asset_status__icontains='报废').count()
        return render(
            request, 'asset/index.html', {
                'total': total,
                'normal': normal,
                'broken': broken,
                'discarded': discarded
            })


class AssetListEditView(LoginRequiredMixin, View):
    """
    资产台账
    """
    def get(self, request):
        assets_types = AssetType.objects.all()
        search = request.GET.get('search')
        if search:
            search = request.GET.get('search').strip()
            # 如果输入的是纯数字，则将序号也加入到搜索的列表中来
            try:
                search_int = int(search)
                assets = Asset.objects.filter(Q(asset_id=search_int) | Q(asset_name__icontains=search)
                                              | Q(asset_model__icontains=search) | Q(
                    specification__icontains=search)
                                              | Q(asset_holder__username__icontains=search) | Q(
                    asset_type__asset_type__icontains=search)
                                              | Q(asset_dep__dp_name__icontains=search) | Q(
                    asset_status__asset_status__icontains=search)). \
                    order_by('asset_id')
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(assets, per_page=per_page, request=request)
                p_assets = p.page(page)
                start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
                return render(
                    request, 'asset/assets_list.html', {
                        'p_assets': p_assets,
                        'start': start,
                        'assets_types': assets_types
                    })
            except Exception:
                assets = Asset.objects.filter(Q(asset_name__icontains=search)
                                              | Q(asset_model__icontains=search) | Q(
                    specification__icontains=search)
                                              | Q(asset_holder__username__icontains=search) | Q(
                    asset_type__asset_type__icontains=search)
                                              | Q(asset_dep__dp_name__icontains=search) | Q(
                    asset_status__asset_status__icontains=search)). \
                    order_by('asset_id')
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(assets, per_page=per_page, request=request)
                p_assets = p.page(page)
                start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
                return render(
                    request, 'asset/assets_list.html', {
                        'p_assets': p_assets,
                        'start': start,
                        'assets_types': assets_types
                    })
        else:
            assets = Asset.objects.all().order_by('-modify_time')
        if request.user.is_superuser == 1 or request.user.isadmin == '1':  # 用户只能看自己的资产
            assets = Asset.objects.all().order_by('-modify_time')
            # 分页功能实现
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(assets, per_page=per_page, request=request)
            p_assets = p.page(page)
            start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
            return render(request, 'asset/assets_list.html', {
                'p_assets': p_assets,
                'start': start,
                'assets_types': assets_types
            })
        else:
            assets_holder = Asset.objects.filter(asset_holder_id=request.user)
            # 分页功能实现
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(assets_holder, per_page=per_page, request=request)
            p_assets = p.page(page)
            start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
            return render(request, 'asset/assets_list.html', {
                'p_assets': p_assets,
                'start': start,
                'assets_types': assets_types
            })


class AssetMaintenanceView(LoginRequiredMixin, View):
    """
    资产维修
    """
    def get(self, request):
        assets_types = AssetType.objects.all()
        search = request.GET.get('search')
        if search:
            search = request.GET.get('search').strip()
            # 如果输入的是纯数字，则将序号也加入到搜索的列表中来
            try:
                search_int = int(search)
                assets = Asset.objects.filter(Q(asset_id=search_int) | Q(asset_name__icontains=search)
                                              | Q(asset_model__icontains=search) | Q(
                    specification__icontains=search)
                                              | Q(asset_holder__username__icontains=search) | Q(
                    asset_type__asset_type__icontains=search)
                                              | Q(asset_dep__dp_name__icontains=search) | Q(
                    asset_status__asset_status__icontains=search)). \
                    order_by('asset_id')
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(assets, per_page=per_page, request=request)
                p_assets = p.page(page)
                start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
                return render(
                    request, 'asset/assets_maintenance_list.html', {
                        'p_assets': p_assets,
                        'start': start,
                        'assets_types': assets_types
                    })
            except Exception:
                assets = Asset.objects.filter(Q(asset_name__icontains=search)
                                              | Q(asset_model__icontains=search) | Q(
                    specification__icontains=search)
                                              | Q(asset_holder__username__icontains=search) | Q(
                    asset_type__asset_type__icontains=search)
                                              | Q(asset_dep__dp_name__icontains=search) | Q(
                    asset_status__asset_status__icontains=search)). \
                    order_by('asset_id')
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(assets, per_page=per_page, request=request)
                p_assets = p.page(page)
                start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
                return render(
                    request, 'asset/assets_maintenance_list.html', {
                        'p_assets': p_assets,
                        'start': start,
                        'assets_types': assets_types
                    })
        else:
            assets = Asset.objects.all().order_by('-modify_time')
        if request.user.is_superuser == 1 or request.user.isadmin == '1':  # 用户只能看自己的资产
            assets = Asset.objects.all().order_by('-modify_time')
            # 分页功能实现
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(assets, per_page=per_page, request=request)
            p_assets = p.page(page)
            start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
            return render(request, 'asset/assets_maintenance_list.html',
                          {'p_assets': p_assets})
        else:
            assets_holder = Asset.objects.filter(asset_holder_id=request.user)
            # 分页功能实现
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(assets_holder, per_page=per_page, request=request)
            p_assets = p.page(page)
            start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
            return render(request, 'asset/assets_maintenance_list.html',
                          {'p_assets': p_assets})


class AssetMaintenanceDetailView(LoginRequiredMixin, View):
    """
    资产维修信息增加
    """
    def get(self, request, asset_id):
        fAsset = Asset.objects.get(asset_id=asset_id)
        return render(request, 'asset/assets_maintenance_detail.html',
                      {'fAsset': fAsset})

    def post(self, request, asset_id):
        AssetMaintenance.objects.update_or_create(
            asset_id=asset_id,
            maintenance_info=request.POST.get('maintenance'),
            date=request.POST.get('maintenance_time'))
        new_log = UserOperateLog(
            username=request.user.username,
            type='增加资产维修信息',
            content=Asset.objects.get(asset_id=asset_id).asset_name,
            asset_id=request.POST.get('asset_id'))
        new_log.save()
        return HttpResponseRedirect((reverse('asset:asset_list')))


class AssetEditView(LoginRequiredMixin, View):
    """
    资产变动
    """
    def get(self, request):
        assets_types = AssetType.objects.all()
        search = request.GET.get('search')
        if search:
            search = request.GET.get('search').strip()
            # 如果输入的是纯数字，则将序号也加入到搜索的列表中来
            try:
                search_int = int(search)
                assets = Asset.objects.filter(Q(asset_id=search_int) | Q(asset_name__icontains=search)
                                              | Q(asset_model__icontains=search) | Q(
                    specification__icontains=search)
                                              | Q(asset_holder__username__icontains=search) | Q(
                    asset_type__asset_type__icontains=search)
                                              | Q(asset_dep__dp_name__icontains=search) | Q(
                    asset_status__asset_status__icontains=search)). \
                    order_by('asset_id')
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(assets, per_page=per_page, request=request)
                p_assets = p.page(page)
                start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
                return render(
                    request, 'asset/assets_list_edit.html', {
                        'p_assets': p_assets,
                        'start': start,
                        'assets_types': assets_types
                    })
            except Exception:
                assets = Asset.objects.filter(Q(asset_name__icontains=search)
                                              | Q(asset_model__icontains=search) | Q(
                    specification__icontains=search)
                                              | Q(asset_holder__username__icontains=search) | Q(
                    asset_type__asset_type__icontains=search)
                                              | Q(asset_dep__dp_name__icontains=search) | Q(
                    asset_status__asset_status__icontains=search)). \
                    order_by('asset_id')
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(assets, per_page=per_page, request=request)
                p_assets = p.page(page)
                start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
                return render(
                    request, 'asset/assets_list_edit.html', {
                        'p_assets': p_assets,
                        'start': start,
                        'assets_types': assets_types
                    })
        else:
            assets = Asset.objects.all().order_by('asset_id')
        if request.user.is_superuser == 1 or request.user.isadmin == '1':
            assets = Asset.objects.all()
            # 分页功能实现
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(assets, per_page=per_page, request=request)
            p_assets = p.page(page)
            start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
            return render(request, 'asset/assets_list_edit.html', {
                'p_assets': p_assets,
                'start': start,
                'assets_types': assets_types
            })
        else:
            assets_holder = Asset.objects.filter(asset_holder_id=request.user)
            # 分页功能实现
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(assets_holder, per_page=per_page, request=request)
            p_assets = p.page(page)
            start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
            return render(request, 'asset/assets_list_edit.html', {
                'p_assets': p_assets,
                'start': start,
                'assets_types': assets_types
            })


class AssetHistoryView(LoginRequiredMixin, View):
    """
    资产历史
    """
    def get(self, request):
        assets_types = AssetType.objects.all()
        search = request.GET.get('search')
        if search:
            search = request.GET.get('search').strip()
            # 如果输入的是纯数字，则将序号也加入到搜索的列表中来
            try:
                search_int = int(search)
                assets = Asset.objects.filter(Q(asset_id=search_int) | Q(asset_name__icontains=search)
                                              | Q(asset_model__icontains=search) | Q(
                    specification__icontains=search)
                                              | Q(asset_holder__username__icontains=search) | Q(
                    asset_type__asset_type__icontains=search)
                                              | Q(asset_dep__dp_name__icontains=search) | Q(
                    asset_status__asset_status__icontains=search)). \
                    order_by('asset_id')
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(assets, per_page=per_page, request=request)
                p_assets = p.page(page)
                start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
                return render(
                    request, 'asset/assets_history.html', {
                        'p_assets': p_assets,
                        'start': start,
                        'assets_types': assets_types
                    })
            except Exception:
                assets = Asset.objects.filter(Q(asset_name__icontains=search)
                                              | Q(asset_model__icontains=search) | Q(
                    specification__icontains=search)
                                              | Q(asset_holder__username__icontains=search) | Q(
                    asset_type__asset_type__icontains=search)
                                              | Q(asset_dep__dp_name__icontains=search) | Q(
                    asset_status__asset_status__icontains=search)). \
                    order_by('asset_id')
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(assets, per_page=per_page, request=request)
                p_assets = p.page(page)
                start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
                return render(
                    request, 'asset/assets_history.html', {
                        'p_assets': p_assets,
                        'start': start,
                        'assets_types': assets_types
                    })
        else:
            assets = Asset.objects.all().order_by('asset_id')
        if request.user.is_superuser == 1 or request.user.isadmin == '1':
            assets = Asset.objects.all()
            # 分页功能实现
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(assets, per_page=per_page, request=request)
            p_assets = p.page(page)
            start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
            return render(request, 'asset/assets_history.html', {
                'p_assets': p_assets,
                'start': start,
                'assets_types': assets_types
            })
        else:
            assets_holder = Asset.objects.filter(asset_holder_id=request.user)
            # 分页功能实现
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(assets_holder, per_page=per_page, request=request)
            p_assets = p.page(page)
            start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
            return render(request, 'asset/assets_history.html', {
                'p_assets': p_assets,
                'start': start,
                'assets_types': assets_types
            })


class AssetAddView(LoginRequiredMixin, View):
    """添加"""
    def get(self, request):
        users = UserProfile.objects.filter(is_superuser=0, is_staff='1')
        types = AssetType.objects.all()
        status = AssetStatus.objects.all()
        deps = Department.objects.all()
        return render(
            request, 'asset/asset_add.html', {
                'users': users,
                'assets_types': types,
                'asset_status': status,
                'asset_deps': deps
            })

    def post(self, request):
        newAsset = AssetForm(request.POST)
        # 判断表单是否正确
        if newAsset.is_valid():
            udate = request.POST.get('purchase_time')
            if UserProfile.objects.filter(id=request.POST.get('asset_holder', 0)).first():
                storeAsset = Asset.objects.create(
                    asset_type=AssetType.objects.filter(
                        id=request.POST.get('asset_type', 0)).first(),
                    asset_name=request.POST.get('asset_name').strip(),
                    asset_model=request.POST.get('asset_model'),
                    specification=request.POST.get('specification'),
                    asset_holder=UserProfile.objects.filter(
                        id=request.POST.get('asset_holder', 0)).first(),
                    asset_dep=Department.objects.filter(
                        id=request.POST.get('asset_dep', 0)).first(),
                    asset_status=AssetStatus.objects.filter(
                        id=request.POST.get('asset_status', 0)).first(),
                    quantity=int(request.POST.get('quantity')),
                    manufacture=request.POST.get('manufacture'),
                    server_type=request.POST.get('server_type'),
                    power=request.POST.get('power'),
                    purchase_time=request.POST.get('purchase_time'),
                    used_time=(datetime.today() -
                               datetime.strptime(udate, '%Y-%m-%d')).days,
                    asset_uuid=uuid.uuid3(
                        uuid.NAMESPACE_URL,
                        request.POST.get('asset_name').strip()),
                    comment=request.POST.get('comment'),
                    modify_time=datetime.now())
                new_history = AssetHistory(
                    modify_operation='新增资产',
                    asset_type=storeAsset.asset_type,
                    asset_id=storeAsset.asset_id,
                    asset_name=storeAsset.asset_name,
                    asset_model=storeAsset.asset_model,
                    specification=storeAsset.specification,
                    asset_holder=storeAsset.asset_holder,
                    asset_status=storeAsset.asset_status,
                    asset_dep=storeAsset.asset_dep,
                    comment=storeAsset.comment,
                    modify_time=datetime.now())
                new_history.save()
                new_log = UserOperateLog(
                    username=request.user.username,
                    type='增加资产',
                    content=request.POST.get('asset_name'),
                    asset_id=storeAsset.asset_id)
                new_log.save()
                return HttpResponseRedirect((reverse('asset:asset_list')))
        else:
            print('错误')
            return render(request, 'asset/asset_add.html', {'msg': '输入错误！'})


class AssetDetailView(LoginRequiredMixin, View):
    """变动详情页"""
    def get(self, request, asset_id):
        qr = qrcode.QRCode(
            version=5,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=3,
            border=1,
        )
        asset = Asset.objects.get(asset_id=asset_id)
        status = AssetStatus.objects.all()
        type = AssetType.objects.all()
        holders = UserProfile.objects.all()
        depart = Department.objects.all()
        qr_asset_info = '名称：{0} 型号：{1}\n所有人：{2} 部门：{3}'.format(
            asset.asset_name, asset.asset_model, asset.asset_holder.username,
            asset.asset_dep.dp_name)
        qr.add_data(qr_asset_info)
        qr.make(fit=True)
        img = qr.make_image()
        with Image.open(r"apps/asset/static/qrcode_model.jpg") as background:
            background.paste(img, (22, 22))
            font1 = ImageFont.truetype(r"apps/asset/static/FZFSJW.TTF", 20)
            font2 = ImageFont.truetype(r"apps/asset/static/FZFSJW.TTF", 30)
            bd = ImageDraw.Draw(background)
            bd.text((150, 30), '名称：' + asset.asset_name, (0, 0, 0), font=font1)
            bd.text((150, 65),
                    '型号：' + asset.asset_model, (0, 0, 0),
                    font=font1)
            bd.text((150, 100),
                    '所有人：' + asset.asset_holder.username, (0, 0, 0),
                    font=font1)
            bd.text((150, 135),
                    '部门：' + asset.asset_dep.dp_name, (0, 0, 0),
                    font=font1)
            bd.text((150, 170),
                    '标识码: ' + asset.asset_uuid[:8].upper(), (0, 0, 0),
                    font=font1)
            bd.text((150, 205),
                    '启用日期：' + asset.purchase_time.strftime("%Y-%m-%d"),
                    (0, 0, 0),
                    font=font1)
            bd.text((21, 140), '许昌市统', (0, 0, 0), font=font2)
            bd.text((21, 175), '计局资产', (0, 0, 0), font=font2)
            bd.text((21, 210), '统一标识', (0, 0, 0), font=font2)
            background.convert("L")
            buffer = BytesIO()  # 创建一个BytesIO临时保存生成图片数据
            background.save(buffer, format="PNG",
                            quality=100)  # 将图片字节数据放到BytesIO临时保存
            # image_stream = buffer.getvalue()  # 在BytesIO临时保存拿出数据
            img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
        return render(
            request, 'asset/asset_detail.html', {
                'asset': asset,
                'status': status,
                'types': type,
                'holders': holders,
                'departs': depart,
                'as_qrcode': img_str
            })


class AssetItemInfoView(LoginRequiredMixin, View):
    """
    单个资产信息展示
    """
    def get(self, request, asset_id):
        qr = qrcode.QRCode(
            version=5,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=3,
            border=1,
        )
        asset = Asset.objects.get(asset_id=asset_id)
        qr_asset_info = '名称：{0} 型号：{1}\n所有人：{2} 部门：{3}'.format(
            asset.asset_name, asset.asset_model, asset.asset_holder.username,
            asset.asset_dep.dp_name)
        qr.add_data(qr_asset_info)
        qr.make(fit=True)
        img = qr.make_image()
        with Image.open(r"apps/asset/static/qrcode_model.jpg") as background:
            background.paste(img, (22, 22))
            font1 = ImageFont.truetype(r"apps/asset/static/FZFSJW.TTF", 20)
            font2 = ImageFont.truetype(r"apps/asset/static/FZFSJW.TTF", 30)
            bd = ImageDraw.Draw(background)
            bd.text((150, 30), '名称：' + asset.asset_name, (0, 0, 0), font=font1)
            bd.text((150, 65),
                    '型号：' + asset.asset_model, (0, 0, 0),
                    font=font1)
            bd.text((150, 100),
                    '所有人：' + asset.asset_holder.username, (0, 0, 0),
                    font=font1)
            bd.text((150, 135),
                    '部门：' + asset.asset_dep.dp_name, (0, 0, 0),
                    font=font1)
            bd.text((150, 170),
                    '标识码: ' + asset.asset_uuid[:8].upper(), (0, 0, 0),
                    font=font1)
            bd.text((150, 205),
                    '启用日期：' + asset.purchase_time.strftime("%Y-%m-%d"),
                    (0, 0, 0),
                    font=font1)
            bd.text((21, 140), '许昌市统', (0, 0, 0), font=font2)
            bd.text((21, 175), '计局资产', (0, 0, 0), font=font2)
            bd.text((21, 210), '统一标识', (0, 0, 0), font=font2)
            background.convert("L")
            buffer = BytesIO()  # 创建一个BytesIO临时保存生成图片数据
            background.save(buffer, format="PNG",
                            quality=100)  # 将图片字节数据放到BytesIO临时保存
            img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
            if AssetHistory.objects.filter(asset_id=asset_id):
                assets_history = AssetHistory.objects.filter(
                    asset_id=asset_id).order_by('-modify_time')
                assets_maintenance = AssetMaintenance.objects.filter(
                    asset_id=asset_id).order_by('-date')
                return render(
                    request, 'asset/asset_item_info.html', {
                        'asset': asset,
                        'as_qrcode': img_str,
                        'assets_history': assets_history,
                        'assets_maintenance': assets_maintenance
                    })
            else:
                return render(request, 'asset/asset_item_info.html', {
                    'asset': asset,
                    'as_qrcode': img_str
                })


class PrintQrcodeView(LoginRequiredMixin, View):
    """打印二维码"""
    def get(self, request, asset_id):
        qr = qrcode.QRCode(
            version=5,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=3,
            border=1,
        )
        asset = Asset.objects.get(asset_id=asset_id)
        qr_asset_info = '名称：{0} 型号：{1}\n所有人：{2} 部门：{3}'.format(
            asset.asset_name, asset.asset_model, asset.asset_holder.username,
            asset.asset_dep.dp_name)
        qr.add_data(qr_asset_info)
        qr.make(fit=True)
        img = qr.make_image()
        with Image.open(r"apps/asset/static/qrcode_model.jpg") as background:
            background.paste(img, (22, 22))
            font1 = ImageFont.truetype(r"apps/asset/static/FZFSJW.TTF", 20)
            font2 = ImageFont.truetype(r"apps/asset/static/FZFSJW.TTF", 30)
            bd = ImageDraw.Draw(background)
            bd.text((150, 30), '名称：' + asset.asset_name, (0, 0, 0), font=font1)
            bd.text((150, 65),
                    '型号：' + asset.asset_model, (0, 0, 0),
                    font=font1)
            bd.text((150, 100),
                    '所有人：' + asset.asset_holder.username, (0, 0, 0),
                    font=font1)
            bd.text((150, 135),
                    '部门：' + asset.asset_dep.dp_name, (0, 0, 0),
                    font=font1)
            bd.text((150, 170),
                    '标识码: ' + asset.asset_uuid[:8].upper(), (0, 0, 0),
                    font=font1)
            bd.text((150, 205),
                    '启用日期：' + asset.purchase_time.strftime("%Y-%m-%d"),
                    (0, 0, 0),
                    font=font1)
            bd.text((21, 140), '许昌市统', (0, 0, 0), font=font2)
            bd.text((21, 175), '计局资产', (0, 0, 0), font=font2)
            bd.text((21, 210), '统一标识', (0, 0, 0), font=font2)
            background.convert("L")
            buffer = BytesIO()  # 创建一个BytesIO临时保存生成图片数据
            background.save(buffer, format="PDF",
                            quality=100)  # 将图片字节数据放到BytesIO临时保存
            image_stream = buffer.getvalue()  # 在BytesIO临时保存拿出数据
            img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
            return HttpResponse(image_stream, content_type="application/pdf")


class AssetModifyView(LoginRequiredMixin, View):
    """资产信息修改"""
    def post(self, request):
        asset_id = int(request.POST.get('asset_id'))
        asset_form = AssetForm(request.POST)
        if asset_form.is_valid():
            Asset.objects.filter(asset_id=asset_id).update(
                asset_type=AssetType.objects.filter(
                    id=request.POST.get('asset_type', 0)).first(),
                asset_name=request.POST.get('asset_name'),
                specification=request.POST.get('specification').strip(),
                asset_model=request.POST.get('asset_model').strip(),
                manufacture=request.POST.get('manufacture'),
                power=request.POST.get('power'),
                server_type=request.POST.get('server_type').strip(),
                quantity=int(request.POST.get('quantity')),
                purchase_time=request.POST.get('purchase_time'),
                asset_status=AssetStatus.objects.filter(
                    id=request.POST.get('asset_status', 0)).first(),
                asset_dep=Department.objects.filter(
                    id=request.POST.get('asset_dep', 0)).first(),
                asset_holder=UserProfile.objects.filter(
                    id=request.POST.get('asset_holder', 0)).first(),
                comment=request.POST.get('comment').strip(),
                modify_time=datetime.now())
            updateAsset = Asset.objects.get(asset_id=asset_id)
            new_history = AssetHistory(modify_operation='修改资产',
                                       asset_type=updateAsset.asset_type,
                                       asset_id=updateAsset.asset_id,
                                       asset_name=updateAsset.asset_name,
                                       asset_model=updateAsset.asset_model,
                                       specification=updateAsset.specification,
                                       asset_holder=updateAsset.asset_holder,
                                       asset_status=updateAsset.asset_status,
                                       asset_dep=updateAsset.asset_dep,
                                       purchase_time=updateAsset.purchase_time,
                                       comment=updateAsset.comment,
                                       modify_time=datetime.now())
            new_history.save()
            new_log = UserOperateLog(username=request.user.username,
                                     type='修改资产',
                                     content=request.POST.get('asset_name'),
                                     asset_id=asset_id)
            new_log.save()
            return HttpResponseRedirect((reverse('asset:asset_item_info',
                                                 args=[asset_id])))
        else:
            return HttpResponseRedirect((reverse('asset:asset_detail',
                                                 args=[asset_id])))


class AssetDeleteView(LoginRequiredMixin, View):
    """删除"""
    def get(self, request, asset_id):
        delAsset = Asset.objects.get(asset_id=asset_id)
        new_log = UserOperateLog(username=request.user.username,
                                 type='删除资产',
                                 content=delAsset.asset_name,
                                 asset_id=asset_id)
        new_log.save()
        Asset.objects.get(asset_id=asset_id).delete()
        return HttpResponseRedirect((reverse('asset:asset_edit')))


class AssetExportView(LoginRequiredMixin, View):
    """导出"""
    def get(self, request):
        search = request.GET.get('search')
        if search:
            search = request.GET.get('search').strip()
            servers = Asset.objects.filter(Q(zctype__zctype__icontains=search) | Q(ipaddress__icontains=search)
                                           | Q(description__icontains=search) | Q(brand__icontains=search)
                                           | Q(zcmodel__icontains=search) | Q(zcnumber__icontains=search)
                                           | Q(zcpz__icontains=search) | Q(owner__username__icontains=search)). \
                order_by('zctype')
        else:
            assets = Asset.objects.all().order_by('asset_type')
        # assets = assets.values('id', 'zctype__zctype', 'ipaddress', 'description', 'brand', 'zcmodel', 'zcnumber',
        #                        'zcpz', 'owner__username', 'undernet', 'guartime', 'comment')
        # colnames = ['名称', '型号', '参数', '购买时间', '使用年限', '备注',
        #             '持有人', '类型', '状态', '部门']
        # response = create_excel(colnames, assets, 'assetadmin')
        # return response


def create_excel(columns, content, file_name):
    """创建导出csv的函数"""
    file_name = file_name + '.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + file_name
    response.charset = 'gbk'
    writer = csv.writer(response)
    writer.writerow(columns)
    for i in content:
        writer.writerow([
            i['asset_name'], i['asset_model'], i['specification'],
            i['purchase_time'], i['used_time'], i['comment'],
            i['asset_holder'], i['asset_type'], i['asset_status'],
            i['asset_dep']
        ])
    return response


class TypeListView(LoginRequiredMixin, View):
    """类别列表"""
    def get(self, request):
        assets_types = AssetType.objects.all()
        return render(request, 'asset/type_list.html',
                      {'assets_types': assets_types})


class TypeAddView(LoginRequiredMixin, View):
    """类别添加"""
    def get(self, request):
        fa_category = AssetType.objects.filter(category_type=1)
        return render(request, 'asset/type_add.html',
                      {'fa_category': fa_category})

    def post(self, request):
        type_name = request.POST.get('type_name')
        category_type = request.POST.get('category_type')
        fa_category = request.POST.get('fa_category')
        if type_name:
            if AssetType.objects.filter(asset_type=type_name):
                return render(request, 'asset/type_add.html',
                              {'msg': type_name + ' 已存在！'})
            else:
                if fa_category:
                    AssetType.objects.update_or_create(
                        asset_type=type_name,
                        category_type=category_type,
                        parent_category=AssetType.objects.get(id=fa_category))
                    new_log = UserOperateLog(username=request.user.username,
                                             type='增加类别',
                                             content=category_type + '-' +
                                             type_name)
                    new_log.save()
                else:
                    AssetType.objects.update_or_create(
                        asset_type=type_name,
                        category_type=category_type,
                    )
                    new_log = UserOperateLog(username=request.user.username,
                                             type='增加类别',
                                             content=category_type + '-' +
                                             type_name)
                    new_log.save()
                return HttpResponseRedirect((reverse('asset:type_list')))
        else:
            return render(request, 'asset/type_add.html', {'msg': '输入错误！'})


class TypeDetailView(LoginRequiredMixin, View):
    """类别详情"""
    def get(self, request, type_id):
        asset_type = AssetType.objects.get(id=type_id)
        return render(request, 'asset/type_detail.html',
                      {'asset_type': asset_type})


class TypeModifyView(LoginRequiredMixin, View):
    """类别修改"""
    def post(self, request):
        type_id = request.POST.get('type_id')
        type_name = request.POST.get('type_name')
        if type_name:
            # 是否重名
            if AssetType.objects.filter(asset_type=type_name):
                return render(request, 'asset/type_detail.html',
                              {'msg': '类别已存在'})
            else:
                modifyType = AssetType.objects.get(id=type_id)
                modifyType.asset_type = type_name
                modifyType.save()
                new_log = UserOperateLog(username=request.user.username,
                                         type='修改类别',
                                         content=type_name)
                new_log.save()
                return HttpResponseRedirect((reverse('asset:type_list')))
        else:
            return render(request, 'asset/type_detail.html', {
                'error_msg': '输入错误！',
            })


class TypeDeleteView(LoginRequiredMixin, View):
    """类别删除"""
    def get(self, request, type_id):
        delType = AssetType.objects.get(id=type_id)
        new_log = UserOperateLog(username=request.user.username,
                                 type='删除类别',
                                 content=delType.asset_type)
        AssetType.objects.get(id=type_id).delete()
        new_log.save()
        return HttpResponseRedirect((reverse('asset:type_list')))


class TypeListView(LoginRequiredMixin, View):
    """类别列表"""
    def get(self, request):
        assets_types = AssetType.objects.all()
        return render(request, 'asset/type_list.html',
                      {'assets_types': assets_types})
