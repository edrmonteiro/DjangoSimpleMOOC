import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'UserName', max_length=30, unique=True, 
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
            'The name can contain only letters and numbers, or the characters @/./+/-/_', 'invalid')]
    )
    email = models.EmailField('Email', unique=True)
    name = models.CharField('Name', max_length=100, blank=True)
    is_active = models.BooleanField('Is active?', blank=True, default=True)
    is_staff = models.BooleanField('Is from group?', blank=True, default=False)
    date_joined = models.DateTimeField('Admittanceate', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'