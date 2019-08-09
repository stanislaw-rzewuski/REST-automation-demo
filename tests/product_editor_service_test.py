import unittest

from bakery.product_editor import ProductEditor
from bakery.product_editor_service import ProductEditorWebService
from bakery.product_model import Product
from flask import Flask, json
from mock import Mock
from product_utils import assert_product


class ProductEditorServiceTest(unittest.TestCase):
    def setUp(self):
        flask = Flask(__name__)
        self._product_editor_app = flask.test_client(self)
        self._product_editor = Mock(ProductEditor)
        ProductEditorWebService.init_service(self._product_editor, flask)

    def test_getting_product(self):
        self._product_editor.fetch = Mock(return_value=Product("Bread", "3.45", "1"))
        response = self._product_editor_app.get("/products/1")
        self.assertEqual({"id": "1", "name": "Bread", "price": "3.45"}, json.loads(response.data))

    def test_posting_product(self):
        self._product_editor.store = Mock(return_value="1")
        response = self._product_editor_app.post("/products", data=json.dumps({"name": "Bread", "price": "3.45", "id": ""}))
        self.assertEqual({"id": "1"}, json.loads(response.data))

    def test_posting_job(self):
        self._product_editor.store = Mock(return_value=None)
        self._product_editor_app.post("/products", data=json.dumps({"name": "Bread", "price": "3.45", "id": ""}),
                                      content_type="application/json")
        assert_product(self, ["Bread", "3.45", ""], self._product_editor.store.call_args[0][0])


if __name__ == '__main__':
    unittest.main()
