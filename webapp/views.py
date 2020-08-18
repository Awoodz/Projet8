from django.template import loader
from django.http import HttpResponse
from webapp.models import Category, Product, Nutriments, User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
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


def results(request):
    template = loader.get_template("webapp/results.html")
    return HttpResponse(template.render(request=request))


def saved_products(request):
    template = loader.get_template("webapp/saved_products.html")
    return HttpResponse(template.render(request=request))

