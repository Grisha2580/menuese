'''
This part of application is depricated, because app's structure is changed

'''


# from rest_framework import generics, mixins
# from .serializers import RestaurantSerializer, RestaurantListSerializer, DishSerializer, RestaurantTypeSerializer
# from restaurants.models import Restaurant, Dish, Type
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters
# from django.db.models import Q
# import operator
# from functools import reduce


#
#
# class DishFilter( filters.BaseFilterBackend ):
# 	def filter_queryset(self, request, queryset, view):
# 		keys = request.GET.keys()
# 		result = queryset
# 		if len( keys ) != 0:
# 			if 'menu' in keys:
# 				q = request.GET.getlist( 'menu' )
# 				# result = queryset.filter( reduce( operator.and_, (Q( menu__in=list(x) ) for x in q) ) )
# 				# result = queryset
# 				for i in q:
# 					result = result.filter( menu__in=[i] )
# 				return result
# 		else:
# 			return queryset
#
#
# class RestaurantAPIListView( generics.ListAPIView ):
# 	serializer_class = RestaurantListSerializer
# 	queryset = Restaurant.objects.all()
# 	filter_backends = (filters.SearchFilter, filters.OrderingFilter, DishFilter)
# 	search_fields = ('name', 'adress')
#
# 	def get_queryset(self):
# 		qs = Restaurant.objects.all()
# 		return qs
#
# 	# def get_queryset(self, *args, **kwargs):
# 	# 	queryset_list = Restaurant.objects.all()
# 	# 	# filtered_queryset = []
# 	# 	query_names = self.request.GET.keys()
# 	# 	queries = self.request.GET
# 	#
# 	# 	if 'menu' in query_names:
# 	# 		menu_ids = queries.getlist( 'menu' )
# 	# 		dish_queryset = Dish.objects.all()
# 	#
# 	# 		for menu in dish_queryset:
# 	# 			is_a_correct_item = False
# 	#
# 	# 			for menu_id in menu_ids:
# 	# 				if menu.id == int(menu_id):
# 	# 					is_a_correct_item = True
# 	# 					print('now its working')
# 	#
# 	# 			if not is_a_correct_item:
# 	# 				dish_queryset = dish_queryset.exclude(id=menu.id)
# 	# 				print('{} is removed from the queryset'.format(menu))
# 	#
# 	# 		# for restaurant in queryset_list:
# 	# 		# 	for dish in restaurant.menu:
# 	# 		# 		if dish not in dish_queryset:
# 	# 		# 			queryset_list = queryset_list.exclude(id=restaurant.id)
# 	# 		print('sdfnkjasfnbjkasbdklasbfkjlasbdkljasbjd')
# 	# 		print(queryset_list)
# 	#
# 	# 		return queryset_list
# 	#
# 	# 	print( queries )
# 	# 	return queryset_list
#
#
# # def post(self, request, *args, **kwargs):
# # 	return self.create( request, *args, **kwargs )
# #
# # def perform_create(self, serializer):
# # 	serializer.save()
#
#
# class DishAPIView( generics.RetrieveUpdateDestroyAPIView ):
# 	serializer_class = DishSerializer
# 	lookup_field = 'id'
#
# 	def get_queryset(self):
# 		qs = Dish.objects.all()
# 		return qs
#
#
# class RestaurantTypeAPIView( generics.ListAPIView):
# 	serializer_class = RestaurantTypeSerializer
#
# 	def get_queryset(self):
# 		qs = Type.objects.all()
# 		return qs
#
# class RestaurantAPIView( generics.RetrieveUpdateDestroyAPIView ):
# 	serializer_class = RestaurantSerializer
# 	lookup_field = 'id'
#
# 	def get_queryset(self):
# 		qs = Restaurant.objects.all()
# 		return qs
#
# 	# def get_object(self):
# 	# 	id = self.kwargs.get('id')
# 	# 	qs = Restaurant.objects.filter(id=id)
# 	# 	return qs
