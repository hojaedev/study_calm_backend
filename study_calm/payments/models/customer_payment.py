from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import uuid

class CreditCardManager(models.Manager):
    pass

class CreditCard(models.Model):

    class Meta:
        db_table = 'CreditCard'
        verbose_name = 'CreditCard'
        verbose_name_plural = 'CreditCards'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True, default=None)
    credit_card_no = models.CharField(max_length=19, blank=False)
    month = models.CharField(max_length=2, blank=False)
    year = models.CharField(max_length=2, blank=False)
    card_holder_name = models.CharField(max_length=30, blank=False)
    password = models.CharField(max_length=2, blank=False)

    def save(self,*args, **kwargs):
        return super(CreditCard, self).save(*args, **kwargs)

    def __str__(self):
        return str(id)

    '''
        save a signal to user whether the signal is triggered or not
    '''