import unittest
from os import remove

from bakery.product_file_db import ProductFileDb
from bakery.product_model import Product
from product_utils import assert_product, assert_products


class ProductFileDbTest(unittest.TestCase):
    _PRODUCT_FILE_DB_LOCATION = "product_test_db"

    def setUp(self):
        self._product_file_db = ProductFileDb(ProductFileDbTest._PRODUCT_FILE_DB_LOCATION)

    def tearDown(self):
        remove(ProductFileDbTest._PRODUCT_FILE_DB_LOCATION)

    def test_can_find_products(self):
        self._test_finding_products([["Bread", "3.45", "1"]])
        self._test_finding_products([["Bun", "1.23", "1"], ["Bread", "3.45", "2"]])

    def test_can_find_product_by_id(self):
        self._test_finding_product("Bread", "3.45", "1")

    def test_can_add_product(self):
        init_db = []
        to_add = Product("Bread", "3.45", "1")
        expected_db = [["Bread", "3.45", "1"]]

        self._test_saving_product(init_db, to_add, expected_db)

    def test_can_update_product(self):
        init_db = [["Bread", "3.45", "1"]]
        to_update = Product("Ray Bread", "5.67", "1")
        expected_db = [["Ray Bread", "5.67", "1"]]

        self._test_saving_product(init_db, to_update, expected_db)

    def test_can_update_product_among_many(self):
        init_db = [["Bread", "3.45", "1"], ["Bun", "1.23", "2"]]
        to_update = Product("Ray Bread", "5.67", "1")
        expected_db = [["Ray Bread", "5.67", "1"], ["Bun", "1.23", "2"]]

        self._test_saving_product(init_db, to_update, expected_db)

    def _test_finding_product(self, product_name, product_price, product_id):
        ProductFileDbTest._fill_db([[product_name, product_price, product_id]])
        actual_product = self._product_file_db.find(product_id)
        assert_product(self, [product_name, product_price, product_id], actual_product)

    def _test_finding_products(self, expected_products_attrs):
        """
        :param expected_products_attrs: [[product_name, product_price, product_id], ...]
        :type expected_products_attrs: list[list[str]]
        """
        ProductFileDbTest._fill_db(expected_products_attrs)
        actual_products = self._product_file_db.find_all()
        assert_products(self, expected_products_attrs, actual_products)

    def _test_saving_product(self, init_db, to_save, expected_db):
        """
        :param init_db: [[product_name, product_price, product_id], ...]
        :param expected_db: [[product_name, product_price, product_id], ...]
        :type init_db: list[list[str]]
        :type to_save: bakery.product_model.Product
        :type expected_db: list[list[str]]
        """
        ProductFileDbTest._fill_db(init_db)
        self._product_file_db.save(to_save)
        assert_products(self, expected_db, self._product_file_db.find_all())

    @staticmethod
    def _fill_db(products_attrs):
        """
        :param products_attrs: [[product_name, product_price, product_id], ...]
        :type products_attrs: list[list[srt]]
        """
        with open(ProductFileDbTest._PRODUCT_FILE_DB_LOCATION, "w") as db:
            for product_attr in products_attrs:
                entry = "{0}{3}{1}{3}{2}{4}".format(product_attr[2], product_attr[0], product_attr[1],
                                                    ProductFileDb._ENTRY_ATTR_SEPARATOR,
                                                    ProductFileDb._ENTRY_END)
                db.write(entry)


if __name__ == '__main__':
    unittest.main()
