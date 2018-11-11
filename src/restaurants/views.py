from rest_framework import generics, mixins, status
from .serializers import RestaurantSerializer, RestaurantListSerializer, RestaurantTypeSerializer
from restaurants.models import Restaurant, Type
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Q
import operator
from functools import reduce
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.models import Profile
from rest_framework.response import Response


"""The logic of this filter is working good, but i didnt realize how to connect 
this filter with search filter 
"""
# class TypeFilter( filters.BaseFilterBackend ):
# # class TypeFilter( filters.SearchFilter, filters.OrderingFilter ):
# 	def filter_queryset(self, request, queryset, view):
# 		keys = request.GET.keys()
# 		result = queryset
# 		if len( keys ) != 0:
# 			if 'type' in keys:
# 				q = request.GET.getlist( 'type' )
# 				# result = queryset.filter( reduce( operator.and_, (Q( menu__in=list(x) ) for x in q) ) )
# 				# result = queryset
# 				# for i in q:
# 				# 	result = result.filter( type__in=[i] )
# 				result = result.filter( type__in=q )
# 				return result
# 			# if 'search' in keys:
# 				# filters.SearchFilter.filter_queryset(request=request, queryset=queryset, view=view)
# 		else:
# 			# filters.SearchFilter.
# 			return queryset


class RestaurantAPIListView( mixins.CreateModelMixin, generics.ListAPIView ):
	serializer_class = RestaurantListSerializer
	queryset = Restaurant.objects.all()
	filter_backends = (filters.SearchFilter, filters.OrderingFilter)#, TypeFilter)
	# filter_backends = (filtersTypeFilter)
	search_fields = ('name', 'address',)
	permission_classes = (IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
		qs = Restaurant.objects.all()
		return qs

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def create(self, request, *args, **kwargs):
		user = self.request.user
		if user.profile.user_type is Profile.MANAGER:
			serializer = self.get_serializer( data=request.data )
			serializer.is_valid( raise_exception=True )
			self.perform_create( serializer )
			headers = self.get_success_headers( serializer.data )
			return Response( serializer.data, status=status.HTTP_201_CREATED, headers=headers )
		else:
			return Response( {'details':'Authentication credentials were not acceptable with this method'}, status=status.HTTP_403_FORBIDDEN)


class RestaurantTypeAPIView( generics.ListAPIView ):
	serializer_class = RestaurantTypeSerializer

	def get_queryset(self):
		qs = Type.objects.all()
		return qs


class RestaurantAPIView( generics.RetrieveUpdateDestroyAPIView ):
	serializer_class = RestaurantSerializer
	lookup_field = 'id'

	def get_queryset(self):
		qs = Restaurant.objects.all()
		return qs
