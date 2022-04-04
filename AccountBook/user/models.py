from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import jwt
from datetime import datetime, timedelta
from django.conf import settings
# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('email must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email, username='', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is False:
            raise ValueError('superuser must have is_staff = true')
        if extra_fields.get('is_superuser') is False:
            raise ValueError('superuser must have is_superuser = true')
        return self._create_user(email, 'blogs/like_section.html', password, **extra_fields)
class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']
class User(AbstractUser, TimestampedModel):
    email = models.EmailField(verbose_name='email', unique=True)
    username = models.TextField(max_length=20)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def token(self):
        return self._generate_jwt_token()
    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': dt.utcfromtimestamp(dt.timestamp())
        }, settings.SECRET_KEY, algorithm='HS256')
        return token