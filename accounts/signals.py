from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Customer


def customer_profile(sender, instance, created, **kwargs):
    if created:
        group, _ = Group.objects.get_or_create(name='customers')
        instance.groups.add(group)

        Customer.objects.create(
            user=instance,
            name=instance.username,
        )
        print('profile ok')


post_save.connect(customer_profile, sender=User)
