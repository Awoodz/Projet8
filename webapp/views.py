from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from webapp.models import Category, Product, Nutriments, CustomUser
from .forms import CustomUserCreationForm, ProductForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from dal import autocomplete


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "webapp/signup.html"


def index(request):
    template = loader.get_template("webapp/index.html")
    return HttpResponse(template.render(request=request))


def base_show(request):
    template = loader.get_template("webapp/base.html")
    return HttpResponse(template.render(request=request))


def legal_mention(request):
    template = loader.get_template("webapp/legalmention.html")
    return HttpResponse(template.render(request=request))


def account(request):
    template = loader.get_template("webapp/account.html")
    return HttpResponse(template.render(request=request))


def saved_products(request):
    template = loader.get_template("webapp/saved_products.html")
    return HttpResponse(template.render(request=request))


def product(request, product_id):
    template = loader.get_template("webapp/product.html")
    product = Product.objects.get(pk=product_id)
    nutriment = Nutriments.objects.get(nutriments_product_id=product_id)

    return HttpResponse(
        template.render(
            {
                "product": product,
                "nutriment": nutriment
            },
            request=request
        )
    )


def search(request):
    template = loader.get_template("webapp/search.html")
    query = request.GET.get("product_search")

    searched_product = Product.objects.filter(id__icontains=query)

    for picked_product in searched_product:
        products = Product.objects.filter(
            product_category_id=picked_product.product_category_id
        ).order_by("product_nutriscore")

    if request.POST.get('save'):
        print('user clicked summary')

    return HttpResponse(
        template.render(
            {
                "searched_product": searched_product,
                "products": products
            },
            request=request
        )
    )


class ProductAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        request = Product.objects.all()

        if self.q:
            request = request.filter(product_name__istartswith=self.q)

        return request


class ProductView(generic.FormView):
    template_name = 'webapp/search_form.html'
    form_class = ProductForm

def save_product(request, product, user):
    product.user_product.add(user)
    product.save()