from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    EmailValidator
)
from datetime import datetime
from accounts.models import User


class CustomerAccountManager(models.Manager):
    pass
#     @classmethod
#     def normalize_email(cls, email):
#         """
#         Normalize the email address by lowercasing the domain part of it.
#         """
#         email = email or ''
#         try:
#             email_name, domain_part = email.strip().rsplit('@', 1)
#         except ValueError:
#             pass
#         else:
#             email = email_name + '@' + domain_part.lower()
#         return email
#
#     def create_user(self, email, password, act_type, **kwargs):
#
#         if all(email, password, act_type):
#             user = self.model(email=self.normalize_email(email), password=password, act_type=act_type, **kwargs)
#         user = self.model(email=self.normalize_email(email), **kwargs)
#         user.set_password(password)
#         user.save(using=self._db)


class Customer(models.Model):
    class Meta:
        db_table = 'Customers'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    objects = CustomerAccountManager()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


    '''
    Basic User Information
    '''
    name = models.CharField(max_length=20, verbose_name='Name', blank=False, default='N/A')
    phone_number = models.CharField(max_length=13, verbose_name='Phone Number')
    # img = models.ImageField(upload_to=None, height_field=100, width_field=100, max_length=100, blank=True)

    '''
    Registration and Login Information
    '''
    registered_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_login_ip = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, blank=True, null=True)

    '''
    Payment Information
    Default - None
    '''
    credit_card_no = models.CharField(max_length=50, blank=True, null=True)
    val_thr_month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)], blank=True, null=True)
    val_thr_year = models.IntegerField(validators=[MinValueValidator(int(datetime.now().strftime('%Y')))], blank=True,
                                       null=True)

    '''
    Activity Information

    '''
    # recent_visit

    '''
    Meta Information
    '''

    # loc_type
    # loc_coord_x
    # loc_coord_y
    # loc_addr

    def __str__(self):
        return self.name