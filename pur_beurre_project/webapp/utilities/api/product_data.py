class Product_data():


    def __init__(self, product_data):
        self.datas = product_data

    @property
    def product_id(self):
        return self.datas["code"]

    @property
    def img(self):
        try:
            img = self.datas["product"]["selected_images"]["front"]["display"]["fr"]
        except KeyError:
            img = "no data"
        return img

    @property
    def url(self):
        return "https://fr.openfoodfacts.org/produit/" + self.datas["code"]

    @property
    def name(self):
        try:
            name = self.datas["product"]["product_name_fr"]
        except KeyError:
            name = "no data"
        return name

    @property
    def energy_kj(self):
        try:
            energy_kj = self.datas["product"]["nutriments"]["energy_100g"]
        except KeyError:
            energy_kj = "no data"
        return energy_kj

    @property
    def energy_kcal(self):
        try:
            energy_kcal = self.datas["product"]["nutriments"]["energy-kcal_100g"]
        except KeyError:
            energy_kcal = "no data"
        return energy_kcal

    @property
    def carbohydrates(self):
        try:
            carbohydrates = self.datas["product"]["nutriments"]["carbohydrates_100g"]
        except KeyError:
            carbohydrates = "no data"
        return carbohydrates

    @property
    def sugar(self):
        try:
            sugar = self.datas["product"]["nutriments"]["sugars_100g"]
        except KeyError:
            sugar = "no data"
        return sugar

    @property
    def lipids(self):
        try:
            lipids = self.datas["product"]["nutriments"]["fat_100g"]
        except KeyError:
            lipids = "no data"
        return lipids

    @property
    def fat(self):
        try:
            fat = self.datas["product"]["nutriments"]["saturated-fat_100g"]
        except KeyError:
            fat = "no data"
        return fat

    @property
    def salt(self):
        try:
            salt = self.datas["product"]["nutriments"]["salt_100g"]
        except KeyError:
            salt = "no data"
        return salt

    @property
    def sodium(self):
        try:
            sodium = self.datas["product"]["nutriments"]["sodium_100g"]
        except KeyError:
            sodium = "no data"
        return sodium

    @property
    def protein(self):
        try:
            protein = self.datas["product"]["nutriments"]["proteins_100g"]
        except KeyError:
            protein = "no data"
        return protein

    @property
    def nutriscore(self):
        try:
            nutriscore = self.datas["product"]["nutriscore_grade"]
        except KeyError:
            try :
                nutriscore = self.datas["product"]["nutrition_grade"]
            except KeyError:
                nutriscore = "none"
        return nutriscore
