from django.db import models
from accounts.models.supplier import Supplier
from .productdetail import ProductDetail

import uuid

class ListingManager(models.Manager):

    @classmethod
    def deregister(self, email):
        pass

class Listing(models.Model):
    class Meta:
        db_table = 'Listings'
        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'
        # ordering = ['']
    objects = ListingManager()
    '''
    Property Information
    '''
    id = models.AutoField(primary_key=True)
    owner = models.OneToOneField(
        Supplier,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=80, blank=False)
    address = models.CharField(max_length=80, blank=False)
    geo_lat = models.DecimalField(max_digits=20, decimal_places=17, default=37.556097)
    geo_lng = models.DecimalField(max_digits=20, decimal_places=17, default=126.942911)
    '''
    Listing Information
    '''
    LISTING_TYPE = (
        ('kyo', '교습소'),
        ('acd', '학원'),
        ('std', '독서실'),
    )
    listing_type = models.CharField(
        max_length=3,
        choices=LISTING_TYPE,
        default='acd',
        blank=False
    )
    operational_hours_24 = models.BooleanField(default=False, blank=False)
    operational_hours_start = models.CharField(max_length=5, blank=False) # Format '00:00'
    operational_hours_end = models.CharField(max_length=5, blank=False)

    '''
    Rent Room
    '''
    rent_room = models.BooleanField(default=False, blank=False)
    rent_room_total = models.IntegerField(default=0, blank=False)
    rent_room_available = models.IntegerField(default=0)

    '''
    Rent Seat
    '''
    rent_seat = models.BooleanField(default=False, blank=False)
    rent_seat_total = models.IntegerField(default=0, blank=False)
    rent_seat_available = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not all([getattr(self,'operational_hours_start'), getattr(self, 'operational_hours_end')]):
            self.operational_hours_24 = False
        super(Listing, self).save(*args, **kwargs)