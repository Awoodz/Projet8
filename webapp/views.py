from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from webapp.models import Category, Product, Nutriments, CustomUser
from webapp.utilities.sql.sql_insert import Sql_insert
from .forms import CustomUserCreationForm, ProductForm
from django.urls import reverse_lazy, reverse
from urllib.parse import urlencode
from django.views import generic
from django.shortcuts import render, redirect
from dal import autocomplete


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "webapp/signup.html"


class IndexView(generic.FormView):
    form_class = ProductForm

    def get(self, request):
        return render(request, "webapp/index.html", {"prodform": self.form_class,})


def legal_mention(request):
    template = loader.get_template("webapp/legalmention.html")
    return HttpResponse(template.render(request=request))


def account(request):
    template = loader.get_template("webapp/account.html")
    return HttpResponse(template.render(request=request))


def saved_products(request):
    template = loader.get_template("webapp/saved_products.html")
    current_user = request.user
    products = Product.objects.filter(user_product=current_user.id)
    return HttpResponse(template.render({"products": products}, request=request))


def product(request, product_id):
    template = loader.get_template("webapp/product.html")
    product = Product.objects.get(pk=product_id)
    nutriment = Nutriments.objects.get(nutriments_product_id=product_id)

    return HttpResponse(
        template.render({"product": product, "nutriment": nutriment}, request=request)
    )


def search(request):
    template = loader.get_template("webapp/search.html")
    query = request.GET.get("product_search")

    try:
        searched_product = Product.objects.filter(id=query)
    except ValueError:
        searched_product = Product.objects.filter(product_name__iexact=query)

    try:
        for picked_product in searched_product:
            products = Product.objects.filter(
                product_category_id=picked_product.product_category_id
            ).order_by("product_nutriscore")

        return HttpResponse(
            template.render(
                {"searched_product": searched_product, "products": products,},
                request=request,
            )
        )
    except UnboundLocalError:
        base_url = reverse("search_help")
        query_string = urlencode({"query": query})
        url = "{}?{}".format(base_url, query_string)
        return redirect(url)


class ProductAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        request = Product.objects.all()

        if self.q:
            request = request.filter(product_name__istartswith=self.q)

        return request


class ProductView(generic.FormView):
    form_class = ProductForm

    def get(self, request):
        query = request.GET.get("query")
        products = Product.objects.filter(product_name__icontains=query)
        return render(
            request,
            "webapp/search_help.html",
            {"prodform": self.form_class, "query": query, "products": products},
        )


def save_product(request):
    current_user = request.user
    get_product_id = request.GET.get("product_token")

    product = Product.objects.get(pk=get_product_id)

    Sql_insert.user_saved_product_inserter(product, current_user)

    return HttpResponse("Vous n'avez rien à faire ici")
