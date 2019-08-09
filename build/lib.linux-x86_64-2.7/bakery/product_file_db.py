import os

from product_model import ProductGateway, Products, Product


class ProductFileDb(ProductGateway):
    _ID_ATTR_IDX = 0
    _NAME_ATTR_IDX = 1
    _PRICE_ATTR_IDX = 2
    _ENTRY_ATTR_SEPARATOR = "!@#"
    _ENTRY_END = "\n"

    def __init__(self, product_db_location):
        """
        :type product_db_location: str
        """
        super(ProductFileDb, self).__init__()
        self._product_db_location = product_db_location

    def find_all(self):
        """
        :rtype: bakery.product_model.Products
        """
        if self._is_db_present():
            return Products()

        return self._read_all()

    def find(self, product_id):
        """
        :type product_id: str
        :rtype: bakery.product_model.Product
        """
        return self.find_all().get(product_id)

    def save(self, product):
        """
        :type product: bakery.product_model.Product
        :rtype: bool
        """
        return self._try_write_to_db(product)

    def _is_db_present(self):
        return not os.path.exists(self._product_db_location)

    def _read_all(self):
        """
        :rtype: bakery.product_model.Products
        """
        with open(self._product_db_location) as db:
            products = Products()
            for entry in db.readlines():
                products.append(ProductFileDb._convert_to_product(entry))
            return products

    def _try_write_to_db(self, product):
        """
        :type product: bakery.product_model.Product
        :rtype bool
        """
        try:
            self._write_to_db(product)
            return True
        except IOError:
            return False

    def _write_to_db(self, product):
        """
        :type product: bakery.product_model.Product
        """
        products = self.find_all()
        products.save(product)

        with open(self._product_db_location, "w") as db:
            for product in products:
                db.write(ProductFileDb._convert_to_db_entry(product))

    @staticmethod
    def _convert_to_db_entry(product):
        """
        :type product: bakery.product_model.Product
        """
        return "{0}{3}{1}{3}{2}{4}".format(product.get_id(), product.get_name(), product.get_price(),
                                           ProductFileDb._ENTRY_ATTR_SEPARATOR,
                                           ProductFileDb._ENTRY_END)

    @staticmethod
    def _convert_to_product(db_product_entry):
        """
        :type db_product_entry: str
        :rtype: bakery.product_model.Product
        """
        product_attrs = ProductFileDb._extract_product_attrs(db_product_entry)
        return Product(product_attrs[ProductFileDb._NAME_ATTR_IDX], product_attrs[ProductFileDb._PRICE_ATTR_IDX],
                       product_attrs[ProductFileDb._ID_ATTR_IDX])

    @staticmethod
    def _extract_product_attrs(db_product_entry):
        """
        :type db_product_entry: str
        :rtype: list[str]
        """
        return db_product_entry.rstrip(ProductFileDb._ENTRY_END).split(ProductFileDb._ENTRY_ATTR_SEPARATOR)
