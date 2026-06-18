"""
User serializers
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    """User registration serializer"""
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2', 'phone']
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Mật khẩu không khớp.'})
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({'username': 'Tên người dùng đã tồn tại.'})
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email': 'Email đã được đăng ký.'})
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    """User profile serializer"""
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'phone',
            'avatar', 'gender', 'date_of_birth', 'address', 'city',
            'state', 'postal_code', 'country', 'is_verified', 'is_seller',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'is_seller']


class UserDetailSerializer(serializers.ModelSerializer):
    """Detailed user serializer"""
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'phone',
            'avatar', 'gender', 'date_of_birth', 'address', 'city',
            'state', 'postal_code', 'country', 'is_verified', 'is_seller',
            'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'is_seller', 'is_verified', 'created_at', 'updated_at']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom token serializer with user info"""
    
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'is_seller': self.user.is_seller,
        }
        return data


class ChangePasswordSerializer(serializers.Serializer):
    """Change password serializer"""
    old_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    new_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    new_password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    def validate(self, data):
        if data['new_password'] != data['new_password2']:
            raise serializers.ValidationError({'new_password': 'Mật khẩu mới không khớp.'})
        return data
