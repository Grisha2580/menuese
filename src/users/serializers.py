from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_auth.models import TokenModel
from rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

UserModel = get_user_model()


class CustomTokenSerializer( serializers.ModelSerializer ):
	"""
	   Serializer for getting the user token for authentication
	"""
	token = serializers.CharField( source='key' )

	class Meta:
		model = TokenModel
		fields = ('token',)


class CustomUserSerializer( UserDetailsSerializer ):
	user_type = serializers.IntegerField( source="profile.user_type" )
	class Meta( UserDetailsSerializer.Meta ):
		fields = UserDetailsSerializer.Meta.fields + ('user_type',)


class UserSerializer( serializers.ModelSerializer ):
	email = serializers.EmailField(
		required=True,
		validators=[UniqueValidator( queryset=User.objects.all() )]
	)
	username = serializers.CharField(
		max_length=32,
		validators=[UniqueValidator( queryset=User.objects.all() )]
	)
	password = serializers.CharField( min_length=8, write_only=True )

	def create(self, validated_data):
		user = User.objects.create_user(
			validated_data['username'],
			validated_data['email'],
			validated_data['password']
		)
		return user

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
