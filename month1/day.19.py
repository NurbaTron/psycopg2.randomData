"""Глобальные и локальные переменные"""

# globalvar = 300  #глобальная переменная

# def myFunc(x):   #локальные переменные
#     print(globalvar)
#     print(x)

# myFunc(200)

# num = 0

# def myFunk2(num):
#     print(num)

# myFunk2(56)

# #Math

# l = [524, 65, 85479, 45]
# print(max(l))
# print(min(l))
# print(sum(l))

# import math

# print(math.sqrt(64))
# print(math.sqrt(100))
# print(math.sqrt(81))

# print(math.pi)

# print(math.pow(3, 3))
# print(3 ** 3)
# print(math.ceil(math.pi))
# print(math.floor(math.pi))
# print(math.floor(5.9888))
# print(math.ceil(7))
# print(math.ceil(7.55))

# """split(), join()"""

# mystr = "hello boy, I'm an ice-cream man, and I have an ice-cream for you"
# print(type(mystr))

# lst = mystr.split(",") #из str -> list
# print(type(mystr)) #list
# print(lst)

# # newstr = ",".join(lst)  #из list -> str
# # print(newstr)

# empty = set()
# empty.add("а ещё я полезный")
# empty.add("а ещё я вкусный")
# empty.add("а ещё я красивый")
# empty.add("а ещё у меня странное имя")
# empty.add("дада я знаю")
# newset = ",".join(empty)
# print(newset)

# # режим 
# # «r» - чтение - значение по умолчанию. Открывает файл для чтения, ошибка, если файл не существует

# # «a» - Добавить - открывает файл для добавления, создает файл, если он не существует. И добавит в конец файла

# # «w» - Запись - открывает файл для записи, создает файл, если он не существует.

# # "x" - Создание - Создает указанный файл, возвращает ошибку, если файл существует.


# # myfile = open("NEW.txt", "x")
# myfile2 = open("BLOCK.txt", "w")
# myfile2.write("Python: Hello waawudo")
# myfile2.close

# myfile2 = open("BLOCK.txt", "r")
# print(myfile2.read())

# """with open"""

# with open("BLOCK.txt", "a") as myfile:
#     myfile.write(", IT, Pythob, Django")
#     myfile.write("Kate is my girlfriend, NurbaTron is cool \n")
#     myfile.close

# with open("BLOCK.txt", "r") as my:
#     print(my.read())



# """readlines()"""


# k = ["KONO \n", "DIO \n", "DA \n"]
# with open("ReadLines.txt", "a") as f:
#     f.writelines(k)
#     f.close()

# with open("ReadLines.txt", "r") as f:
#     print(f.readlines())

# with open("ReadLines.txt", "r") as f:
#     #print(f.readlines())
#     for i in f:
#         print(i.strip(), end=" ")


import os
# os.remove("BLOCK.txt")

if os.path.exists("BLOCK.txt"):
    os.remove("BLOCK.txt")
else:
    print("Нету такого файла")

def comands(comand):
    if comand == "touch":
        filename = input("Придумайте имя для папки: ")
        with open(filename, "x"):
            print("готово!")