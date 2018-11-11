from menu.models import Dish
from rest_framework import serializers
from restaurants.models import Restaurant, Table
from .models import Order, Item


class QuantitySerializer( serializers.ModelSerializer ):
	""" This serializer is used to represent orders and quantities in GET
	 api/order/<int:id> method. It's used only in OrderSerializer
	 
	"""

	class Meta:
		model = Item
		fields = [
			'dish',
			'quantity',
			'status',
		]
		depth = 1


class OrderListSerializer( serializers.ModelSerializer ):
	items = QuantitySerializer( source='order_to_dish', many=True, read_only=True )

	class Meta:
		model = Order
		fields = [
			'id',
			'payment_option',
			'restaurant',
			'order_status',
			'items',
			'total_price',
			# 'user',
		]




class OrderSerializer( serializers.ModelSerializer ):
	"""Serializer for orders.
	
	Attributes:
		dishes: field of ItemSerializer class providing the JSON with dish and 
				its quantity in the order
	"""
	items = QuantitySerializer( source='order_to_dish', many=True, read_only=True )
	# table = TableSerializer(read_only=True)
	class Meta:
		model = Order
		fields = [
			'id',
			'restaurant',
			'payment_option',
			'order_status',
			'table',
			'items',
			'timestamp',
			'total_price',

		]

	def update(self, instance, validated_data):
		"""Updates order
		
		:param instance: order which has to be updated
		:param validated_data: data to update
		:return: updated order object
		"""
		items = validated_data.get( 'items' )
		payment_option = validated_data.get( 'payment_option' )
		order_stauts = validated_data.get('order_status')
		order = instance
		if items:
			self.create_items( items, order )
		if payment_option is not None:
			order.payment_option = payment_option
			order.save()
		if order_stauts is not None:
			order.order_status = order_stauts
			order.save()
		return order

	def create(self, validated_data, user=None):
		"""Creates Order instance and item instances
		for each dish in the order and connect them (dishes with order)
		
		:param validated_data: 
		:param user: 
		:return: created order object
		"""

		if user:
			# getting other attributes
			restaurant = Restaurant.objects.get( id=validated_data['restaurant'] )
			table = Table.objects.get( restaurant=restaurant, number=validated_data['table'] )
			table.is_available = False
			table.save()
			items = validated_data['items']

			order = Order(
				restaurant=restaurant,
				payment_option=validated_data['payment_option'],
				order_status=validated_data['order_status'],
				user=user,
				table=table
			)
			order.save()

			self.create_items( items, order )

			return order

		else:
			raise serializers.ValidationError( {"details": "User is not found"} )

	def create_items(self, items, order):
		"""
		Creates item models connecting order with dishes
		
		:param items: a dictionary of items  
		:param order: order with missing items
		"""
		for item in items:
			dish = Dish.objects.filter( id=item['dish'] )[0]
			quantity = item['quantity']
			Item.objects.create_item( order, dish, quantity )
