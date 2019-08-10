import os

from flask import Flask, json

from product_editor import ProductEditor
from product_editor_service import ProductEditorWebService
from product_file_db import ProductFileDb
from product_overview import ProductOverview
from product_overview_service import ProductOverviewWebService, NewestProductIdWebService


def create_flask():
    return Flask(__name__)


def create_product_file_db(path_to_db):
    """
    :rtype: bakery.product_model.ProductFileDb
    """
    return ProductFileDb(path_to_db)


def create_product_overview(product_gateway, flask):
    """
    :type product_gateway: bakery.product_model.ProductGateway
    :type flask: flask.Flask
    """
    product_overview = ProductOverview(product_gateway)
    ProductOverviewWebService.init_service(product_overview, flask)
    NewestProductIdWebService.init_service(product_overview, flask)


def create_product_editor(product_gateway, flask):
    """
    :type product_gateway: bakery.product_model.ProductGateway
    :type flask: flask.Flask
    """
    product_editor = ProductEditor(product_gateway)
    ProductEditorWebService.init_service(product_editor, flask)


def fill_db_with_sample_product(flask):
    """
    :type flask: flask.Flask
    """
    service = flask.test_client()
    service.post("/products", data=json.dumps({"name": "Bread", "price": "3.45", "id": ""}),
                 content_type="application/json")


app = create_flask()
product_file_db = create_product_file_db(os.path.abspath("product_db"))

create_product_overview(product_file_db, app)
create_product_editor(product_file_db, app)

fill_db_with_sample_product(app)
