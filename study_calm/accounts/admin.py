from django.contrib import admin
from accounts.models.user import User
from accounts.models import Customer
from accounts.models import Supplier

'''
Company Admin Authentication

'''

# def credit_card_registration_status(obj):
#     return all([obj.credit_card_no, obj.val_thr_month, obj.val_thr_year])
#
# def bank_account_registration_status(obj):
#     return all([obj.bank_name, obj.account_number, obj.account_holder_name])
#
# credit_card_registration_status.boolean = True
# credit_card_registration_status.short_description = 'Card Reg. Status'
# bank_account_registration_status.boolean = True
# bank_account_registration_status.short_description = 'Bank Acc Reg. Status'

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email', ]
    list_display = ('email', 'is_active')
    readonly_fields = (
        'date_joined',
        'last_login',
        'last_login_ip',
        'valid_payment',
    )

    fieldsets = (
        ('General', {
            'fields': ('email', 'username', 'password'),
        }),
        ('Account Category', {
            'fields': ('user_role',),
        }),
        ('Advanced', {
            'fields': ('date_joined', 'last_login', 'last_login_ip','valid_payment',)
        })
    )


class SupplierAdmin(admin.ModelAdmin):
    search_fields = ['email']
    list_display = ('get_email', 'phone_number')

    readonly_fields = ('id',)

    def get_email(self, obj):
        return obj.user.email

class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['email']
    list_display = ('get_email', 'phone_number')

    readonly_fields = ('id',)

    def get_email(self, obj):
        return obj.user.email

admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Supplier, SupplierAdmin)