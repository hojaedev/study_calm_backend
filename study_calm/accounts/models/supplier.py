from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

class SupplierAccountManager(models.Manager):
    pass

class Supplier(models.Model):

    class Meta:
        db_table = 'Suppliers'
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    '''
    Basic User Information
    '''
    name = models.CharField(max_length=20, verbose_name='Name', blank=True, null=True, default=None)
    phone_number = models.CharField(max_length=13, verbose_name='Phone Number', blank=True, null=True, default=None)

    '''
    Bank Account Information
    Default - None
    '''

    bank_name = models.CharField(max_length=50, blank=True, null=True, default=None)
    account_number = models.CharField(max_length=50, blank=True, null=True, default=None)
    account_holder_name = models.CharField(max_length=50, blank=True, null=True, default=None)

    '''
    Other Details
    '''
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True, default=None)

    def payment_verified(self):
        return all([getattr(self, 'bank_name'), getattr(self, 'account_number'), getattr(self, 'account_holder_name')])

    def __str__(self):
        return self.user.email

@receiver(post_save, sender='accounts.User')
def create_profile(sender, **kwargs):
    if kwargs['created'] and kwargs['instance'].user_role == 3:
        user_profile = Supplier.objects.create(user=kwargs['instance'])