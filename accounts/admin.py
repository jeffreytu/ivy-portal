from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Product)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'date_created']
admin.site.register(Order, OrderAdmin)



admin.site.register(Tag)