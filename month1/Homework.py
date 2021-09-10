#________________________________________-Problem 1-___________________________
import json

jobj_dict =  '{"name": "David", "age": 6, "class": "I"}'

jobj_list =   '["Red", "Green", "Black"]'

jobj_string = '"Python Json"'

jobj_int = '1234'

jobj_float =  '21.34'

json.dumps(jobj_dict, indent=3)

with open("Myjson.json", "w") as file:
    file.write(jobj_dict)
    file.close()

with open("Myjson.json", "r") as f:
    dataa = f.read()
    print(json.loads(dataa))
    print(type(json.loads(dataa)))


json.dumps(jobj_list, indent=3)

with open("Myjson1.json", "w") as file1:
    file1.write(jobj_list)
    file1.close()

with open("Myjson1.json", "r") as s:
    dataa1 = s.read()
    print(json.loads(dataa1))
    print(type(json.loads(dataa1)))


with open("Myjson2.json", "w") as file2:
    file2.write(jobj_string)
    file2.close()

with open("Myjson2.json", "r") as d:
    dataa2 = d.read()
    print(json.dumps(dataa2))
    print(type(json.dumps(dataa2)))


with open("Myjson3.json", "w") as file3:
    file3.write(jobj_int)
    file3.close()

with open("Myjson3.json", "r") as g:
    dataa3 = g.read()
    print(json.loads(dataa3))
    print(type(json.loads(dataa3)))


with open("Myjson4.json", "w") as file4:
    file4.write(jobj_float)
    file4.close()

with open("Myjson4.json", "r") as h:
    dataa4 = h.read()
    print(json.loads(dataa4))
    print(type(json.loads(dataa4)))


#________________________________________-Problem 2-______________________________________________________
