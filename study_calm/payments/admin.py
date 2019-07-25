from django.contrib import admin
from payments.models import CreditCard, BankAccount

# Register your models here.
class CreditCardAdmin(admin.ModelAdmin):
    pass
    # search_fields = ['rent_room_available']
    # readonly_fields = (
    #     'operational_hours_overnight',
    #     'operational_hours_24',
    #     'rent_room',
    #     'rent_seat',
    #
    #     'rent_room_total',
    #     'rent_room_available',
    #     'rent_seat_total',
    #     'rent_seat_available',
    #     'id'
    # )

class BankAccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(CreditCard, CreditCardAdmin)
admin.site.register(BankAccount, BankAccountAdmin)