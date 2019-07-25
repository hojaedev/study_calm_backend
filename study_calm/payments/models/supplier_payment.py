from django.db import models
import uuid

class BankAccountManager(models.Manager):
    pass

class BankAccount(models.Model):

    class Meta:
        db_table = 'BankAccount'
        verbose_name = 'BankAccount'
        verbose_name_plural = 'BankAccounts'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey('accounts.Supplier', on_delete=models.CASCADE)

    # 예금주
    name = models.CharField(max_length=30, blank=True, null=True, default=None)
    account_no = models.CharField(max_length=30, blank=False)
    bank_name = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return str(id)
