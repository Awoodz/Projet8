from urllib.parse import urlencode

from dal import autocomplete
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from django.views import generic

from webapp.models import Category, Nutriments, Product
from webapp.utilities.sql.sql_insert import Sql_insert

from userapp.models import CustomUser

from .forms import ProductForm


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
    current_user = request.user

    try:
        searched_product = Product.objects.filter(id=query)
    except ValueError:
        searched_product = Product.objects.filter(product_name__unaccent__iexact=query)
        if searched_product.count() != 1:
            base_url = reverse("search_help")
            query_string = urlencode({"query": query})
            url = "{}?{}".format(base_url, query_string)
            return redirect(url)

    for picked_product in searched_product:
        products = (
            Product.objects.filter(
                product_category_id=picked_product.product_category_id
            )
            .exclude(product_nutriscore__gte=picked_product.product_nutriscore)
            .order_by("product_nutriscore")[:30]
        )

    return HttpResponse(
        template.render(
            {"searched_product": searched_product, "products": products,},
            request=request,
        )
    )


class ProductAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        request = Product.objects.all()

        if self.q:
            request = request.filter(product_name__unaccent__istartswith=self.q)

        return request


class ProductView(generic.FormView):
    form_class = ProductForm

    def get(self, request):
        query = request.GET.get("query")
        products = Product.objects.filter(product_name__unaccent__icontains=query)
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
