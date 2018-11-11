from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from users.views import UserCreateAPIView
from menu.views import (
	DishAPIView,
	# DishApiCreateView
)
from restaurants.views import (
	RestaurantAPIListView,
	RestaurantAPIView,
	RestaurantTypeAPIView
)
from orders.views import (
	OrderAPIView,
	OrderAPICreateView,
	OrderAPIListView,
)

# app_name = 'restaurants'
app_name = 'api'

urlpatterns = [
	# users API methods
	path( 'users/create', UserCreateAPIView.as_view(), name='account-create' ),
	path( 'users/', include('rest_auth.urls')),

	# restaurants API methods
	path( 'restaurants', RestaurantAPIListView.as_view() ),
	path( 'restaurants/<int:id>', RestaurantAPIView.as_view() ),
	path( 'restaurants/types', RestaurantTypeAPIView.as_view() ),

	# menu API methods
	path( 'menu/dish/<int:id>', DishAPIView.as_view() ),

	# orders API methods
	path( 'orders', OrderAPIListView.as_view() ),
	path( 'orders/<int:id>', OrderAPIView.as_view() ),
	path( 'orders/add', OrderAPICreateView.as_view() ),
]
