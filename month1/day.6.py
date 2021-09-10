# login = input("Ведите ваш логин: ")
# if login == "admin":
#     print("Добро пожаловать программист!")
# elif login == "manager":
#     print("Сайт приветствует руководство!")
# else: 
#     print("Программа завершила своё использование. . .")


# Ебучие циклы While, For

# lst = [4, 5, 88, 7, 87, 56]
# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[3])
# print(lst[4])
# print(lst[5])
# print("здесь конъець")

# #1 способ

# for i in lst:   
#     print(i)    

#2 способ

# for i in range(len(lst)):   #i = 0     i = 1     i = 2   i = 3  i = 4   i = 5      
#     print(lst[i])           #lst[0]    lst[1]    lst[2]  lst[3] lst[4]  lst[5]                     


# 2<=i < len9lst
# for i in range(len(lst)):   #i = 0     i = 1     i = 2   i = 3  i = 4   i = 5      
#     print(lst[i]) 

# a = range(9)
# for i in a:
#     print(i)

# hi = "Hello world"
# for i in range(5):
#     print(hi)

# for i in range(6):
#     print(i, "- столько раз ты проиграл")

# for i in range(2, 20, 2):
#     print(i)

# for odd in range(1, 20, 2):
#     print(odd)

# number = int(input("Введите число для умножение: "))
# for i in range(11):
#     print(i, "*", number, "=", i*number)

#while

# num = int(input("до какого числа нужно вывести четные числа: "))
# i = 0
# while i < num:
#     print(i)
#     i = i + 2

# for i in range(0, 10, 1):
#     print(i)

# while i < 10:
#     print(i)
#     i = i + 1

# count = 0
# for i in [2, 8, 7, True]:
#     count = count + i
# print("Сумма всех чисел от 0 до 10: ", count)

# number = int(input("Введите число для умножение: "))
# if number % 2 ==0:
#     print("ura")

i = 0
while True:
    if i == 9999999999999999999999999999099999999999999999999999:
        break
    else:
        print(i)
    i +=999999

#задуха

# i = 0
# lang = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in range(len(lang)):
#     if lang[i] == 'php':
#         break
#     else:
#         print(lang[i])



# a = int(input("Введите число: "))
# b = a*a
# print(b)
# c = str(int(input("Желаете продолжить? ")))


# lst1 = [12, 71, -33, 0, 86]

# i = 0
# lst2 = []
# # while i < len(lst1):
# #     lst2.append(lst1[i]*5)
# #     i += 1
# # print(lst2)
# for i in range(len(lst1)):
#     lst2.append((lst1[i])*10)
# print(lst2)


# lst1 = [12, 71, -33, 0, 86]

# i = 0
# lst2 = []
# for i in range(len(lst1)):
#     lst2.append((lst1[i]))
# print(lst2,)


