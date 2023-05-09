from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class PublishedFiles(models.Model):
    class Meta:
        verbose_name = 'Published Files'

    owner = models.ForeignKey(
        User,
        verbose_name='owner',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    file_name = models.CharField(
        max_length=256,
        blank=False,
    )

    description = models.CharField(
        max_length=256,
        blank=True
    )
    category = models.CharField(
        max_length=256,
        blank=True
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Published"
    )

    format_file = models.CharField(
        max_length=50,
        blank=False
    )

    file_source = models.FileField()

    uploaded_at = models.DateTimeField(auto_now_add=True)

    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name="Time of change"
    )

    def subscribe(self):
        return reverse(
            viewname='subscribe',
            kwargs={'file_name': self.file_name}
        )


class Comments(models.Model):
    class Meta:
        verbose_name = 'Comments'

    comment_text = models.TextField(verbose_name='Comment text')

    published_file = models.ForeignKey(
        PublishedFiles,
        verbose_name='Published File',
        on_delete=models.CASCADE,
        blank=False,
    )

    owner = models.ForeignKey(
        User,
        verbose_name='owner',
        on_delete=models.CASCADE,
        blank=False
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse(
            'comment_file',
            kwargs={'id': self.pk}
        )


class Subscription(models.Model):
    class Meta:
        verbose_name = 'Subscription'

    owner = models.OneToOneField(
        User,
        related_name='subscription',
        on_delete=models.CASCADE,
    )


class Subscriber(models.Model):
    class Meta:
        verbose_name = 'Subscriber'

    subscriber_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='subscriber',
        blank=False,
    )
    subscription = models.ForeignKey(
        Subscription,
        to_field='owner',
        on_delete=models.CASCADE,
        related_name='subscriber',
        blank=False,
    )
