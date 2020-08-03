from webapp.utilities.api.product_data import Product_data
from webapp.utilities.api.requester import Requester
import webapp.utilities.data as dt
from webapp.models import Category, Product, Nutriments, User
from django.db import DatabaseError, transaction


class Sql_insert():


    def product_inserter():

        Category.objects.all().delete()
        Product.objects.all().delete()
        Nutriments.objects.all().delete()
        
        i = 0
        for elem in dt.CAT_LIST:
            category = Category(category_name=elem)
            try:
                with transaction.atomic():
                    category.save()
            except DatabaseError:
                print("category insertion error")
                pass

            id_list = Requester(elem).product_id_list

            for product_id in id_list:
                product_data = Product_data(Requester.product_data_requester(product_id))
                product = Product(
                    product_name=product_data.name,
                    product_url=product_data.url,
                    product_img=product_data.img,
                    product_nutriscore=product_data.nutriscore,
                    product_category_id=category
                    )

                nutriments = Nutriments(
                    nutriments_product_id=product,
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
                try:
                    with transaction.atomic():
                        product.save()
                        nutriments.save()
                        i += 1
                        print(str(i) + " produit(s) ajouté(s)")
                except DatabaseError:
                    print("product insertion error")
                    pass


    def user_inserter(name, mail, password):
        user = User(
            user_name=name,
            user_mail=mail,
            user_password=password
        )
        try:
            with transaction.atomic():
                user.save()
        except DatabaseError:
            print("user insertion error")
            pass

    def user_saved_product_inserter(user, product):
        user.user_product.add(product)
        try:
            with transaction.atomic():
                user.save()
        except DatabaseError:
            print("save user>product error")
            pass