import product_editor
from flask import jsonify
from flask_restful import Resource, Api, reqparse

from product_model import Product


class ProductEditorWebService(Resource):
    @staticmethod
    def init_service(product_editor, flask):
        """
        :type product_editor: bakery.product_editor.ProductEditor
        :type flask: flask.Flask
        """
        api = Api(flask)
        api.add_resource(ProductEditorWebService, "/products", resource_class_args=([product_editor]))
        api.add_resource(ProductEditorWebService, "/products/<product_id>", resource_class_args=([product_editor]),
                         endpoint="bakery.product")

    def __init__(self, *args):
        """
        # Design comment.
        # "_support_following_product_attr" is an initialization method and should be considered as a constructor flaw.
        # This is Flask way. Fortunately "RequestParser()" and "add_argument" don't make testing harder.
        # Otherwise these are candidates for stubbing or choosing different REST framework.

        :param args: 0: bakery.product_editor.ProductEditor
        """
        super(ProductEditorWebService, self).__init__()
        self._product_editor = args[0]  # type: product_editor.ProductEditor
        self._support_following_product_attrs()

    def get(self, product_id):
        """
        :type product_id: str
        :rtype: bakery.product_model.Product
        """
        return jsonify(self._fetch_product(product_id).as_dict())

    def post(self):
        product_attrs = self._reqparse.parse_args()
        return jsonify(id=(self._store_product(product_attrs)))

    def _store_product(self, product_attrs):
        """
        :type product_attrs: dict[str, str]
        :rtype: str
        """
        product = Product(product_attrs["name"], product_attrs["price"], product_attrs["id"])
        product_id = self._product_editor.store(product)
        return product_id

    def _fetch_product(self, product_id):
        """
        :type product_id: str
        :rtype: bakery.product_model.Product
        """
        return self._product_editor.fetch(product_id)

    def _support_following_product_attrs(self):
        self._reqparse = reqparse.RequestParser()
        self._reqparse.add_argument('id', type=str, location='json')
        self._reqparse.add_argument('name', type=str, location='json')
        self._reqparse.add_argument('price', type=str, location='json')
