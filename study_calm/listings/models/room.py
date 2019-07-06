from django.db import models
from .listing import Listing
from .productdetail import ProductDetail
import uuid
from accounts.models.user import User

class Room(models.Model):
    class Meta:
        db_table = 'Rooms'
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'
    '''
    ROOM PROPERTY
    '''
    # Unique ROOM ID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)

    used_by = models.OneToOneField(User, null=True, on_delete=models.CASCADE, primary_key=False)
    # ith_room
    nth_room = models.IntegerField()
    # max ppl
    max_pax = models.IntegerField()
    # min ppl
    min_pax = models.IntegerField()
    # extendable
    extendable = models.BooleanField(default=True, blank=False)

    # A room is registered under the listing
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    details = models.ManyToManyField(ProductDetail)

    # Room will always be in default to prevent overbooking
    in_use = models.BooleanField(default=True, blank=False)
    in_use_until = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.listing.id) + '#R.'+ str(self.id)