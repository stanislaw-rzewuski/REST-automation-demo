import json

class Product:
    def __init__(self, productId, name, price):
        self.productId = productId
        self.name = name
        self.price = price

    def __str__(self):
        return '{{"id" = "{0}","name" = "{1}", "price" = {2}}}'.format(self.productId, self.name, self.price)

    # def get_productId(self):
    #     return self._productId
    #
    #     # setter method
    #
    # def set_productId(self, x):
    #     self._productId = x

def obj_creator(d):
    return Product(d['id'], d['name'], d['price'])


# with open('/home/stan/repos/Vonage_Python/bakery/bakery_tests/venv/sample.json', 'r') as fp:
#     # data = fp.read()
#     # obj = json.load(data, object_hook=obj_creator)
#     obj = json.load(fp, object_hook=obj_creator)
# print obj
