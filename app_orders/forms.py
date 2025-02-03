from django import forms
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class CheckoutForm(forms.ModelForm):
    address = forms.CharField(max_length=128)

    class Meta:
        model = UserModel
        fields = ["first_name", "last_name", "email", "address"]
