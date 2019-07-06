from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import uuid


class UserAccountManager(BaseUserManager):

    '''
    For Customer Database
    '''

    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email Field is Required')
        if not password:
            raise ValueError('Password Field is Required')
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **kwargs):
        self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('user_role', 1)
        kwargs.setdefault('acc_type', 'nat')
        self._create_user(email, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):

    '''
    Customer Model
    '''
    class Meta:
        db_table = 'Users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined',]

    # Designated User Manager for Model
    objects = UserAccountManager()

    # User Model Settings
    USERNAME_FIELD = 'email'

    ACCOUNT_TYPE = (
        (1, 'Google'),
        (2, 'Facebook'),
        (3, 'Native'),
    )
    ROLE_CHOICES = (
        (1, 'ADMIN'),
        (2, 'CUSTOMER'),
        (3, 'SUPPLIER'),
        (4, 'to_be_added_1'),
        (5, 'to_be_added_2'),
        (6, 'to_be_added_3'),
        (7, 'to_be_added_4'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

    user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    acc_type = models.PositiveSmallIntegerField(choices=ACCOUNT_TYPE, default=3, blank=False)

    email = models.EmailField(unique=True, verbose_name='Email')

    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Date of Registration')

    registered_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_login_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, blank=True, null=True)

    is_active = models.BooleanField(default=False, verbose_name='Active Activity Status')
    is_staff = models.BooleanField(default=False, verbose_name='Staff Status')


    def __str__(self):
        return self.email

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All superusers are staff
    #     return self.is_superuser