from rest_framework import serializers
from .models import Restaurant, Type, Table
from menu.serializers import MenuSerializer


class TableSerializer(serializers.ModelSerializer):
	class Meta:
		model = Table
		fields = [
			'number',
			'is_available',
			'seates'
		]
class RestaurantTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Type
		fields = [
			# 'id',
			'name',
		]

class RestaurantSerializer(serializers.ModelSerializer):
	menu = MenuSerializer(required=False, many=True, read_only=True)
	type = RestaurantTypeSerializer(read_only=True)

	class Meta:
		model = Restaurant
		fields = [
			'id',
			'name',
			'address',
			'type',
			'image',
			'menu',
		]


class RestaurantListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Restaurant
		fields = [
			'id',
			'name',
			'address',
			'image',
		]



