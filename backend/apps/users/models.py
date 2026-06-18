"""
Custom User Model for ecommerce
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    """
    Custom user model with additional fields
    """
    GENDER_CHOICES = [
        ('M', 'Nam'),
        ('F', 'Nữ'),
        ('O', 'Khác'),
    ]
    
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message='Số điện thoại phải có từ 9 đến 15 chữ số.'
    )
    
    phone = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True,
        null=True,
        verbose_name='Số điện thoại'
    )
    
    avatar = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True,
        verbose_name='Ảnh đại diện'
    )
    
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
        verbose_name='Giới tính'
    )
    
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='Ngày sinh'
    )
    
    address = models.TextField(
        blank=True,
        null=True,
        verbose_name='Địa chỉ'
    )
    
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Thành phố'
    )
    
    state = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Tỉnh/Thành phố'
    )
    
    postal_code = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Mã bưu điện'
    )
    
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default='Vietnam',
        verbose_name='Quốc gia'
    )
    
    is_verified = models.BooleanField(
        default=False,
        verbose_name='Đã xác minh'
    )
    
    is_seller = models.BooleanField(
        default=False,
        verbose_name='Là người bán'
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Ngày tạo'
    )
    
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Ngày cập nhật'
    )
    
    class Meta:
        verbose_name = 'Người dùng'
        verbose_name_plural = 'Người dùng'
        ordering = ['-date_joined']
    
    def __str__(self):
        return f"{self.username} ({self.get_full_name()})"
    
    def get_full_address(self):
        """Get full address"""
        parts = [
            self.address,
            self.city,
            self.state,
            self.postal_code,
            self.country
        ]
        return ', '.join([p for p in parts if p])
