import requests


class Openfoodfact_request():


    def category_request(category, page_nb):
        request = requests.get(
            "https://fr.openfoodfacts.org/category/" +
            category + "/" + str(page_nb) + ".json"
        )
        return request.json()

    
    def product_request(product_id):
        request = requests.get(
            "https://fr.openfoodfacts.org/api/v0/product/" +
            product_id + ".json"
        )
        return request.json()