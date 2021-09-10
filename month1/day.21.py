import json

# myjson = {
#     "name":"Anna",
#     "age":17,
#     "gender":"female"
# }
# print(len(myjson))
# print(myjson["age"])

# mydict = """{
#     "name":"Anna",
#     "age":17,
#     "gender":"female"
# }"""

# pyobj = json.loads(mydict)
# print(pyobj)
# print(type(pyobj))

# json_obj = json.dumps(myjson)
# print(json_obj)
# print(type(json_obj))


# dd = {
#     "имя":"Саня",
#     "возраст":28,
#     "пол":"мужской"
# }

# #dump()
# with open("data.json", "w")as f:
#     #data = json.dump(myjson, f)
#     data2 = json.dump(dd, f, ensure_ascii=False, indent=2)

# with open("data.json", "r")as f:
#     print(f.read())
#     print(type(myjson))


# with open("data.json", "r") as f:
#     data3 = json.load(f)


# print(data3)

# data = 0
# def searchcallcode(country):
#     with open("country-by-calling-code.json", "r") as ff:
#         data = json.load(ff)
#         # print(data)
#         for i in data:
#             if i["country"] == country:
#                 print(i["calling_code"])
#             else:
#                 print("Not found country")
#                 break

# int_data = input("Input country's name: ").title()
# searchcallcode(int_data)

# def searchcallcode(country):
#     with open("country-by-calling-code.json", "r") as ff:
#         data = json.load(ff)
#         cou = []
#         for c in data:
#             cou.append(c["country"])

#         if country in cou:
#             for i in data:
#                 if i["country"] == country:
#                     print(f'Calling code of {country} is {i["calling_code"]}')


# int_data = input("Input country's name: ").title()
# searchcallcode(int_data)


# data_dict = {}
# name = input("Введите ваше имя: ")
# sourn = input("Введите ваше фамилие: ")
# email = input("Введите вашу почту: ")
# login = input("Теперь ваш логин: ")
# age = input("Введите ваш возраст: ")


# data_dict["name"] = name
# data_dict[" фамилие"] = sourn
# data_dict["почта"] = email
# data_dict["логин"] = login
# data_dict["Возраст"] = age
# # print(data_dict)

# with open("info.json", "w") as f:
#     info = json.dump(data_dict, f, ensure_ascii=False, indent=3)

# with open("info.json", "r") as f:
#     # print(json.load(data_dict))
#     print(f.read())

#frozenset

# a = [54, 65, 8]
# tup = [54, 68, 74]

# mset = {58, 8, 96, 8, 5}
# print(len(mset))

# mset.add(58)
# mset.add(57)
# print(len(mset))

# fr = frozenset({3, 4, 55, 7, 1, 3})
# print(fr)
# print(len(fr))



# for i in range(10):
#     print(i, end="\t") #горизонтальный

# for i in range(10):
#     print(i, end="\n") #вертикальный

# for i in range(10):
#     print(i)

# for i in range(10):
#     print(i, end=" ") #пробел 

# l = [54, 658, 87, 54, 321, 58]
# print(*l, sep="---")



#рекурсивная функция эта та которая вызывает само себя

def main():
    print("Hello")
    test()


def test():
    print("Test")

main() #Hello
       #Test


def recurs(n):
    if n == 1:
        return 1
    else:
        return n*recurs(n-1)

# print(recurs(5))
# print(recurs(6))

#"""reques""" - запросы

