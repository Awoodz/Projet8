from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from webapp.models import Category, Product, Nutriments, CustomUser
from .forms import CustomUserCreationForm, SearchForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render


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


def results(request):
    template = loader.get_template("webapp/results.html")
    return HttpResponse(template.render(request=request))


def saved_products(request):
    template = loader.get_template("webapp/saved_products.html")
    return HttpResponse(template.render(request=request))


def test(request, product_id):
    product = Product.objects.get(pk=product_id)
    message = "le nom du produit est {}".format(product.product_name)
    return HttpResponse(message)


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


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "GET":
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, "name.html", {"form": form})
