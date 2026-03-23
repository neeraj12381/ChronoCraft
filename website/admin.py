from django.contrib import admin
from .models import Watch, Order, UserActivity

# Watch ke liye simple admin
@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at') # Ab error nahi aayega

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'product_name', 'order_date')

@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')

from .models import ContactMessage
admin.site.register(ContactMessage)