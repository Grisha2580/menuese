from django.db import models
from restaurants.models import Restaurant


class Menu( models.Model ):
	name = models.CharField( max_length=90 )
	restaurant = models.ForeignKey( Restaurant, on_delete=models.CASCADE, related_name='menu' )

	def __str__(self):
		return self.restaurant.name + ' ' + self.name


class DishType( models.Model ):
	name = models.CharField( max_length=90 )

	def __str__(self):
		return self.name

	# image = models.ImageField( upload_to='pic_folder/', default='pic_folder/None/no-img.jpg', blank=True )


class Dish( models.Model ):
	name = models.CharField( max_length=90 )
	ingredients = models.CharField( max_length=500, null=True, blank=True,
	                                help_text='Separate items by comma' )
	description = models.CharField( max_length=400, null=True, blank=True )
	type = models.ForeignKey( DishType, on_delete=models.CASCADE, blank=True, null=True, related_name='dish_type' )
	price = models.DecimalField( max_digits=10, decimal_places=2, default=0.00 )
	menu = models.ForeignKey( Menu, on_delete=models.CASCADE, blank=True, null=True, related_name='dishes' )

	class Meta:
		verbose_name_plural = 'Dishes'

	def __str__(self):
		return self.name
