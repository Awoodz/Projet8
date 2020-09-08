from django.test import TestCase
from django.urls import reverse
from webapp.models import Product, Nutriments, Category
from userapp.models import CustomUser


class IndexPageTestCase(TestCase):
    def test_index_returns_200(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)


class ProductPageTestCase(TestCase):
    def test_product_page_returns_200(self):
        fake_cat = Category.objects.create(category_name="Fake category",)
        fake_prod = Product.objects.create(
            product_name="Fake product",
            product_url="http://fake_product.com",
            product_img="http://fake_product.com/fakeprod.png",
            product_nutriscore="e",
            product_category_id=fake_cat,
        )
        fake_nutri = Nutriments.objects.create(
            nutriments_product_id=fake_prod,
            nutriments_kj="0",
            nutriments_kcal="0",
            nutriments_lipids="0",
            nutriments_fat="0",
            nutriments_carbohydrates="0",
            nutriments_sugar="0",
            nutriments_protein="0",
            nutriments_salt="0",
            nutriments_sodium="0",
        )
        product_id = Product.objects.get(product_name="Fake product").id
        response = self.client.get(reverse("product", args=(product_id,)))
        self.assertEqual(response.status_code, 200)

    def test_product_page_returns_404(self):
        fake_cat = Category.objects.create(category_name="Fake category",)
        fake_prod = Product.objects.create(
            product_name="Fake product",
            product_url="http://fake_product.com",
            product_img="http://fake_product.com/fakeprod.png",
            product_nutriscore="e",
            product_category_id=fake_cat,
        )
        fake_nutri = Nutriments.objects.create(
            nutriments_product_id=fake_prod,
            nutriments_kj="0",
            nutriments_kcal="0",
            nutriments_lipids="0",
            nutriments_fat="0",
            nutriments_carbohydrates="0",
            nutriments_sugar="0",
            nutriments_protein="0",
            nutriments_salt="0",
            nutriments_sodium="0",
        )
        product_id = Product.objects.get(product_name="Fake product").id + 1
        response = self.client.get(reverse("product", args=(product_id,)))
        self.assertEqual(response.status_code, 404)


class LegalMentionPageTestCase(TestCase):
    def test_legal_mention_returns_200(self):
        response = self.client.get(reverse("legalmention"))
        self.assertEqual(response.status_code, 200)


class AccountPageTestCase(TestCase):
    def test_account_returns_200_when_user_logged_in(self):
        user = CustomUser.objects.create(
            username="Fakeuser", email="Fakemail@mail.com", password="password",
        )
        user_login = self.client.force_login(user)
        response = self.client.get(reverse("account"))
        self.assertEqual(response.status_code, 200)

    def test_account_returns_302_when_user_not_logged_in(self):
        user = CustomUser.objects.create(
            username="Fakeuser", email="Fakemail@mail.com", password="password",
        )
        response = self.client.get(reverse("account"))
        self.assertEqual(response.status_code, 302)


class SavedProductsPageTestCase(TestCase):
    def test_saved_products_returns_200_when_user_logged_in(self):
        user = CustomUser.objects.create(
            username="Fakeuser", email="Fakemail@mail.com", password="password",
        )
        user_login = self.client.force_login(user)
        response = self.client.get(reverse("saved_products"))
        self.assertEqual(response.status_code, 200)

    def test_saved_products_returns_302_when_user_not_logged_in(self):
        user = CustomUser.objects.create(
            username="Fakeuser", email="Fakemail@mail.com", password="password",
        )
        response = self.client.get(reverse("saved_products"))
        self.assertEqual(response.status_code, 302)


class SaveProductPageTestCase(TestCase):
    def test_save_products_works(self):
        fake_cat = Category.objects.create(category_name="Fake category",)
        fake_prod = Product.objects.create(
            product_name="Fake product",
            product_url="http://fake_product.com",
            product_img="http://fake_product.com/fakeprod.png",
            product_nutriscore="e",
            product_category_id=fake_cat,
        )
        user = CustomUser.objects.create(
            username="Fakeuser", email="Fakemail@mail.com", password="password",
        )
        product_id = Product.objects.get(product_name="Fake product").id

        user_login = self.client.force_login(user)

        response = self.client.get(
            reverse("save_product"), {"product_token": product_id,}
        )
        self.assertEqual(
            fake_prod.user_product.filter(username="Fakeuser").exists(), True
        )
