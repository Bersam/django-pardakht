from django.contrib import admin
from pardakht.models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('ref_number', 'price', 'state', 'user', 'gateway', 'payment_result', 'verification_result','token', 'created_at')
    # add user to list_filter and search_fields
    list_filter = ('gateway', 'state',)
    search_fields = ('token', 'ref_number')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'