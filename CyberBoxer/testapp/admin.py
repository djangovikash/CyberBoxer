from django.contrib import admin
from testapp.models import Item
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display=['name','quantity','imag']
admin.site.register(Item,ItemAdmin)
 
