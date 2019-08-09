# coding=utf-8
# US 1. As a bakery owner, I can add a bakery good to let the customers see what is currenlty fresh in sell.
# Conditions of satisfaction: Can I store product’s name and price?

# Czy tu chodzi by napisać test automatyczny jaki tworzy podukty (albo za hardcodowane albo z pliku tekstowego (CSV) ) i potem odpytuj
# sklep i zapisuje produkty do pliku tekstowego /CSV, który ma w sobie: id/ produkt / cenę produktu
# na przykład:
# 1,Bread,3.45
# None,None,None <- tak aplikacja pozwala na dodanie pustego produktu :-) babbol
# 3,bun,1.2,

# US 2. As a bakery customer, I can view all the fresh bakery goods in sell to step in.
# Conditions of satisfaction: Can I see product’s price?
# Czy tu mam pobrać listę produktów i ich ceny i wpisać do pliku/wyświetlić?

# US 3. As a bakery customer, I can check what is the most fresh bakery good right now in sell.
# Czy tu chodzi by wyświetlić to zwraca  request: http://127.0.0.1:5000/products/newest_id
# Niestety jak dodam coś bez nazwy (pusty JSON  w requeście: POST http://127.0.0.1:5000/products {}
# to wyświetla się None :-) - chyba kolejny babol - ale az mam go ochotę naprawić ;-)


# importing the requests library
import json

import pandas
import requests
import product


# api-endpoint's
product_id=1
url_get_products = "http://127.0.0.1:5000/products"
url_get_newest_id_products = "http://127.0.0.1:5000/products/newest_id"
url_get_products_with_id = "http://127.0.0.1:5000/products/"+str(product_id)

url_add_products = "http://127.0.0.1:5000/products" #here json has to be attached as object


# 1. get products and write the to file as json and as CSV.file

# sending get request and saving the response as
response = requests.get(url=url_get_products)

# extracting data in json format
data = response.json()

# df = pandas.read_json("/home/stan/repos/Vonage_Python/bakery/bakery_tests/venv/local/stackedSample.json")
# df = pandas.read_json(str(myResponse.text))
# If you are not familiar with pandas, here a quick headstart, how to work with a dataframe object:
# print df.head() #gives you the first rows of the dataframe
# print df["name"] # gives you the column review_id as a vector
# print df.iloc[1,:] # gives you the complete row with index 1
# print df.iloc[1,2] # gives you the item in row with index 1 and column with index 2

if response.ok:
    print "code:" + str(response.status_code)
    print "header:" + str(response.headers)

    # Loading the response data into a dict variable
    # json.loads takes in only binary or string variables so using content to fetch binary content
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    # jsonData = json.loads(myResponse.content)

    jsonData = json.loads(response.text)

    print("The response contains {0} properties".format(len(jsonData)))
    print("\n")
    # print "MyReposnse " + str(myResponse.text) # to wypluwa ładnego json
    # print "\n"

    # for distro in jsonData:
    #     print(distro['id'])
    a=[]
    obj = []
    for iterator in jsonData:
        # print "iterator" +str(iterator)
        # print "-------------------"
        # print "id " + iterator['id']  # str(iterator)
        # print "name " + iterator['name']  # str(iterator)
        # print "price " + iterator['price']  # str(iterator)
        # print "-------------------"
        # obj = json.load(iterator, object_hook=product.obj_creator)

        # obj= json.loads(json.dumps(iterator, sort_keys=True), object_hook=product.obj_creator)
        obj.append(json.loads(json.dumps(iterator, sort_keys=True), object_hook=product.obj_creator))
        # print obj
        # a.append(obj)
        # print(iterator['id'])
        # print("name %s: id %d" %iterator['name'], iterator['id'])
        # print "id" +jsonData.
        # print "name" +jsonData
        # print "price" + jsonData
        # print key
else:
    # If response code is not ok (200), print the resulting http error code with description
    response.raise_for_status()

# wrtite results to file in CSV format
csvfile = open("results.csv","w+")
jsonfile = open("results.json","w+")
jsonfile.write("[\r\n")
k=0
for i in obj:
    csvfile.write("%s , %s, %s \r\n" % ( str(i.productId), str(i.name), str(i.price)  ) )
    # jsonfile.write("%s \r\n" %json.dumps(str(i)))
    k=k+1
    if (k==len(obj)):

        jsonfile.write("%s \r\n" % (str(i).replace("=", ":")))
    else:
        jsonfile.write("%s, \r\n" % ( str(i).replace("=",":") ) )
print "-------------------"
jsonfile.write("]")
jsonfile.close
csvfile.close()

