from rest_framework import serializers
from .models import Dish, Menu, DishType


class DishTypeSerializer( serializers.ModelSerializer ):
	class Meta:
		model = DishType
		fields = ['name']


class DishSerializer( serializers.ModelSerializer ):
	type = DishTypeSerializer( read_only=True )

	class Meta:
		model = Dish
		fields = [
			'id',
			'name',
			'ingredients',
			'description',
			'type',
			'price',
		]


class MenuSerializer( serializers.ModelSerializer ):
	name = serializers.CharField( max_length=90 )
	dishes = DishSerializer( read_only=True, many=True )

	class Meta:
		model = Menu
		fields = [
			'id',
			'name',
			'dishes',
		]
