from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomerAccountManager(models.Manager):
    pass


class Customer(models.Model):

    class Meta:
        db_table = 'Customers'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    objects = CustomerAccountManager()

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    '''
    Basic User Information
    '''
    name = models.CharField(max_length=20, verbose_name='Name', blank=True, null=True, default=None)
    phone_number = models.CharField(max_length=13, verbose_name='Phone Number', blank=True, null=True, default=None)
    # img = models.ImageField(upload_to=None, height_field=100, width_field=100, max_length=100, blank=True)

    def payment_verified(self):
        return all([getattr(self, 'credit_card_no'), getattr(self, 'val_thr_month'), getattr(self, 'val_thr_year')])

    def __str__(self):
        return self.user.email

@receiver(post_save, sender='accounts.User')
def create_profile(sender, **kwargs):
    if kwargs['created'] and kwargs['instance'].user_role == 2:
        user_profile = Customer.objects.create(user=kwargs['instance'])