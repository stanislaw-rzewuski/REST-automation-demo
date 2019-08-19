# coding=utf-8
# US 1. As a bakery owner, I can add a bakery good to let the customers see what is currenlty fresh in sell.
# Conditions of satisfaction: Can I store product’s name and price?

# Czy tu chodzi by napisać test automatyczny jaki tworzy podukty
# (albo za hardcodowane albo z pliku tekstowego (CSV) ) i potem odpytuje
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
import sys
import requests
import product
import tools

# api-endpoint's
product_id = 1
url_get_products = "http://127.0.0.1:5000/products"
url_get_newest_id_products = "http://127.0.0.1:5000/products/newest_id"
url_get_products_with_id = "http://127.0.0.1:5000/products/" + str(product_id)

url_add_products = "http://127.0.0.1:5000/products"  # here json has to be attached as object

# 1. get products and write the to file as json and as CSV.file

# sending get request and saving the response as
try:
    response = requests.get(url=url_get_products)
except:
    sys.exit("HTTP Response is not 200=OK -  Exiting !!!")
else:
    print "Response received with 200=OK"

# process_reposnse()
# extracting data in json format
data_in_response = response.json()

if response.ok:
    print "code:" + str(response.status_code)
    print "header:" + str(response.headers)
    obj = tools.create_obj_from_resopnse(response,product.obj_creator)

else:
    # If response code is not ok (200), print the resulting http error code with description
    response.raise_for_status()
    sys.exit("aa!Response is not 200 Exiting ")

# wrtite results to file in CSV format

csv_filename = open("results.csv", "w+")
json_filename = open("results.json", "w+")

tools.write_obj_to_csv_file(csv_filename,obj)
tools.write_obj_to_json_file(json_filename,obj)

# pliki json i csv mają to co jest w piekarni bakery - teraz pobierzmy dane z pliku jaki uzywa piekarnia i porównajmy

file_with_reference_data = open("/home/stan/repos/REST-automation-demo/bakery/product_db", "r")
reference_csv_file = open("reference_product_data.csv", "w+")
reference_json_file = open("reference_product_data.json", "w+")
reference_json_file.write("[\r\n")
kk = 0

for line in file_with_reference_data:
    fields = line.split("!@#") # file separator !@#
    # and let's extract the data:
    ref_product_id = fields[0]
    ref_product_name = fields[1]
    ref_product_price = fields[2].replace("\n", "")
    reference_csv_file.write("%s , %s, %s \r\n" % (ref_product_id, ref_product_name,ref_product_price))  # zagatka czemu w jednej pętli musz zrobic \r\n a w drugie musze to wywalic !!! pewnie w ostatniej zmiennej wczytujemy znak konca lini - no kurwa co za lamerstwo pythonowe
    kk = kk + 1
    if (kk != len(obj)):
        reference_json_file.write("{\"id\" : \"%s\",\"name\" : \"%s\", \"price\" : %s}, \r\n" % (ref_product_id, ref_product_name, ref_product_price))
    else:
        reference_json_file.write("{\"id\" : \"%s\",\"name\" : \"%s\", \"price\" : %s} \r\n" % (ref_product_id, ref_product_name, ref_product_price))

reference_json_file.write("]")
reference_json_file.close()
print "--------- end of processing reference file ----------"
file_with_reference_data.close()
reference_csv_file.close()

# porównanie plików :) - brzmi jak proste rozwiazanie - ale czy najlepsze

csv_file = "results.csv"
reference_csv_file = "reference_product_data.csv"
# porownanie plikow
if tools.compareFiles(csv_file,reference_csv_file) == True:
    assert_flag_file = 1
    print "Files are the same"
else:
    assert_flag_file = 0
    print "Files are NOT the same"


# porównanie dwóch obiektów - to intelektualnie dobry wariant treningowy
assert_flag_object = 0
reference_json_file = "reference_product_data.json"

reference_json_obj = []
print "comparing obejcts"
obj_ref = tools.create_obj_from_json(reference_json_file, product.obj_creator)

if obj == obj_ref:
    print "objects are the same"
    print  obj.__eq__(obj_ref)
    assert_flag_object =1
else:
    print "objects are NOT the same"
    print  obj.__eq__(obj_ref)
    assert_flag_object = 0

print "End of Program"
