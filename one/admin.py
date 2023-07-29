from django.contrib import admin
from one import models
# Register your models here.
class itemdetAdmin(admin.ModelAdmin):
    list_display=['itname','itno','itprice','itqty']
admin.site.register(models.itemdet,itemdetAdmin)
