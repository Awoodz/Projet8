from django.template import loader
from django.http import HttpResponse
from webapp.models import Category, Product, Nutriments, User

def index(request):

    template = loader.get_template('webapp/index.html')
    return HttpResponse(template.render(request=request))

    # products = Product.objects.filter()
    # formatted_products = ["<li>{}</li>".format(product.product_name) for product in products]
    # message = """<ul>{}</ul>""".format("\n".join(formatted_products))
    # return HttpResponse(message)

# def listing(request):
#     products = Product.objects.filter()
#     formatted_products = ["<li>{}</li>".format(product.product_name) for product in products]
#     message = """<ul>{}</ul>""".format("\n".join(formatted_products))
#     return HttpResponse(message)

# def detail(request, product_id):
#     product = Product.objects.get(pk=product_id)
#     nutriments = " ".join([nutriments.nutriments_sugar for nutriment in product.nutriments.all()])
#     message = "Le nom de l'album est {}. Il a été écrit par {}".format(product.product_name, nutriments)
#     return HttpResponse(message)

def base_show(request):
    template = loader.get_template('webapp/base.html')
    return HttpResponse(template.render(request=request))

def legal_mention(request):
    message = "mentions légale ici"
    return HttpResponse(message)

def product(request):
    message = "page produit"
    return HttpResponse(message)

def account(request):
    message = "page compte"
    return HttpResponse(message)

def results(request):
    message = "page résultat"
    return HttpResponse(message)

def saved_products(request):
    message = "produits sauvegardés"
    return HttpResponse(message)