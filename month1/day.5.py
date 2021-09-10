# sets - множества
# не можем получить элемент по индексу
# не можем удалить элемент
# множество контейнер уникальных и повторяющихся элементов

# st = set()
# st2  = {54, True, "get"}
# lst = [54, 54, True, True, 5, 3, 8, 3]
# umit = set(lst)
# #print(st2[0]) будет ошибка
# print(type(st2))
# st2.add(54) 
# print(st2)
# print(umit)
# print(len(st2)) #получить число элемента в множестве
# # val = {} - dict
# # s = () - tuple
# # lst2 = [] - list
# st - set()
# st.add(True)
# st.add(58)               
# st.add("good") 
# copylst = st.copy() 
# st.remove(58)
# print(st)
# print(copylst)
# st.pop()
# print(st)

# st.discard(777777777777777)

# st.clear()                 #очистка множества
# print(st)


# fset = {54, 96, 78, 22, 36, 4}
# sset = {"set", "dict", "tuple", "list", "str", "int", "float", 4, 96}
# fset.update(sset)
# print(fset)

# # fset.intersection_update(sset)
# # print(fset)

# print(fset.intersection(sset))
# # print(sset.intersection(fset))

# print(fset.difference(sset))
# print(fset - sset)
# print(fset & sset)
# print(fset | sset)
# print(fset ^ sset)


#Problem1

# st = set()
# st2 = {3, 8, 10, 14, 2} 
# st3 = {4, 3, 9, 12, 7} 
# st4 = {1, 11, 5, 6, 13} 
# st.update(st2)
# st.update(st3)
# st.update(st4)
# print(st)
# print(len(st2))
# print(len(st3))
# print(len(st4))
# print(type(st2))
# st2.pop
# st3.pop
# st4.pop
# print(st2)
# print(st3)
# print(st4)

# menu = {"lagman":80, "borsh":50}
# menu["beshparmak"] = 130
# menu["samsa"] = 20
# menu["lagman"] = 135
# del menu["borsh"]



# print(menu)



# Problem 020
# seet = {".update()","intersection_update()",".intersection()","difference()", "sdisjoint()", ".issubset()", ".issuperset()", ".union()", ".symmetric_difference()", ".copy()", ".update()", ".difference_update()", ".symmetric_difference_update()", ".add()", ".remove()", ".discard()", ".pop()", ".clear()"}
# dictii = {".clear()", ".copy()", ".fromkeys()", ".get()", ".items()", ".keys()", ".pop()", "popitem()", "setdefault()", "update()", "values()"}
# print(seet & dictii)

# cars = []
# car = input("Введите вашу машину: ")
# cars.append(car)
# print("Ваша машина: ", cars)

# students = ("Erbol", "Dior", "Nurbek")
# student = input("Input students name: ")
# if student in students:
#     print("{name} is our student".format(name=student))
# else:
#     print("{name} is our student".format(name=student))
    

mydict = {"play":"играть", "run":"бегать"}
mydict["swim"] = "плавать"
mydict["jump"] = "прыгать"
mydict["brake"] = "ломать..???"
word = input("Введите слово для перевода: ")
print(mydict[word])

