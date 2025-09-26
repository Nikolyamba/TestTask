from django.contrib import admin

from payments.models import PaymentInfo, Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "country")

@admin.register(PaymentInfo)
class PaymentInfoAdmin(admin.ModelAdmin):
    list_display = ("id", "payer_id", "amount", "percent", "pay_date")
