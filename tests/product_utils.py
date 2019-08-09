from bakery.product_model import Products, Product


def create_products(products_attrs):
    """
    :param products_attrs: [[product_name, product_price, product_id], ...]
    :type products_attrs: list[list[str]]
    :rtype: bakery.product_model.Products
    """
    products = Products()
    for p_attrs in products_attrs:
        products.append(Product(p_attrs[0], p_attrs[1], p_attrs[2]))

    return products


def assert_products(test_case, expected_products_attrs, actual_products):
    """
    :param expected_products_attrs: [[product_name, product_price, product_id], ...]
    :type test_case: unittest.TestCase
    :type expected_products_attrs: list[list[str]]
    :type actual_products: bakery.product_model.Products
    """
    test_case.assertEqual(len(expected_products_attrs), actual_products.size())
    for expected_product_attrs in expected_products_attrs:
        assert_product(test_case, expected_product_attrs, actual_products.get(expected_product_attrs[2]))


def assert_product(test_case, expected_product_attrs, actual_product):
    """
    :param expected_product_attrs: [product_name, product_price, product_id]
    :type test_case: unittest.TestCase
    :type expected_product_attrs: list[str]
    :type actual_product: bakery.product_model.Product
    """
    test_case.assertEqual(expected_product_attrs[0], actual_product.get_name())
    test_case.assertEqual(expected_product_attrs[1], actual_product.get_price())
    test_case.assertEqual(expected_product_attrs[2], actual_product.get_id())
