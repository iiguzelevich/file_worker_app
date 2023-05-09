from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PersonalData

User = get_user_model()


@receiver(post_save, sender=User)
def create_or_update_user_data(sender, instance, created, **kwargs):
    if created:
        instance.personaldata = PersonalData.objects.create(owner=instance)
    instance.personaldata.save()
