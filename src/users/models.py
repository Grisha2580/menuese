from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile( models.Model ):
	WAITER = 0
	COOK = 1
	MANAGER = 2
	CUSTOMER = 3

	USER_TYPE = (
		(WAITER, 'Waiter'),
		(COOK, 'Cook'),
		(MANAGER, 'Manager'),
		(CUSTOMER, 'Customer')
	)

	# user = models.OneToOneField( User, on_delete=models.CASCADE, related_name='user' )
	user = models.OneToOneField( User, on_delete=models.CASCADE )
	user_type = models.IntegerField( choices=USER_TYPE, default=CUSTOMER )
# type = models.CharField(max_length=100)


@receiver( post_save, sender=User )
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create( user=instance )


@receiver( post_save, sender=User )
def save_user_profile(sender, instance, **kwargs):
	instance.profile.save()
