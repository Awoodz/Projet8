from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Product


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    # prod_search = forms.ModelChoiceField(
    #     queryset=Product.objects.all(),
    #     widget=autocomplete.ModelSelect2(url='product-autocomplete')
    # )

