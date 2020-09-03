import webapp.utilities.data as dt
from webapp.utilities.api.externals.openfoodfact_request import Openfoodfact_request


class Requester:
    def __init__(self, category):
        self.product_id_list = self.product_id_requester(category)

    def product_id_requester(self, category):

        product_id_list = []
        i = 0
        while i < dt.MAX_PAGE:
            category_data = Openfoodfact_request.category_request(category, i)
            i += 1
            for dictionnary in category_data["products"]:
                product_id_list.append(dictionnary["_id"])
        return product_id_list

    def product_data_requester(product_id):

        product_data = Openfoodfact_request.product_request(product_id)
        return product_data
