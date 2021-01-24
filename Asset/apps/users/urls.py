from django.urls import path

from apps.users import api
from apps.users.views import SectionAddView, SectionDeleteView, SectionDetailView, SectionModifyView, SectioneListView, UserLoginView, UserLogoutView
from apps.users.views import UserListView, UserAddView, UserDetailView, UserModifyView, UserResetPwd, UserDeleteView
from apps.users.views import UserPwdModifyView, UserOperateView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),

    # 定义用户的相关url
    path('user/list/', UserListView.as_view(), name='user_list'),
    path('user/add/', UserAddView.as_view(), name='user_add'),
    path('user/detail/<int:user_id>/', UserDetailView.as_view(), name='user_detail'),
    path('user/modify/', UserModifyView.as_view(), name='user_modify'),
    path('user/pwdreset/<int:user_id>', UserResetPwd.as_view(), name='user_pwdreset'),  # 该url为管理员重置用户密码
    path('user/delete/<int:user_id>/', UserDeleteView.as_view(), name='user_delete'),
    path('user/pwdmodify/', UserPwdModifyView.as_view(), name='user_pwd_modify'),  # 该url为用户修改自身密码
    path('user/log/', UserOperateView.as_view(), name='user_log'),  # 用户操作日志


    # 定义用户部门的相关url
    path('dp/list/', SectioneListView.as_view(), name='dp_list'),
    path('dp/add/', SectionAddView.as_view(), name='dp_add'),
    path('dp/detail/<int:id>/', SectionDetailView.as_view(), name='dp_detail'),
    path('dp/modify/<int:id>/', SectionModifyView.as_view(), name='dp_modify'),
    path('dp/delete/<int:id>/', SectionDeleteView.as_view(), name='dp_delete'),


    # 定义用户操作url
    path('user/operate_log/', UserOperateView.as_view(), name='operate_log'),
    # API测试
    path('api/v1/userslist', api.UserListSet.as_view({'get': 'list'}))
]
