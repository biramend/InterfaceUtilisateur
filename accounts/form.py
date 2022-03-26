from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import CustomerUser


class RegistrationFormUser(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ("email", "phone", "address",)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Adresse mail',
                    'class': 'form-control',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Téléphone',
                    'class': 'form-control',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'placeholder': 'Adresse',
                    'class': 'form-control',
                }
            )

        }
