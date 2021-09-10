# lst = [5, 8, 2, 7, 8, 8, 2, 4]
# n = 8
# res = []
# if n in lst:
#     for i in range(len(lst)):
#         if n == lst[i]:
#             res.append(i)
#         print(*res)
# else: print("Отсутствует")

# def lst2(number):
#     res = []
#     for i in range(len(number)):
#         res.append(i)

#     return res

# my_input = int(input("Input your number: "))
# print(lst2(my_input))

#Тернарный оператор
# a = 21
#если а == 21 то вывести на экан "ровно"
#если а !=  21 то вывести "не ровно"
#tckb a > 21 то вывести "больше"
#если a < 21 то вывести "меньше"

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# res = ["Они равны" if a == b else "Они неравны" if a != b else "больше" if a > b else "меньше" if a < b else a]
# print(*res)

# lst = [5, 8, 2, 7, 8, 8, 2, 4]
# for i in lst:
#     print(i, end=" ")

# lst = [5, 8, 2, 7, 8, 8, 2, 4]    

# def mySum():
#     print(5+7)

# def mySum2(a, b):
#     print(a + b)

# def mySum3(a, b):
#     print("Hello")
#     return a+b

# mySum()
# mySum2(5, 1)
# mySum2(5, 7)
# print(mySum3(5, 3))

number1 = 1
u = 1
pin_kod = 2005
while u >0:
    if number1>0:
        print("Банк BEKbank приветствует вас!")

balance = 3000000
print('1.USD = 84.80 KGS')
print('2.EU = 101.70 KGS')
print('3.KT = 0.200 KGS')
voluta = int(input('Укажите в какой валюте хотите снять чеканые монеты: '))
if voluta == 1:
    print("У вас на счету: ", balance / 84.80, 'USD!')
    chek = float(input('Укажите нужную сумму в USD для снятия: '))
    if chek > balance / 84.80:
        print('У вас недостаточно средств. . .')
    else:
        print('Возьмите' , chek, 'USD!' , 'Остаток на карте: ' , balance / 84.80 - chek , 'USD/', (balance / 84.80 - chek) * 84.80 , '(SOM)')
if voluta == 2:
        print("У вас на счету: ", balance / 101.70, 'EU!')
chek = float(input('Укажите нужную сумму в EU для снятия: '))
if chek > balance / 101.70:
        print('У вас недостаточно средств. . .')
else:
        print('Возьмите' , chek, 'EU!' , 'Остаток на карте: ' , balance / 101.70 - chek , 'UE/', (balance / 101.70 - chek) * 101.70 , '(SOM)')
        if voluta == 3:
            print("У вас на счету: ", balance / 0.200, 'KT!')
chek = float(input('Укажите нужную сумму в KT для снятия: '))
if chek > balance / 0.200:
        print('У вас недостаточно средств. . .')
else:
        print('Возьмите' , chek, 'KT!' , 'Остаток на карте: ' , balance / 0.200 - chek , 'KT/', (balance / 0.200 - chek) * 0.200 , '(SOM)')