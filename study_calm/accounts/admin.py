from django.contrib import admin
from accounts.models.user import User
from accounts.models.customer import Customer
from accounts.models.supplier import Supplier

'''
Company Admin Authentication

'''

def credit_card_registration_status(obj):
    return all([obj.credit_card_no, obj.val_thr_month, obj.val_thr_year])

credit_card_registration_status.boolean = True
credit_card_registration_status.short_description = 'Card Reg. Status'

class UserAdmin(admin.ModelAdmin):
    pass

class SupplierAdmin(admin.ModelAdmin):
    pass

class CustomerAdmin(admin.ModelAdmin):

    search_fields = ['name',]
    list_display = ('name', 'phone_number', credit_card_registration_status,)

    # fieldsets = (
    #     ('Detail', {
    #         'fields': ('phone_number'),
    #     }),
    #     ('Payment', {
    #         'fields': ('credit_card_no', 'val_thr_month', 'val_thr_year'),
    #     }),
    #     ('Advanced', {
    #         'classes': ('collapse',),
    #         'fields': ('registered_at', 'last_login', 'last_login_ip'),
    #     }),
    # )

    # readonly_fields = ('registered_at', 'last_login')

admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Supplier, SupplierAdmin)