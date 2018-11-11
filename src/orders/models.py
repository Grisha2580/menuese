from django.contrib.auth.models import User
from django.db import models
from menu.models import Dish
from restaurants.models import Restaurant, Table


class Order( models.Model ):
	"""Order model class.
	
	Attributes:
		restaurant: links on restaurant from which the order was made
		payment_option: int number showing payment type: 0 - cash, 1 - card
		order_status: int number showing order status: 0 - in progress,
			1 - waiting for payment, 2 - paid.
		dishes: field linking on DishQuantity through model making connection between
		order and its dishes
		timestamp: created date
		total_price: property counting how much does order coast
	
	"""
	# PAYMENT_TYPE Initialization
	CASH = 0
	CARD = 1

	PAYMENT_TYPE = (
		(CASH, 'Cash'),
		(CARD, 'Card'),
	)

	# ORDER_STATUS Initialization
	PAID = 2
	WFP = 1
	IN_PROGRESS = 0

	ORDER_STATUS = (
		(PAID, 'Paid'),
		(WFP, 'Waiting For Payment'),
		(IN_PROGRESS, 'In Progress'),
	)

	restaurant = models.ForeignKey( Restaurant, on_delete=models.CASCADE, null=True )
	user = models.ForeignKey( User, on_delete=models.CASCADE, null=True )
	payment_option = models.IntegerField( choices=PAYMENT_TYPE, default=CARD )
	order_status = models.IntegerField( choices=ORDER_STATUS, default=IN_PROGRESS )
	items = models.ManyToManyField( Dish, through='Item', related_name='dishes_in_order' )
	timestamp = models.DateTimeField( auto_now_add=True )
	table = models.ForeignKey(Table, on_delete=models.CASCADE, null = True)

	# total price counting function
	@property
	def total_price(self):
		total = 0
		for item in self.get_items():
			quantity = item.quantity
			total += (item.dish.price * quantity)

		return total

	@property
	def ordered_items(self):
		items = self.get_items()
		answer = ''
		for index, item in enumerate( items ):
			answer += '{}. dish : {}; quantity: {}; price: {},\n'.format( index + 1, item.dish.name,
			                                                            item.quantity,
			                                                            item.dish.price )
		return answer

	def __str__(self):
		return '{}'.format( self.id )

	def get_items(self):
		return Item.objects.filter( order=self ).all()


class ItemManager( models.Manager ):
	"""Dish Quantity object manager"""

	def create_item(self, order, dish, quantity):
		item = self.create( order=order, dish=dish, quantity=quantity )
		return item


class Item( models.Model ):
	"""This class provides many-to-many relationships
    between order and dish models.	
	
	Attributes:
		DISH_STATUS: choices model representing dish statuses
		dish: link to Dish model of the order
		order: link to the Order model
		dish_status: 
		quantity: this field represents number of dishes in order
		objects: Object Manager
	"""

	# DISH_STATUS initialization
	ACCEPTED = 0
	IS_BEING_COOKED = 1
	IS_READY_TO_BE_SERVED = 2

	STATUS = (
		(ACCEPTED, 'Accepted'),
		(IS_BEING_COOKED, 'Is being cooked'),
		(IS_READY_TO_BE_SERVED, 'Is ready to be served'),
	)

	dish = models.ForeignKey( Dish, on_delete=models.CASCADE, related_name='dish_to_order' )
	order = models.ForeignKey( Order, on_delete=models.CASCADE, related_name='order_to_dish' )
	status = models.IntegerField( choices=STATUS, default=ACCEPTED )
	quantity = models.IntegerField()
	objects = ItemManager()
