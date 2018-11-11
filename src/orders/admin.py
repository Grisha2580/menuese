from django.contrib import admin

from .models import Item
from .models import Order


class ItemInline( admin.StackedInline ):
	model = Item
	can_delete = False
	verbose_name_plural = 'items'

class OrderAdmin( admin.ModelAdmin ):
	list_display = ['id', 'restaurant', 'total_price', 'timestamp']
	readonly_fields = ('ordered_items', 'total_price')
	inlines = (ItemInline,)



# Re-register UserAdmin
# admin.site.unregister( User )
# admin.site.register( User, UserAdmin )

admin.site.register( Order, OrderAdmin )
admin.site.register( Item )
# Register your models here.
