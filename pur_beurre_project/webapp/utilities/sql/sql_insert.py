from webapp.utilities.api.product_data import Product_data
from webapp.utilities.api.requester import Requester
from webapp.models import Category, Product, Nutriments, User


class Sql_insert():


    def __init__(self, category):
        
        self.id_list = Requester(category).product_id_list
        self.prod = self.product_inserter(self.id_list, category)

    def category_inserter():
        category_list = [
            "camenberts",
            "sodas-au-cola",
            "pates-a-tartiner-aux-noisettes"
        ]
        for elem in category_list:
            category = Category(category_name=elem)
            category.save()

    def product_inserter(self, id_list, category):

        for product_id in id_list:
            product_data = Product_data(Requester.product_data_requester(product_id))

            product = Product(
                product_name=product_data.name,
                product_url=product_data.url,
                product_img=product_data.img,
                product_nutriscore=product_data.nutriscore,
                product_category_id=category
            )
            product.save()
            nutriments = Nutriments(
                nutriments_product_id=product_data.name,
                nutriments_kj=product_data.energy_kj,
                nutriments_kcal=product_data.energy_kcal,
                nutriments_lipids=product_data.lipids,
                nutriments_fat=product_data.fat,
                nutriments_carbohydrates=product_data.carbohydrates,
                nutriments_sugar=product_data.sugar,
                nutriments_protein=product_data.protein,
                nutriments_salt=product_data.salt,
                nutriments_sodium=product_data.sodium
            )
            nutriments.save()

    def user_inserter(name, mail, password):
        user = User(
            user_name=name,
            user_mail=mail,
            user_password=password
        )

    def user_saved_product_inserter(user, product):
        user.user_product.add(product)
        user.save()
