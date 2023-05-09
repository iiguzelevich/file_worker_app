from django import forms
from django.contrib.auth.models import User
from .models import PersonalData


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class PersonalDataForm(forms.ModelForm):
    class Meta:
        model = PersonalData
        fields = ('information', 'interests', 'photo', 'birth_day')
        widgets = {
            'information': forms.TextInput(
                attrs={
                    'class': 'contact_input contact_textarea',
                    'required': False,
                },
            ),
            'interests': forms.TextInput(
                attrs={
                    'class': 'contact_input contact_textarea',
                    'required': False,
                },
            ),
            'photo': forms.FileInput(
                attrs={
                    'class': 'contact_button',
                },

            )

        }
