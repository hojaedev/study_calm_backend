from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
import uuid
from payments.models import CreditCard

class UserAccountManager(BaseUserManager):
    '''
    For Customer Database
    '''

    def create_user(self, email, username, password='password', user_role=2, **kwargs):
        if not all([email, password, user_role]):
            raise ValueError('[email, password, acc_type, user_role] should be provided')
        user = self.model(email=self.normalize_email(email), username=username, user_role=user_role, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_active', True)
        self.create_user(email, username, password, 1, **kwargs)

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


    # User Model Setting
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    ROLE_CHOICES = (
        (1, 'ADMIN'),
        (2, 'CUSTOMER'),
        (3, 'SUPPLIER'),
        (4, 'to_be_added_1'),
        (5, 'to_be_added_2'),
        (6, 'to_be_added_3'),
        (7, 'to_be_added_4'),
    )

    id = models.AutoField(primary_key=True)
    user_role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    email = models.EmailField(unique=True, verbose_name='Email')
    username = models.CharField(max_length=100, blank=False)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Date of Registration')

    registered_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_login_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, blank=True, null=True)

    is_active = models.BooleanField(default=False, verbose_name='Active Activity Status')
    is_superuser = models.BooleanField(default=False, verbose_name='Superuser Status')
    is_staff = models.BooleanField(default=False, verbose_name='Staff Status')

    # only for customer
    valid_payment = models.BooleanField(default=False, verbose_name='Payment Information Registration Status')

    def activate_user(self):
        setattr(self, 'is_active', True)

    def __str__(self):
        return self.email

@receiver(post_save, sender='payments.CreditCard')
def credit_card_reg(sender, **kwargs):
    if kwargs['created']:
        if not kwargs['instance'].user.valid_payment:
            kwargs['instance'].user.valid_payment = True
            kwargs['instance'].user.save(update_fields=['valid_payment'])

@receiver(post_delete, sender='payments.CreditCard')
def credit_card_dereg(sender, **kwargs):
    if CreditCard.objects.filter(user = kwargs['instance'].user).count() == 0:
        kwargs['instance'].user.valid_payment = False
        kwargs['instance'].user.save(update_fields=['valid_payment'])