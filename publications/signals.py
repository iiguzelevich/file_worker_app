from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import PublishedFiles, Subscriber

from .tasks import send_letter

User = get_user_model()


@receiver(pre_save, sender=PublishedFiles)
def my_callback(sender, instance, **kwargs):
    try:
        sub_id = instance.owner_id
        user_sub = Subscriber.objects.filter(subscription_id=6)

        us = User.objects.filter(subscriber__subscription_id=sub_id)

        _mail = [u.email for u in us if u != '']

        send_letter.delay(_mail)

    except ObjectDoesNotExist:
        ...
