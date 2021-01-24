from rest_framework import serializers

from apps.users.models import UserProfile, Department


class DepartmentSerializer(serializers.ModelSerializer):
    """外键的序列化"""
    class Meta:
        model = Department
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = UserProfile
        fields = ['username', 'sex', 'email', 'bg_telephone', 'department']

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return UserProfile.objects.create(**validated_data)
