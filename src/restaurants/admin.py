from django.contrib import admin
from .models import Restaurant, Type, Table

class TableAdmin(admin.ModelAdmin):
	list_display = ['restaurant','number', 'seates', 'is_available']

class RestaurantAdmin( admin.ModelAdmin ):
	list_display = ['name', 'address', 'type']
	readonly_fields = ('tables',)
admin.site.register(Table, TableAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Type)