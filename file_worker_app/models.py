from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


def original_path_txt(self, name_file):
    return f'user_{self.owner.id}/original_txt/{name_file}'


def original_path_pdf(self, filename):
    return f'user_{self.owner.id}/original_pdf/{filename}'


def original_path_video(self, filename):
    return f'user_{self.owner.id}/original_video/{filename}'


class TXTtoPDF(models.Model):
    class Meta:
        verbose_name = 'TXTtoPDF'

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

    text_file = models.FileField(upload_to=original_path_txt)

    uploaded_at = models.DateTimeField(auto_now_add=True)


class PDFfromTXT(models.Model):
    class Meta:
        verbose_name = 'PDFfromTXT'

    owner = models.ForeignKey(
        User,
        verbose_name='owner',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    original_file = models.OneToOneField(
        TXTtoPDF,
        verbose_name='original file',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    file_name = models.CharField(
        max_length=256,
        blank=False,
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name="Published"
    )

    format_file = models.CharField(
        max_length=50,
        blank=False
    )

    pdf_file = models.FileField()

    uploaded_at = models.DateTimeField(auto_now_add=True)

    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name="Time of change"
    )

    def get_absolute_url(self):
        return reverse(
            'edit_file_pdf',
            kwargs={'file_name': self.file_name}
        )

    def delete_pdf(self):
        return reverse(
            'delete_file_pdf',
            kwargs={'file_name': self.file_name}
        )

    def publish_pdf(self):
        return reverse(
            viewname='publish_pdf',
            kwargs={
                'file_name': self.file_name,
            }
        )


class PDFtoAudio(models.Model):
    class Meta:
        verbose_name = 'PDFtoMP3'

    owner = models.ForeignKey(
        User,
        verbose_name='owner',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

    file_name = models.CharField(
        max_length=256,
        blank=False,
    )

    pdf_file = models.FileField(upload_to=original_path_pdf)

    uploaded_at = models.DateTimeField(auto_now_add=True)


class AudiofromPDF(models.Model):
    class Meta:
        verbose_name = 'MP3fromPDF'

    owner = models.ForeignKey(
        User,
        verbose_name='owner',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    original_file = models.OneToOneField(
        PDFtoAudio,
        verbose_name='original file',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    file_name = models.CharField(
        max_length=256,
        blank=False,
    )

    audio_file = models.FileField()

    uploaded_at = models.DateTimeField(auto_now_add=True)

    is_published = models.BooleanField(
        default=False,
        verbose_name="Published"
    )

    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name="Time of change"
    )

    def get_absolute_url(self):
        return reverse(
            'edit_file_audio',
            kwargs={'file_name': self.file_name}
        )

    def delete_audio(self):
        return reverse(
            'delete_file_audio',
            kwargs={'file_name': self.file_name}
        )

    def publish_audio(self):
        return reverse(
            viewname='publish_audio',
            kwargs={'file_name': self.file_name}
        )


class VideoToGIF(models.Model):
    class Meta:
        verbose_name = 'MP4 file'

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

    video_file = models.FileField(upload_to=original_path_video)

    uploaded_at = models.DateTimeField(auto_now_add=True)


class GIFfromVideo(models.Model):
    class Meta:
        verbose_name = 'GIF'

    owner = models.ForeignKey(
        User,
        verbose_name='owner',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    original_file = models.OneToOneField(
        VideoToGIF,
        verbose_name='original file',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    file_name = models.CharField(
        max_length=256,
        blank=False,
    )

    gif_file = models.FileField(upload_to=original_path_txt)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    is_published = models.BooleanField(
        default=False,
        verbose_name="Published"
    )

    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name="Time of change"
    )

    def get_absolute_url(self):
        return reverse(
            'edit_file_gif',
            kwargs={'file_name': self.file_name}
        )

    def delete_gif(self):
        return reverse(
            'delete_file_gif',
            kwargs={'file_name': self.file_name}
        )

    def publish_gif(self):
        return reverse(
            viewname='publish_gif',
            kwargs={'file_name': self.file_name}
        )
