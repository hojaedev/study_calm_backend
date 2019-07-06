from django.db import models
from .listing import Listing
from .productdetail import ProductDetail
from accounts.models.user import User
import uuid

class Seat(models.Model):

    class Meta:
        db_table = 'Seats'
        verbose_name = 'Seat'
        verbose_name_plural = 'Seats'

    '''
    SEAT PROPERTY
    '''
    # Unique SEAT ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    used_by = models.OneToOneField(User, null=True, on_delete=models.CASCADE, primary_key=False)

    # th seat
    nth_seat = models.IntegerField()
    # extendable
    extendable = models.BooleanField(default=True, blank=False)
    details = models.ManyToManyField(ProductDetail)

    # A seat is registered under the listing
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    # Seats will always be in default to prevent overbooking
    in_use = models.BooleanField(default=True, blank=False)
    in_use_until = models.DateTimeField(auto_now=False, auto_now_add=False)