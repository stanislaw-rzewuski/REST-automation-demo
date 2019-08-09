class ProductOverview:
    def __init__(self, product_gateway):
        """
        :type product_gateway: product_model.ProductGateway
        """
        self._product_gateway = product_gateway

    def fetch(self):
        """
        :rtype: product_model.Products
        """
        return self._product_gateway.find_all()

    def find_newest_id(self):
        """
        :rtype: str
        """
        return max(self.fetch(), key=lambda product: product.get_id()).get_id()
