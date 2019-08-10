import product_overview
from flask.json import jsonify
from flask_restful import Api, Resource


class ProductOverviewWebService(Resource):
    @staticmethod
    def init_service(product_overview, flask):
        """
        :type product_overview: product_overview.ProductOverview
        :type flask: flask.Flask
        """
        Api(flask).add_resource(ProductOverviewWebService, '/products', resource_class_args=([product_overview]))

    def __init__(self, *args):
        """
        :param args: 0: bakery.product_overview.ProductOverview
        """
        super(ProductOverviewWebService, self).__init__()
        self._product_overview = args[0]  # type: product_overview.ProductOverview

    def get(self):
        products_dict = ProductOverviewWebService._convert_to_list_of_dict(self._fetch_products())
        return jsonify(products_dict)

    def _fetch_products(self):
        """
        # Design comment.
        # Logic of the service enclosed with a separate method. The get method follows only technology aspects related to Flask.
        # This method can be reused by RESTful, SOAP and other services after moving it to the new ProductOverviewService class.
        # Now, we have only one (RESTful) service, so let's keep them separated in a single class. This way, we are ready for new.
        # Note. In real projects the logic can be more complex.

        :returns [{product_attr_key, product_attr_value}]
        :rtype: list[dict[str, str]]
        """
        return self._product_overview.fetch()

    @staticmethod
    def _convert_to_list_of_dict(products):
        """
        :type products: bakery.product_model.Products
        :rtype: list[dict[str, str]]
        """
        return [product.as_dict() for product in products]


class NewestProductIdWebService(Resource):
    @staticmethod
    def init_service(product_overview, flask):
        """
        :type product_overview: bakery.product_overview.ProductOverview
        :type flask: flask.Flask
        """
        Api(flask).add_resource(NewestProductIdWebService, '/products/newest_id', resource_class_args=([product_overview]))

    def __init__(self, *args):
        """
        :param args: 0: bakery.product_overview.ProductOverview
        """
        super(NewestProductIdWebService, self).__init__()
        self._product_overview = args[0]  # type: product_overview.ProductOverview

    def get(self):
        return jsonify(id=self._fetch_newest_id())

    def _fetch_newest_id(self):
        """
        :rtype: str
        """
        return self._product_overview.find_newest_id()
