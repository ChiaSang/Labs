from django.contrib import messages
from django.shortcuts import render, redirect, render_to_response
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
import django_excel as excel
from pure_pagination import Paginator, PageNotAnInteger

from .models import UserProfile, UserOperateLog, Department
from .forms import LoginForm, UserPwdModifyForm, UserInfoForm
from assetadmin.settings import per_page
from apps.utils.mixin_utils import LoginRequiredMixin

# 定义普通用户初始密码
pwd = '12345678'


class UserLoginView(View):
    """用户登录视图"""

    def get(self, request):
        return render(request, 'users/login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'users/login.html', {'error_msg': '用户不存在'})
        else:
            return render(request, 'users/login.html', {'error_msg': '账号或密码错误'})
            # return render(request, 'users/login.html', {'msg': '账号或密码错误', 'login_form': login_form})


# 用户退出
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        response = redirect(reverse('users:user_login'))
        response.delete_cookie('username')
        return response


# 用户修改密码
class UserPwdModifyView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/user_pwd_modify.html')

    def post(self, request):
        user_pwd_modify_form = UserPwdModifyForm(request.POST)
        if user_pwd_modify_form.is_valid():
            user = UserProfile.objects.get(username=request.user.username)
            pwd1 = request.POST.get('pwd1').strip()
            pwd2 = request.POST.get('pwd2').strip()
            if pwd1 == pwd2:
                user.password = make_password(pwd1)
                user.save()
                return HttpResponseRedirect((reverse('users:user_login')))
            else:
                return render(request, 'users/user_pwd_modify.html', {'msg': '两次密码不一致！'})
        else:
            return render(request, 'users/user_pwd_modify.html', {'msg': '密码不能为空！',
                                                                  'user_pwd_modify_form': user_pwd_modify_form})


# 管理员对用户的操作相关视图(管理员可见)
# 用户列表
class UserListView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get('search')
        if search:
            search = request.GET.get('search').strip()
            users = UserProfile.objects.filter(Q(username__icontains=search)
                                               | Q(department__dp_name__icontains=search)
                                               | Q(bg_telephone__icontains=search),
                                               is_superuser=0).order_by('-is_superuser', 'id')  # 排除超级管理员
        else:
            users = UserProfile.objects.filter(is_superuser=0).order_by('-is_superuser', 'id')  # 排除超级管理员

        # 分页功能实现
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(users, per_page=per_page, request=request)
        p_users = p.page(page)
        start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始
        return render(request, 'users/user_list.html', {'p_users': p_users, 'start': start, 'search': search})


# 用户添加
class UserAddView(LoginRequiredMixin, View):
    def get(self, request):
        sections = Department.objects.all()
        return render(request, 'users/user_add.html', {'sections': sections})

    def post(self, request):
        userinfo_form = UserInfoForm(request.POST)
        if userinfo_form.is_valid():
            username = request.POST.get('username').strip()
            # department = Department.objects.get(id=request.POST.get('user_dep')),
            # bg_telephone = request.POST.get('bg_telephone').strip()
            # email = request.POST.get('email').strip()
            # isadmin = request.POST.get('isadmin')
            if UserProfile.objects.filter(username=username):
                return render(request, 'users/user_add.html', {'msg': '用户 ' + username + ' 已存在！'})
            else:
                UserProfile.objects.create(username=request.POST.get('username').strip(), password=make_password(pwd),
                                           department=Department.objects.get(id=request.POST.get('user_dep')),
                                           isadmin=request.POST.get('isadmin'))
                return HttpResponseRedirect((reverse('users:user_list')))
        else:
            return render(request, 'users/user_add.html', {'msg': '输入错误！', 'userinfo_form': userinfo_form})


# 用户详情
class UserDetailView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = UserProfile.objects.get(id=user_id)
        section = Department.objects.all()
        return render(request, 'users/user_detail.html', {'user': user, 'sections': section})


# 用户修改
class UserModifyView(LoginRequiredMixin, View):
    def post(self, request):
        userinfo_form = UserInfoForm(request.POST)
        user_id = int(request.POST.get('user_id'))
        user = UserProfile.objects.get(id=user_id)
        sections = Department.objects.all()
        if userinfo_form.is_valid():
            # username = request.POST.get('username').strip()
            # other_user = UserProfile.objects.filter(~Q(id=request.POST.get('user_id')), username=username)
            # # 如果修改了用户名，判断是否该用户名与其他用户冲突
            # if other_user:
            #     return render(request, 'users/user_detail.html', {'msg': username + '用户名已存在！'})
            # else:
            if user.is_superuser:
                print(user.isadmin)
                user.username = request.POST.get('username').strip() #  姓名不可修改
                user.department_id = Department.objects.filter(id=request.POST.get('user_dep', 0)).first()
                user.bg_telephone = request.POST.get('bg_telephone').strip()
                # user.email = request.POST.get('email').strip()
                user.isadmin = request.POST.get('isadmin')
                user.save()
                return render(request, 'users/user_detail.html', {'user': user, 'sections': sections, 'msg': '修改成功！',
                                                              'userinfo_form': userinfo_form})

            else:
                user.bg_telephone = request.POST.get('bg_telephone').strip()
                # user.email = request.POST.get('email').strip()
                user.isadmin = request.POST.get('isadmin')
                user.save()
                return render(request, 'users/user_detail.html', {'user': user, 'sections': sections, 'msg': '修改成功！',
                                                                  'userinfo_form': userinfo_form})
        else:
            return render(request, 'users/user_detail.html', {'user': user, 'sections': sections, 'msg': '输入错误！',
                                                              'userinfo_form': userinfo_form})


# 重置用户密码
class UserResetPwd(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = UserProfile.objects.get(id=user_id)
        user.password = make_password(pwd)
        user.save()
        return HttpResponseRedirect((reverse('users:user_list')))


# 用户删除
class UserDeleteView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = UserProfile.objects.get(id=user_id)
        user.delete()
        return HttpResponseRedirect((reverse('users:user_list')))


# 操作日志视图
class UserOperateView(LoginRequiredMixin, View):
    def get(self, request):
        search = request.GET.get('search')
        if search:
            search = search.strip().upper()
            operate_logs = UserOperateLog.objects.filter(Q(username__icontains=search) | Q(scope__icontains=search)
                                                         | Q(type__icontains=search)).order_by('-modify_time')
        else:
            operate_logs = UserOperateLog.objects.all().order_by('-modify_time')

        # 分页功能实现
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(operate_logs, per_page=per_page, request=request)
        p_operate_logs = p.page(page)
        start = (int(page) - 1) * per_page  # 避免分页后每行数据序号从1开始

        return render(request, 'users/operate_log.html', {'operate_logs': p_operate_logs, 'start': start,
                                                          'search': search})


class SectionAddView(LoginRequiredMixin, View):
    """部门添加"""

    def get(self, request): 
        return render(request, 'users/user_section_add.html')

    def post(self, request):
        dp_name = request.POST.get('dp_name')
        if dp_name:
            if Department.objects.filter(dp_name=dp_name):
                return render(request, 'users/user_section_detail.html', {'msg': dp_name + ' 已存在！'})
            else:
                Department.objects.create(dp_name=dp_name)
                new_log = UserOperateLog(username=request.user.username, type='添加部门',
                                        content=dp_name)
                new_log.save()
                return HttpResponseRedirect((reverse('users:dp_list')))
        else:
            return render(request, 'users/user_section_detail.html', {'msg': '输入错误！'})


class SectionDetailView(LoginRequiredMixin, View):
    """部门详情"""

    def get(self, request, id):
        dp = Department.objects.get(id=id)
        return render(request, 'users/user_section_detail.html', {'dp': dp})


class SectionModifyView(LoginRequiredMixin, View):
    """部门修改"""

    def post(self, request, id):
        dp_id = request.POST.get('dp_id')
        dp_name = request.POST.get('dp_name').strip()
        if dp_name:
            # 是否重名
            if Department.objects.filter(dp_name=dp_name):
                return render(request, 'users/section_detail.html', {'msg': '部门已存在'})
            else:
                modifySection = Department.objects.get(id=dp_id)
                modifySection.dp_name = dp_name
                modifySection.save()
                new_log = UserOperateLog(username=request.user.username, type='修改部门',
                                        content=dp_name)
                new_log.save()
                return HttpResponseRedirect((reverse('users:dp_list')))
        else:
            return render(request, 'users/dp_detail.html', {'error_msg': '输入错误！', })


class SectionDeleteView(LoginRequiredMixin, View):
    """部门删除"""

    def get(self, request, id):
        delDp = Department.objects.get(id=id)
        new_log = UserOperateLog(username=request.user.username, type='修改类别',
                                content=delDp.dp_name)
        Department.objects.get(id=id).delete()
        new_log.save()
        return HttpResponseRedirect((reverse('users:dp_list')))


class SectioneListView(LoginRequiredMixin, View):
    """部门列表"""

    def get(self, request):
        section_lists = Department.objects.all()
        return render(request, 'users/user_section_list.html', {'section_lists': section_lists})



# 定义全局404
def page_not_found(request):
    response = render_to_response('templates/404.html')
    response.status_code = 404
    return response


# 定义全局500
def page_error(request):
    response = render_to_response('500.html')
    response.status_code = 500
    return response
