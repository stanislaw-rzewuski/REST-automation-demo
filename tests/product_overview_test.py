import unittest

from bakery.product_model import ProductGateway
from bakery.product_overview import ProductOverview
from mock import Mock
from product_utils import create_products, assert_products


class ProductOverviewTest(unittest.TestCase):
    def setUp(self):
        self._product_gateway = Mock(ProductGateway)
        self._product_overview = ProductOverview(self._product_gateway)

    def test_can_deliver_products(self):
        self._test_fetching_products([["Bread", "3.45", "1"]])
        self._test_fetching_products([["Rye Bread", "2.45", "1"], ["Bun", "1.23", "2"]])

    def test_can_find_last_added_product_id(self):
        self._product_gateway.find_all = Mock(return_value=create_products([["Bread", "3.45", "1"], ["Bun", "3.45", "2"]]))
        newest_product_id = self._product_overview.find_newest_id()
        self.assertEqual("2", newest_product_id)

    def _test_fetching_products(self, expected_products_attrs):
        """
        :param expected_products_attrs: [[product_name, product_price, product_id], ...]
        :type expected_products_attrs: list[list[str]]
        """
        self._product_gateway.find_all = Mock(return_value=(create_products(expected_products_attrs)))
        actual_products = self._product_overview.fetch()
        assert_products(self, expected_products_attrs, actual_products)

if __name__ == '__main__':
    unittest.main()
