from rest_framework import generics, status, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Order
from .serializers import (
	OrderListSerializer,
	OrderSerializer,
)


class OrderAPIListView( generics.ListAPIView ):
	serializer_class = OrderListSerializer
	permission_classes = (IsAuthenticated,)
	http_method_names = ['get', 'options']

	def get_queryset(self):
		user = self.request.user
		return Order.objects.filter( user=user )

	def list(self, request, *args, **kwargs):
		queryset = self.filter_queryset( self.get_queryset() )
		serializer = self.get_serializer( queryset, many=True )
		json = serializer.data
		for index, item in enumerate( json ):
			item['restaurant'] = queryset[index].restaurant.name
			item['timestamp'] = queryset[index].timestamp
		return Response( json )


class OrderAPICreateView( generics.CreateAPIView ):
	""" This View provides clients opportunities to add new orders 
	"""
	serializer_class = OrderSerializer

	# This property is commented just to test the methods on clients:
	permission_classes = (IsAuthenticated,)

	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class( data=request.data )
		if serializer.is_valid():
			order = serializer.create( request.data, user=self.request.user )
			if order:
				json = {'id': order.id}
				json.update( serializer.validated_data )
				json['restaurant'] = order.restaurant.name
				json['total_price'] = order.total_price
				json['table'] = order.table.number
				json['timestamp'] = order.timestamp
				items = order.get_items()
				dish_list_to_json = []
				for item in items:
					dish_list_to_json.append( {
						'quantity': item.quantity,
						'status': item.status,
						'dish': {
							'name': item.dish.name,
							'price': item.dish.price,
						},
					} )
				json['items'] = dish_list_to_json
				return Response( json, status=status.HTTP_201_CREATED )
		return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

	def get_queryset(self):
		qs = Order.objects.all()
		return qs


# class OrderAPIView(mixins.CreateModelMixin, generics.RetrieveUpdateDestroyAPIView ):
class OrderAPIView( mixins.RetrieveModelMixin, mixins.CreateModelMixin, generics.GenericAPIView ):
	"""Generates order using its id. I'ts available only for users provided
	 authentication credentials
	
	"""
	serializer_class = OrderSerializer
	permission_classes = (IsAuthenticated,)
	lookup_field = 'id'

	# http_method_names = ['get', 'post', 'options']

	def create(self, request,id):
		instance = self.get_object(id=id)
		serializer = self.serializer_class( data=request.data, partial=True )
		if serializer.is_valid():
			serializer.update( instance, request.data )
			new_ser = self.serializer_class( instance )
			return Response( new_ser.data, status=status.HTTP_200_OK )
		return Response( serializer.errors, status=status.HTTP_400_BAD_REQUEST )

	def post(self, request, id, format=None):
		return self.create(request=request, id=id)

	def get(self, request, id, format=None):
		print( id )
		snippet = self.get_object( id=id )
		serializer = OrderSerializer( snippet )
		return Response( serializer.data )


	def get_queryset(self):
		qs = Order.objects.all()
		return qs

	def get_object(self, id):
		return Order.objects.get( id=id )
