from django.db import models


class Type( models.Model ):
	name = models.CharField( max_length=90 )

	def __str__(self):
		return self.name


class Restaurant( models.Model ):
	name = models.CharField( max_length=90 )
	address = models.CharField( max_length=200 )
	type = models.ForeignKey( Type, on_delete=models.CASCADE, blank=True, null=True )
	image = models.ImageField( default='restaurants_images/default.png', upload_to='restaurants_images', null=True )

	@property
	def tables(self):
		tables = Table.objects.filter( restaurant=self ).all()
		print( tables )
		str_tables = ''
		for table in tables:
			print( table )
			str_tables += 'Number: {}; is available: {}; seates: {}\n'.format( table.number, table.is_available,
			                                                                   table.seates )
		return str_tables

	def __str__(self):
		return self.name


class Table( models.Model ):
	restaurant = models.ForeignKey( Restaurant, on_delete=models.CASCADE )
	number = models.IntegerField()
	is_available = models.BooleanField( default=True )
	seates = models.IntegerField()

	def __str__(self):
		return '{} table № {}'.format( self.restaurant.name, self.number )
