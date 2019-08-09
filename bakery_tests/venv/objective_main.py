import json


class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def __str__(self):
        return '{{"firstName" = "{0}","lastName" = "{1}", "age" = {2}}}'.format(self.firstName, self.lastName, self.age)


def obj_creator(d):
    return Person(d['firstName'], d['lastName'], d['age'])


with open('/home/stan/repos/Vonage_Python/bakery/bakery_tests/venv/samplePerson.json', 'r') as fp:
    obj = json.load(fp, object_hook=obj_creator)

print obj


