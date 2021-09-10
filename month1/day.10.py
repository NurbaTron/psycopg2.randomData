""" item(), keys(), values() """

# dict1 = {"hair":"yellow", "apple":["red", "green", "green", "yellow"], "banana":"yellow"}

# for i in dict1:
#     print(f"keys: {i} - values: {dict1[i]}")

# print("case 2")
# for key, value in dict1.items():
#     print(f"{key} - {value}")

# for i in dict1.keys():
#     print(f"keys: {i} - values: {dict1[i]}")

# for i in dict1.values():
#     print(f"values: {i}")



#mylist = [1, 5, 6, 1, 8, 4, 4, 5, 1]
#mydict = {1:3, 5:2, 6:1, 8:1, 4:2}
# mydict = {}
# for i in mylist:
#     ren = i
#     lol = mylist.count(i)
#     mydict[ren] = lol
# print(mydict)


# for i in mylist:
#     if i in mydict:
#         mydict[i] += 1
#     else:
#         mydict[i] = 1
# print(mydict)


""" Анонимные функций - lambda"""

# def my(a):
#     return a + a
# print(my(5))

# lmbda = lambda a, b, n, s: a + b * n // s
# print("ответ:", lmbda(6, 4, 3, 8))

# number = lambda b: b-b
# print(number(2))

# number1 = lambda n:  n*n
# print(number1(3))

# number3 = lambda s: s%s
# print(number3(6))

# a = range(1100, 4600,4)
# # a = map(lambda x: x, a)
# for i in a:
#     if i % 5 != 0:
#         print(i, end=" ")

"""модуль, библиотека"""

# import my_function

# my = my_function.my_title("великая фатронская германия")
# print(my)


# from my_function import my_title
# my2 = my_title("билят я хавать беляш хачуу")
# print(my2)

# from my_function import *
# mysum(5, 8)

# from my_function import 


# from my_function import *
# bigword("Кырг Аол Djk")



