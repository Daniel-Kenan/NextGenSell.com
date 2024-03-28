from django.contrib import admin
from .models import BusinessInfo, BusinessType, Client, Device, Payment, Doc

@admin.register(BusinessInfo)
class BusinessInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'website')

@admin.register(BusinessType)
class BusinessTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('business_info', 'business_type', 'industry', 'status')
    list_filter = ('business_type', 'status')

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('device_name', 'client', 'installation_date')
    list_filter = ('client',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('client', 'amount', 'payment_date', 'subscription_start_date', 'subscription_end_date')
    list_filter = ('client',)

@admin.register(Doc)
class DocAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

