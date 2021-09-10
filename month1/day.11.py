# str1 = 'information'
# res = {}
# for i in str1:
#     if i in res:
#         res[i] += 1
#     else:
#         res[i] = 1    
# print(res)

############################################

# def sum(a, b):
#     print(a + b)

# def minus():
#     print(5 - 4)


# def un():
#     print(5 * 4)

# def dev():
#     print(5 % 4)

# def test(fun, fun2, fun3, fun4):
#     print("Begin of function")
#     fun(5, 6)
#     fun2()
#     fun3()
#     fun4()
#     print("End of function")

# test(sum,minus,un,dev)

"""декораты"""

# def sayhallo():
#     print("Hello everybody!")
#     print("how are you?")

# def my_decor(my_func):
#     def wrap():
#         print("begin of decor")
#         my_func()
#         print("End of decor")
#     wrap()
# my_decor(sayhallo)

# def my_decor(my_func):
#     def wrap():
#         print("begin of decor")
#         my_func()
#         print("End of decor")
#     wrap()
# @my_decor

# def sayhallo():
#     print("Hello everybody!")
#     print("how are you?")

# # from my_function import my_lambda

# # print(my_lambda)

# @my_decor
# def removesinhle():
#     a = [5, 6, 8, 7, 5, 6]
#     a = set(a)
#     print(list(a))





# """datetame"""
# import datetime
# mydate = datetime.datetime(2007, 4, 12, 10, 25, 30, 666666)
# onlydate = datetime.date(2001, 12, 25)
# onlytime = datetime.time(11, 22, 45)
# today = datetime.datetime.today()
# now = datetime.datetime.now()

# print(mydate)
# print(onlydate)
# print(onlytime)
# print(today)
# print(now.date())
# print(now.time())
# print(now.day)
# print(now.month)
# print(now.year)



# # bd = int(input("ваша дата: "))
# # print(now.year - bd, "лет", )


# print(today.strftime("%y:%m:%d"))
# print(today.strftime("%y--%m--%d"))
# print(today.strftime("%y--%h--%d"))
# print(today.strftime("%H-%M-%S"))

import random
myNum = random.random()
print(myNum)

my_ineger = random.randint(0, 99)
print(my_ineger)

#####################

from random import random, randint, choice

myNum2 = random()
print(myNum2)

my_ineger2 = randint(0, 99)
print(my_ineger2)


myStr = "ITCBootcamp"
random_letter = choice(myStr)

for i in range(len(myStr)):
    if myStr[i] == random_letter:
        print("Индекс буквы:", random_letter, i)