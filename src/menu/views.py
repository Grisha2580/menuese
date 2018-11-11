from rest_framework import generics, mixins
from .serializers import DishSerializer
from .models import Dish

class DishAPIView( generics.RetrieveUpdateDestroyAPIView ):
	serializer_class = DishSerializer
	lookup_field = 'id'

	def get_queryset(self):
		qs = Dish.objects.all()
		return qs

class DishAPICreateView(generics.CreateAPIView):
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)