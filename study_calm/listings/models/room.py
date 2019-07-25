from django.db import models
import uuid
from datetime import datetime, timedelta

class Room(models.Model):

    class Meta:
        db_table = 'Rooms'
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'
    '''
    ROOM PROPERTY
    '''
    # Unique ROOM ID
    id = models.AutoField(primary_key=True)
    listing = models.ForeignKey('listings.Listing', on_delete=models.CASCADE)

    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, primary_key=False, blank=True, null=True)    # ith_room

    nth_room = models.IntegerField()
    extendable = models.BooleanField(default=True, blank=False)
    details = models.ManyToManyField('listings.ProductDetail', blank=True)

    max_pax = models.IntegerField()
    min_pax = models.IntegerField()

    # Room will always be in default to prevent overbooking
    in_use = models.BooleanField(default=True, blank=False)
    in_use_until = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

    # Identify if model was created
    created = models.DateTimeField(auto_now_add=True)

    def ret(self, user):
        try:
            if self.is_user(user):
                setattr(self, 'in_use', False)
                setattr(self, 'user', None)
                setattr(self, 'in_use_until', None)
                setattr(self, 'in_use', False)
                self.save()
                return True
        except Exception as e:
            print(e)
        return False

    def use(self, user, time):
        if not self.in_use:
           update_time = self.is_time_available(time)
           if update_time:
               setattr(self, 'in_use', False)
               setattr(self, 'user', user)
               setattr(self, 'in_use_until', update_time)
               self.save()
               return True
        return False

    def is_time_available(self, time):
        update_time = None
        if self.in_use:
            update_time = getattr(self, 'in_use_until') + timedelta(minutes=time)
        else:
            update_time = datetime.now() + timedelta(minutes=time)
        if update_time.time() <= self.listing.operational_hours_end:
            return update_time
        return None

    def get_qr(self):
        return self.nth_room

    def is_user(self, user):
        if self.user == user:
            return True
        else:
            return False

    def __str__(self):
        return str(self.id)


    def __init__(self, *args, **kwargs):
        super(Room, self).__init__(*args, **kwargs)
        self.__prev_in_use = getattr(self, 'in_use')

    def save(self, *args, **kwargs):
        update_fields = None
        setattr(self, 'in_use', bool(getattr(self, 'user')))
        if self.in_use != self.__prev_in_use and self.created:
            update_fields = ['listing', 'user', 'nth_room', 'extendable', 'in_use', 'in_use_until']
        self.__prev_in_use = self.in_use
        return super(Room, self).save(update_fields=update_fields, *args, **kwargs)

    def delete(self, *args, **kwargs):
        if not getattr(self, 'in_use'):
            return super(Room, self).delete(*args, **kwargs)
        return None