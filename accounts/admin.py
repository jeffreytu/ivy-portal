from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'date_created']
admin.site.register(Order, OrderAdmin)