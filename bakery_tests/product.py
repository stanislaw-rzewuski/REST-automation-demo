class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return '{{"id" = "{0}","name" = "{1}", "price" = {2}}}'.format(self.product_id, self.name, self.price)

    def __eq__(self, other):
        if not isinstance(other, Product):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return (
                self.__class__ == other.__class__ and
                self.product_id == other.product_id and
                self.name == other.name and
                str(self.price) == str(other.price)
        )


def obj_creator(d):
    return Product(d['id'], d['name'], d['price'])
