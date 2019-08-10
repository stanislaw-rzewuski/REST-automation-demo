from abc import ABCMeta, abstractmethod


class Products:
    def __init__(self):
        self._products = []

    def get(self, product_id):
        """
        :type product_id: str
        :rtype: Product
        """
        return next(product for product in self._products if product.get_id() == product_id)

    def append(self, product):
        """
        :type product: Product
        """
        self._products.append(product)

    def save(self, product):
        """
        :type product: Product
        """
        if self._exists(product):
            self._update(product)
        else:
            self.append(product)

    def size(self):
        """
        :rtype: int
        """
        return len(self._products)

    def _update(self, product):
        """
        :type product: Product
        """
        self._products.remove(self.get(product.get_id()))
        self.append(product)

    def _exists(self, product):
        """
        :type product: Product
        """
        return any(product.get_id() == p.get_id() for p in self._products)

    def __iter__(self):
        return self._products.__iter__()


class Product:
    def __init__(self, name, price, p_id=""):
        """
        :type name: str
        :type price: str
        :type p_id: str
        """
        self._name = name
        self._price = price
        self._p_id = p_id
        pass

    def get_id(self):
        """
        :rtype: str
        """
        return self._p_id

    def get_name(self):
        """
        :rtype: str
        """
        return self._name

    def get_price(self):
        """
        :rtype: str
        """
        return self._price

    def as_dict(self):
        """
        :rtype: dict[str, str]
        """
        return {"id": self._p_id, "name": self._name, "price": self._price}


class ProductGateway:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def find_all(self):
        """
        :rtype: Products
        """
        pass

    @abstractmethod
    def find(self, product_id):
        """
        :type product_id: str
        :rtype: Product
        """
        pass

    @abstractmethod
    def save(self, product):
        """
        :type product: Product
        :rtype: bool
        """
        pass
