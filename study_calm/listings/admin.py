from django.contrib import admin
from listings.models.productdetail import ProductDetail
from listings.models.seat import Seat
from listings.models.room import Room
from listings.models.listing import Listing


# Register your models here.
class ListingAdmin(admin.ModelAdmin):

    search_fields = ['rent_room_available']
    readonly_fields = ('rent_room_total', 'rent_room_available','rent_seat_total','rent_seat_available')

class RoomAdmin(admin.ModelAdmin):
    pass

class SeatAdmin(admin.ModelAdmin):
    pass

class ProductDetailAdmin(admin.ModelAdmin):
    pass

admin.site.register(Listing, ListingAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(ProductDetail, ProductDetailAdmin)

