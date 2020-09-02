from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Product
from dal import autocomplete


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class ProductForm(forms.ModelForm):
    product_search = forms.ModelChoiceField(
        label=False,
        queryset=Product.objects.all(),
        widget=autocomplete.ModelSelect2(
            url="autocomplete",
            attrs={
                # Set some placeholder
                "data-placeholder": "Recherchez des substituts à un produit",
                # Only trigger autocompletion after 3 characters have been typed
                "data-minimum-input-length": 3,
            },
        ),
    )

    class Meta:
        model = Product
        fields = ("product_search",)
