from product_model import Product


class ProductEditor:
    def __init__(self, product_gateway):
        """
        :type product_gateway: product_model.ProductGateway
        """
        self._product_gateway = product_gateway
        self._product_count = 0

    def fetch(self, product_id):
        """
        :type product_id: str
        :rtype: product_model.Product
        """
        return self._product_gateway.find(product_id)

    def store(self, product):
        """
        :type product: product_model.Product
        :rtype: str
        :returns product_id or empty string if failed to store
        """
        product_to_save = self._fill_with_id_if_new(product)
        return product_to_save.get_id() if self._product_gateway.save(product_to_save) else ""

    def _fill_with_id_if_new(self, product):
        """
        :type product: bakery.product_module.Product
        :rtype: bakery.product_module.Product
        """
        return self._fill_with_id(product) if ProductEditor._is_new(product) else product

    def _fill_with_id(self, product):
        """
        :type product: bakery.product_model.Product
        :rtype: bakery.product_model.Product
        """
        self._product_count += 1
        return Product(product.get_name(), product.get_price(), str(self._product_count))

    @staticmethod
    def _is_new(product):
        return product.get_id() == ""
