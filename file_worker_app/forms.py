from django import forms
from .models import PDFfromTXT, AudiofromPDF, GIFfromVideo


class AddTextFileForm(forms.Form):
    file_name = forms.CharField(
        max_length=255,
        label="Name",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    text_file = forms.FileField(
        label="File",
    )


class AddPDFFileForm(forms.Form):
    file_name = forms.CharField(
        max_length=255,
        label="Name",
        widget=forms.TextInput(attrs={'class': 'form-control'})

    )
    pdf_file = forms.FileField(
        label="File",
    )


class AddVideoFileForm(forms.Form):
    file_name = forms.CharField(
        max_length=255,
        label="Name",
        widget=forms.TextInput(attrs={'class': 'form-control'})

    )
    video_file = forms.FileField(
        label="File",
    )
    start = forms.IntegerField(label="Start", )
    stop = forms.IntegerField(label="Stop", )


class EditPDFfromTextForm(forms.ModelForm):
    class Meta:
        model = PDFfromTXT
        fields = ('file_name',)


class EditAudiofromPDFForm(forms.ModelForm):
    class Meta:
        model = AudiofromPDF
        fields = ('file_name',)


class EditGIFfromVideoForm(forms.ModelForm):
    class Meta:
        model = GIFfromVideo
        fields = ('file_name',)
