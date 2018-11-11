'''
This part of application is depricated, because app's structure is changed

'''

# from rest_framework import serializers
# from restaurants.models import Restaurant, Dish, Type, Menu, DishType
#
# # class RestaurantSerializer(serializers.ModelSerializer):
# #
# # 	class Meta:
# # 		model = Restaurant
# # 		fields = [
# # 			'id',
# # 			'name',
# # 			'address',
# # 			'menu'
# # 		]
# # class MenuSerializer(serializers.ModelSerializer):
# # 	class Meta:
# # 		model = Menu
# # 		fields = [
# # 			'name',
# # 			'restaurant',
# # 		]
#
# class DishTypeSerializer(serializers.ModelSerializer):
#
# 	class Meta:
# 		model = DishType
# 		fields = [
# 			'name'
# 		]
#
# class DishSerializer(serializers.ModelSerializer):
# 	type = DishTypeSerializer(read_only=True)
# 	class Meta:
# 		model = Dish
# 		fields = [
# 			'id',
# 			'name',
# 			'ingredients',
# 			'description',
# 			'type'
# 		]
#
#
# # class MenuSerializer(serializers.Serializer):
# class MenuSerializer(serializers.ModelSerializer):
# 	name = serializers.CharField(max_length=90)
# 	# dishes = serializers.PrimaryKeyRelatedField( many=True, read_only=True )
# 	dishes = DishSerializer(read_only=True, many=True)
#
# 	class Meta:
# 		model = Menu
# 		fields = [
# 			'id',
# 			'name',
# 			'dishes',
# 		]
#
# class RestaurantTypeSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Type
# 		fields = [
# 			# 'id',
# 			'name',
# 		]
#
# class RestaurantSerializer(serializers.ModelSerializer):
# 	id = serializers.CharField(max_length=10)
# 	name = serializers.CharField(max_length=90)
# 	address = serializers.CharField(max_length=180)
# 	menu = MenuSerializer(required=False, many=True)
# 	type = RestaurantTypeSerializer(read_only=True)
#
# 	class Meta:
# 		model = Restaurant
# 		fields = [
# 			'id',
# 			'name',
# 			'address',
# 			'type',
# 			'menu',
# 		]
#
#
# class RestaurantListSerializer(serializers.ModelSerializer):
#
# 	class Meta:
# 		model = Restaurant
# 		fields = [
# 			'id',
# 			'name',
# 			'address',
# 		]
# 	def create_restaurant(self, validated_data):
# 		restaurant = Restaurant.objects.create_restaurant(
# 			validated_data['name'],
# 			validated_data['address'],
# 			validated_data['menu']
# 		)
# 		return restaurant
#
#
