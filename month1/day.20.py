# spisoc1 = ('lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
# spisoc2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)

# # for i, j in zip(spisoc1, spisoc2):
# #     print(i, j)

# res = []
# for i in spisoc2:
#     if i in spisoc1:
#         continue
#     else:
#         res.append(i)
# print(*res)






# """JSON, JavaSkript objekt"""
# import json
# """dump, dumps, load"""




# dict2 = "name: Nurbek"

# with open("data.json", "w") as mydata:
#     mydata.write(dict2)
#     mydata.close()

# with open("data.json", "r") as f:
#     print(f.read())

# dict1 = {
#     "name":"Nubik",
#     "sourname":"Kalushev",
#     "age":18
# }

# print(dict1["name"])
# print(json.dumps(dict1))
# jsondata = json.dumps(dict1)
# # print(jsondata["name"])
# print(type(jsondata))

# with open("data.json", "w") as file:
#     file.write(jsondata)
#     file.close()

# with open("data.json", "r") as f:
#     print(f.read())

# mydict = {
#     "Имя":"Нурбик",
#     "Фамилие":"Калышев",
#     "Отчество":"Калышев",
#     "Возраст":"18"
# }

# jsoninfo = json.dumps(mydict, ensure_ascii = False, indent=4)

# with open("data2.json", "w") as file:
#     file.write(jsoninfo)
#     file.close()
# with open("data2.json", "r") as f:
#     dataa = f.read()
#     print(dataa)
#     print(json.loads(dataa))
#     print(type(json.loads(dataa)))

# import json

# x2 = '{"name":"John", "age":"30", "city":"New York"}'

# x = """{
#         "name":"John", 
#         "age":"30", 
#         "city":"New York"
#     }"""

# # jsonopen =  json.dumps(x, ensure_ascii=False, indent=3)

# print(json.loads(x2)["age"])
# print(json.loads(x)["age"])
# # print(jsondata["name"])

# with open("dada.json", "w") as file:
#     file.write(jsonopen)
#     file.close()

# with open("dada.json", "r") as f:
#     dataa = f.read()
#     print(dataa)
#     print(json.loads(dataa))
#     print(type(json.loads(dataa)))


import json

# python = {
#     "name":"Давид",
#     "class":"I",
#     "age":"6"
# }

# jsonapp = json.dumps(python, ensure_ascii=False, indent=3)

# with open("dada.json", "w") as file:
#     file.write(jsonapp)
#     file.close()

# with open("dada.json", "r") as f:
#     dataa = f.read()
#     print(dataa)
#     print(json.dumps(dataa))
#     print(type(json.dumps(dataa)))

python_obj = {
  "name": "Давид",
  "class":"I",
  "age": 6  
}


python_dict =  {"name": "David", "age": 6, "class":"I"}



with open("MyJSON.json", "w") as myFile:
    json.dump(python_dict, myFile, indent=2)

python_list =  ["Red", "Green", "Black"]
python_str =  "Python Json"
python_int =  (1234)
python_float =  (21.34)
python_T =  (True)
python_F =  (False)
python_N =  (None)
python_dict =  {"name": "David", "age": 6, "class":"I"}
def main(python_obj):
    with open("MY.json", "w") as ff:
        json.dump(python_list, ff, indent=2, sort_keys=True)
main(python_list)


with open("MyJSON.json", "r") as dd:
    pyth_obj = json.load(dd)
print(python_obj)
print(type(python_obj))

