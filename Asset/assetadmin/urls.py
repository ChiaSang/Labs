from django.contrib import admin
from rest_framework.routers import DefaultRouter

from apps.asset.views import IndexView

from django.urls import path, include

from apps.users.api import UserListSet

router = DefaultRouter()
router.register(r'users', UserListSet)
urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('cs/', include(router.urls)),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('asset/', include(('asset.urls', 'asset'), namespace='asset')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
