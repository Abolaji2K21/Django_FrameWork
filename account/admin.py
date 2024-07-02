from django.contrib import admin

from .models import Account


# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('accountNumber', 'balance', 'account_type')
    list_per_page = 10
    search_fields = ['account_type'],
    list_editable = ['account_type', 'balance']



# admin.site.register(Account)
