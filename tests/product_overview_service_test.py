import unittest

from bakery.product_overview import ProductOverview
from bakery.product_overview_service import ProductOverviewWebService, NewestProductIdWebService
from flask import Flask, json
from mock import Mock
from product_utils import create_products


class ProductOverviewServiceTest(unittest.TestCase):
    def setUp(self):
        flask = Flask(__name__)
        self._product_overview_app = flask.test_client(self)
        self._product_overview = Mock(ProductOverview)
        ProductOverviewWebService.init_service(self._product_overview, flask)

    def test_getting_products(self):
        self._product_overview.fetch = Mock(return_value=create_products([["Bread", "3.45", "1"]]))
        response = self._product_overview_app.get("/products")
        self.assertEqual([{"name": "Bread", "price": "3.45", "id": "1"}], json.loads(response.data))


class NewestProductIdServiceTest(unittest.TestCase):
    def setUp(self):
        flask = Flask(__name__)
        self._product_overview_app = flask.test_client(self)
        self._product_overview = Mock(ProductOverview)
        NewestProductIdWebService.init_service(self._product_overview, flask)

    def test_getting_newest_product_id(self):
        self._product_overview.find_newest_id = Mock(return_value="1")
        response = self._product_overview_app.get("/products/newest_id")
        self.assertEqual({"id": "1"}, json.loads(response.data))


if __name__ == '__main__':
    unittest.main()
