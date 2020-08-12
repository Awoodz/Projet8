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
    template = loader.get_template('webapp/legalmention.html')
    return HttpResponse(template.render(request=request))

def product(request):
    template = loader.get_template('webapp/product.html')
    return HttpResponse(template.render(request=request))

def account(request):
    template = loader.get_template('webapp/account.html')
    return HttpResponse(template.render(request=request))

def results(request):
    template = loader.get_template('webapp/results.html')
    return HttpResponse(template.render(request=request))

def saved_products(request):
    template = loader.get_template('webapp/saved_products.html')
    return HttpResponse(template.render(request=request))