from django.db import models

from .user import User

class SupplierAccountManager(models.Manager):
    pass
    # @classmethod
    # def normalize_email(cls, email):
    #     """
    #     Normalize the email address by lower-casing the domain part of it.
    #     """
    #     email = email or ''
    #     try:
    #         email_name, domain_part = email.strip().rsplit('@', 1)
    #     except ValueError:
    #         pass
    #     else:
    #         email = email_name + '@' + domain_part.lower()
    #     return email
    #
    # def create_user(self, email, password, act_type, **kwargs):
    #
    #     if all(email, password, act_type):
    #         user = self.model(email=self.normalize_email(email), password=password, act_type=act_type, **kwargs)
    #     else:
    #         raise ValueError('Enter all required fields')
    #     user.set_password(password)
    #     user.save(using=self._db)

class Supplier(models.Model):

    class Meta:
        db_table = 'Suppliers'
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'


    objects = SupplierAccountManager()

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    '''
    Basic User Information
    '''
    name = models.CharField(max_length=20, verbose_name='Name', blank=False, default='N/A')
    phone_number = models.CharField(max_length=13, verbose_name='Phone Number')


    '''
    Bank Account Information
    Default - None
    '''
    bank_name = models.CharField(max_length=50, default=None, blank=True)
    account_number = models.CharField(max_length=50, default=None, blank=True)
    account_holder_name = models.CharField(max_length=50, default=None, blank=True)

    '''
    Other Details
    '''
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return self.name