from django.contrib import admin

from .models import Account


# Register your models here.

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'accountNumber', 'balance')
    list_per_page = 10
    search_fields = ['accountNumber', 'firstName', 'lastName']
    # list_editable = ['lastName', 'accountNumber', 'balance', 'account_type']


# admin.site.register(Account)
