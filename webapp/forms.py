from dal import autocomplete
from django import forms

from .models import Product


class BaseForm(forms.ModelForm):
    """Basic search form"""

    product_search = forms.CharField(
        max_length=100,
        label=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Recherchez des substituts à un produit"}
        ),
    )

    class Meta:
        model = Product
        fields = ("product_search",)


class ProductForm(forms.ModelForm):
    """autocomplete search form"""

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
