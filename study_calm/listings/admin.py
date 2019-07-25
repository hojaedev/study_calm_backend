from django.contrib import admin
from listings.models import ProductDetail
from listings.models.seat import Seat
from listings.models import Room
from listings.models import Listing


# Register your models here.
class ListingAdmin(admin.ModelAdmin):

    search_fields = ['rent_room_available']
    readonly_fields = (
        'operational_hours_overnight',
        'operational_hours_24',
        'rent_room',
        'rent_seat',

        'rent_room_total',
        'rent_room_available',
        'rent_seat_total',
        'rent_seat_available',
        'id'
    )


class RoomAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
    )
    list_display = ('id', 'in_use', 'in_use_until')

class SeatAdmin(admin.ModelAdmin):
    readonly_fields = (
        'id',
    )
    list_display = ('id', 'in_use', 'in_use_until')


class ProductDetailAdmin(admin.ModelAdmin):
    pass

admin.site.register(Listing, ListingAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(ProductDetail, ProductDetailAdmin)