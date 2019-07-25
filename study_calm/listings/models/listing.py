from django.db import models
from django.contrib.auth import get_user_model
from datetime import time

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from listings.models.seat import Seat
from listings.models.room import Room


class ListingManager(models.Manager):
    pass

class Listing(models.Model):
    class Meta:
        db_table = 'Listings'
        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'
        # ordering = ['']

    '''
    Property Information
    '''
    id = models.AutoField(primary_key=True)

    is_active = models.BooleanField(blank=True)

    owner = models.OneToOneField(
        'accounts.User',
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

    operational_hours_24 = models.BooleanField(blank=False)
    operational_hours_overnight = models.BooleanField(null=True, blank=True, default=None)
    operational_hours_start = models.TimeField(null=True, blank=True, default=None)
    operational_hours_end = models.TimeField(null=True, blank=True, default=None)

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

    def manage_time(self):
        # operational hours 24 only if start and end hours are not provided
        if not all([getattr(self, 'operational_hours_start'), getattr(self, 'operational_hours_end')]):
            setattr(self, 'operational_hours_24', True)
            setattr(self, 'operational_hours_overnight', False)
            setattr(self, 'operational_hours_start', None)
            setattr(self, 'operational_hours_end', None)
            print('triggered')
        else:
            setattr(self,'operational_hours_24', False)
            if(time(hour=0, minute=0, second=0) < getattr(self, 'operational_hours_end')) and (getattr(self, 'operational_hours_end') < getattr(self, 'operational_hours_start')):
                setattr(self, 'operational_hours_overnight', True)


    # later this method will be sent to on create in seat and room
    def service_type(self):
        setattr(self, 'rent_room', bool(getattr(self, 'rent_room_total')))
        setattr(self, 'rent_seat', bool(getattr(self, 'rent_seat_total')))

    def save(self,*args, **kwargs):
        self.manage_time()
        self.service_type()
        return super().save(*args, **kwargs)




@receiver(post_save, sender='listings.Seat')
def control_seat_save(sender, **kwargs):
    print(kwargs)
    if kwargs['created']:
        # new item created (add to total and add to available as no one is using it)
        kwargs['instance'].listing.rent_seat_total += 1
        if not kwargs['instance'].in_use:
            kwargs['instance'].listing.rent_seat_available += 1
        kwargs['instance'].listing.save(update_fields=['rent_seat_total', 'rent_seat_available'])
    else:
        if kwargs['update_fields']:
            if kwargs['instance'].in_use:
                # when room is used
                kwargs['instance'].listing.rent_seat_available -= 1
                kwargs['instance'].listing.save(update_fields=['rent_seat_available'])
            else:
                # when seat is returned
                kwargs['instance'].listing.rent_seat_available += 1
                kwargs['instance'].listing.save(update_fields=['rent_seat_available'])

@receiver(post_delete, sender='listings.Seat')
def control_seat_delete(sender, **kwargs):
    print(kwargs)
    kwargs['instance'].listing.rent_seat_total -= 1
    kwargs['instance'].listing.rent_seat_available -= 1
    kwargs['instance'].listing.save(update_fields=['rent_seat_total', 'rent_seat_available'])


@receiver(post_save, sender='listings.Room')
def control_seat_save(sender, **kwargs):
    if kwargs['created']:
        # new item created (add to total and add to available as no one is using it)
        kwargs['instance'].listing.rent_room_total += 1
        if not kwargs['instance'].in_use:
            kwargs['instance'].listing.rent_room_available += 1
        kwargs['instance'].listing.save(update_fields=['rent_room_total', 'rent_room_available'])
    else:
        if kwargs['update_fields']:
            if kwargs['instance'].in_use:
                # when room is used
                kwargs['instance'].listing.rent_room_available -= 1
                kwargs['instance'].listing.save(update_fields=['rent_room_available'])
            else:
                # when seat is returned
                kwargs['instance'].listing.rent_room_available += 1
                kwargs['instance'].listing.save(update_fields=['rent_room_available'])

@receiver(post_delete, sender='listings.Room')
def control_seat_delete(sender, **kwargs):
    kwargs['instance'].listing.rent_room_total -= 1
    kwargs['instance'].listing.rent_room_available -= 1
    kwargs['instance'].listing.save(update_fields=['rent_room_total', 'rent_room_available'])