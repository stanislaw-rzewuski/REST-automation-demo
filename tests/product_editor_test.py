import unittest

from mock import Mock

from bakery.product_editor import ProductEditor
from bakery.product_model import Product, ProductGateway
from product_utils import assert_product


class ProductEditorTest(unittest.TestCase):
    def setUp(self):
        self._product_gateway = ProductEditorTest.ProductGatewayFake()
        self._product_editor = ProductEditor(self._product_gateway)

    def test_can_deliver_product(self):
        self._product_gateway.find = Mock(return_value=Product("Bread", "3.45", "1"))
        product = self._product_editor.fetch("1")
        assert_product(self, ["Bread", "3.45", "1"], product)

    def test_can_store_new_product(self):
        self._test_storing_product("1", "Bread", "3.45", "")

    def test_can_store_existing_product(self):
        self._test_storing_product("1", "", "", "")
        self._test_storing_product("1", "Bread", "3.45", "1")

    def test_iterates_product_id_by_one_for_every_new_product(self):
        self._test_storing_product("1", "", "", "")
        self._test_storing_product("2", "", "", "")

    def _test_storing_product(self, expected_new_id, product_name, product_price, product_id):
        product_new_id = self._product_editor.store(Product(product_name, product_price, product_id))
        assert_product(self, [product_name, product_price, expected_new_id], self._product_editor.fetch(product_new_id))
        self.assertEqual(expected_new_id, product_new_id)

    class ProductGatewayFake(ProductGateway):
        def __init__(self):
            self._product = Product("", "", "")

        def find_all(self):
            pass

        def find(self, product_id):
            return self._product

        def save(self, product):
            self._product = product
            return True


if __name__ == '__main__':
    unittest.main()
