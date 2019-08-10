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


if response.ok:
    print "code:" + str(response.status_code)
    print "header:" + str(response.headers)

    json_data = json.loads(response.text)

    print("The response contains {0} properties".format(len(json_data)))
    print("\n")
    a=[]
    obj = []
    for iterator in json_data:
        obj.append(json.loads(json.dumps(iterator, sort_keys=True), object_hook=product.obj_creator))

else:
    # If response code is not ok (200), print the resulting http error code with description
    response.raise_for_status()

# wrtite results to file in CSV format
csv_file = open("results.csv", "w+")
json_file = open("results.json", "w+")
json_file.write("[\r\n")
k=0
for i in obj:
    csv_file.write("%s , %s, %s \r\n" % (str(i.productId), str(i.name), str(i.price)))
    # jsonfile.write("%s \r\n" %json.dumps(str(i))) #this works very ppor
    k=k+1
    if (k==len(obj)):
        json_file.write("%s \r\n" % (str(i).replace("=", ":")))
    else:
        json_file.write("%s, \r\n" % (str(i).replace("=", ":")))
print "--------- end of processing object with results data  ----------"
json_file.write("]")
json_file.close
csv_file.close()

# pliki json i csv mają to co jest w piekarni bakery 0 teraz pobierzmy dane z pliku jaki uzywa piekarnia i porównajmy


file_with_reference_data = open("/home/stan/repos/REST-automation-demo/product_db", "r")
reference_csv_file = open("reference_product_data.csv", "w+")
reference_json_file = open("reference_product_data.json", "w+")
# Repeat for each song in the text file
reference_json_file.write("[\r\n")
kk=0

for line in file_with_reference_data:
    # Let's split the line into an array called "fields" using the ";" as a separator:
    fields = line.split("!@#")
    # and let's extract the data:
    ref_product_id = fields[0]
    ref_product_name = fields[1]
    ref_product_price = fields[2].replace("\n","")
    reference_csv_file.write("%s , %s, %s \r\n" % (ref_product_id, ref_product_name, ref_product_price)) # zagatka czemu w jednej pętli musz zrobic \r\n a w drugie musze to wywalic !!! pewnie w ostatniej zmiennej wczytujemy znak konca lini - no kurwa co za lamerstwo pythonowe
    kk = kk + 1
    if (kk != k):
        print "reference json write LAST LINE"
        reference_json_file.write("{\"id\" : \"%s\",\"name\" : \"%s\", \"price\" : %s}, \r\n" % (
        ref_product_id, ref_product_name, ref_product_price))
    else:
        reference_json_file.write( "{\"id\" : \"%s\",\"name\" : \"%s\", \"price\" : %s} \r\n" % (
        ref_product_id, ref_product_name, ref_product_price) )
    #     print "json NOT !!! write"
    #     reference_json_file.write("Problem kurwa, \r\n" )

reference_json_file.write("]")
reference_json_file.close()
print "--------- end of processing reference file ----------"
# It is good practice to close the file at the end to free up resources
file_with_reference_data.close()
reference_csv_file.close()

# porównanie plików :) - brzmi jak proste rozwiazanie - ale czy najlepsze
assert_flag_file =0
csv_file = "results.csv"
reference_csv_file = "reference_product_data.csv"
# porownanie plikow

filename1 = csv_file
filename2 = reference_csv_file

print "Comparing difference between file: %s and %s" %(filename1,filename2)
with open(filename1) as f1:
   with open(filename2) as f2:
      file1list = f1.read().splitlines()
      file2list = f2.read().splitlines()
      list1length = len(file1list)
      list2length = len(file2list)
      if list1length == list2length:
          for index in range(len(file1list)):
              if file1list[index] == file2list[index]:
                  # print file1list[index] + "== " + file2list[index]
                  assert_flag_file = 1
              else:
                  print file1list[index] + "!= " + file2list[index]+" Not-Equel"
                  assert_flag_file = 0
      else:
          print "difference inthe size of the file and number of lines"
if assert_flag_file == 1:
    print "File are the same all ok"
else:
    print "Something went south - oh shyt "


# porównanie dwóch obiektów - to intelektualnie dobry wariant
assert_flag_object =0
reference_json_file = "reference_product_data.json"

reference_json_obj=[]
print "comparing obejcts"

with open(reference_json_file, 'r') as f:
    reference_json_obj = json.load(f)
    obj_ref = json.loads(json.dumps(reference_json_obj, sort_keys=True), object_hook=product.obj_creator) # tyle zachodu by miec objekt o tej samej strukturze co



for i in obj:
     print str(i.productId),str(i.name),str(i.price)

for i in obj_ref:
     print str(i.productId),str(i.name),str(i.price)

print "End of Program"
