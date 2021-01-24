from rest_framework import status, generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import UserProfile
from apps.users.serializers import UserProfileSerializer


# class UserList(APIView):
#     """
#     List all users, or create a new users.
#     """
#
#     def get(self, request, format=None):
#         users = UserProfile.objects.all()
#         serializer = UserProfileSerializer(users, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = UserProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserListPagination(PageNumberPagination):
#     page_size = 1000
#     page_size_query_param = 'page_size'
#     max_page_size = 10000


# class UserList(generics.ListAPIView):
#     """用户通用视图列表"""
#     queryset = UserProfile.objects.all()
#     serializer_class = UserProfileSerializer


class UserListSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """通用视图用户列表"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
