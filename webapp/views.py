from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from webapp.models import Category, Product, Nutriments, CustomUser
from .forms import CustomUserCreationForm, SearchForm
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


def product(request):
    template = loader.get_template("webapp/product.html")
    return HttpResponse(template.render(request=request))


def account(request):
    template = loader.get_template("webapp/account.html")
    return HttpResponse(template.render(request=request))


def saved_products(request):
    template = loader.get_template("webapp/saved_products.html")
    return HttpResponse(template.render(request=request))


def search(request):
    template = loader.get_template("webapp/search.html")
    query = request.GET.get("form_input")
    if not query:
        products = Product.objects.all()
    else:
        products = Product.objects.filter(product_name__icontains=query)

    if not products.exists():
        message = "No result"

    for product in products:
        product.product_nutriscore = (
            "static/webapp/img/nutri" + product.product_nutriscore + ".png"
        )
    return HttpResponse(template.render({"products": products}, request=request))

