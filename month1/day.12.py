"""args - позиционные жлементы, **kwargs - именованные элементы"""
# def mysum(a, b, *c):
#     print(a)
#     print(b)
#     print(*c)
#     print(c)
#     print(type(c))
# mysum(54, 99, 54, True, "code", 54, 88, 77, 89, 57)

# def test(a, **kwargs):
#     print(a)
#     print(type(kwargs))
#     print(kwargs)
#     for i in kwargs:
#         print(f"key: {i} - value: {kwargs[i]}")




# test(56)
# test(56, name = "Meerim",  is_student = True)

# dict1 = {"name":"Meerim", "is student":True}
# print(dict1.items())

# dict2 = {"code":15, "ru":"Russia"}
# a = {**dict1, **dict2}
# print(a)

# "я и не собирался потому что это не моё."

# def summ(a, *args):
#     summ = 0
#     for i in args:
#         if i % 2 ==0:
#             summ = summ +i
#     print(summ - a)
# summ(5, 45, 58, 98, 14, 2, 57, 8)

# def summ(a, *args):
#     summ = 0
#     for i in args:
#         if i % 2 ==0:
#             summ = summ //i
#     print(summ - a)
# summ(5, 45, 58, 98, 14, 2, 57, 8)

# """traceback"""

# def lst2(a,*args):
#     for i in args:
#         try:
#             print(a/i)
#         except ZeroDivisionError:
#             print("На ноль делить нельзя!")
#         except TypeError:
#             print("Тип данных str или False/True, а не число!")
#         finally:
#             print("Всё бл*ть. Конец.")
# lst2(5,4,5,8,7,0,1,True,False,"code")

a = []
a.append([])
from random import randint

def lists(a,b):
    res = []
    for i in range(a):
        res.append([])
        for j in range(b):
            res[-1].append(randint(0, 120))
    print(res)        
lists(2, 6) 
lists(2, 4) 
