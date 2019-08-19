import json
import re
import product


def compareFiles(file1,file2):
        print file1
        print file2
        filename1 = file1
        filename2 = file2

        print "Comparing difference between file: %s and %s" % (filename1, filename2)
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
                            # assert_flag_file = 1
                            return True
                        else:
                            print file1list[index] + "!= " + file2list[index] + " Not-Equel"
                            # assert_flag_file = 0
                            return False
                else:
                    print "difference in the size of the file and number of lines"

#
def compareProductObjects(object_1,object_2):
         # if obj == obj_ref:
         # check if the object_1 and object_2 are the same instance of product class
        if object_1.__eq__(object_2):
            print "objects are EQUAL !"
            return True
        else:
            print "objects are NOT equal"
            return False
#
def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj]
#
def create_obj_from_json(json_filename, object_hook):
        print "creating object from filename %s" %json_filename
        tmp = re.split("/", object_hook.func_code.co_filename)
        tmp2 = tmp[len(tmp)-1]
        classname= re.split("\.", tmp2)[0]

        object_hook_used = classname +"."+ object_hook.func_code.co_name
        print "obj_hook used for creating object %s" %object_hook_used

        with open(json_filename, 'r') as f:
            reference_json_obj = json.load(f)
            # obj_ref = json.loads(json.dumps(reference_json_obj, sort_keys=True),object_hook=product.obj_creator)  # tyle zachodu by miec objekt o tej samej strukturze co
            object_from_file  = json.loads(json.dumps(reference_json_obj, sort_keys=True),object_hook=object_hook)  # tyle zachodu by miec objekt o tej samej strukturze co
            return object_from_file

#
def create_obj_from_resopnse(response,obj_hook):
    json_data = json.loads(response.text)
    print("The response contains {0} properties".format(len(json_data)))
    print("\n")
    obj = []
    for iterator in json_data:
        obj.append(json.loads(json.dumps(iterator, sort_keys=True), object_hook=obj_hook))
    return obj
#
def write_obj_to_csv_file(filename,obj):
    for i in obj:
        filename.write("%s , %s, %s \r\n" % (str(i.product_id), str(i.name), str(i.price)))
    print "--------- end of processing object with results data  ----------"
    filename.close()
    pass
#

def write_obj_to_json_file(filename,obj):
    filename.write("[\r\n")
    k = 0
    for i in obj:
        k = k + 1
        if (k == len(obj)):
            filename.write("%s \r\n" % (str(i).replace("=", ":")))
        else:
            filename.write("%s, \r\n" % (str(i).replace("=", ":")))
    print "--------- end of processing object with results data  ----------"
    filename.write("]\r\n")
    filename.close()
    pass
#