from django.contrib import admin
from pardakht.models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('price', 'state', 'user', 'gateway', 'payment_result', 'verification_result','token', 'created_at')
    list_filter = ('gateway', 'state')
    search_fields = ('token', )
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'