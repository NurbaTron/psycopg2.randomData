"""уверен адбулхаким проиграет из за меня."""

#____________________________problem1______________________________


print ("Введите любой из этих знаков: '+,-,*,/'") 
w = input('сюда: ') 
a = int(input("Введите перове число: ")) 
b = int(input("Введте второе число: ")) 
if w == '+': 
    print (a+b) 
elif w == '-': 
    print (a-b) 
elif w == '/': 
    print (a/b) 
elif w == '*': 
    print(a*b)

#____________________________problem2______________________________


a = 0 
b = 2 
c = 5 
print ('a = ',a) 
print ('b = ',b) 
print ('c = ',c) 
print ('_______after the reaction__________') 
a = b 
b = c 
c = (a+b) 
print ('a = ',a) 
print ('b = ',b) 
print ('c = ',c)


#____________________________problem3______________________________

A_p = int(input("Введите длину квадрата:"))
perimeter = (A_p + A_p)
rectangle = A_p+A_p
print("площадь равна", rectangle, "сантиметрам")
print("периметр равен", perimeter, "сантиметрам")


#____________________________problem4______________________________

sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')

is_repeatable0 = len(sequence_0) != len(set(sequence_0)) 
print("Имеются повторяющиеся элементы" if is_repeatable0 else "Все элементы уникальны")

is_repeatable1 = len(sequence_1) != len(set(sequence_1))
print("Имеются повторяющиеся элементы" if is_repeatable1 else "Все элементы уникальны")

is_repeatable2 = len(sequence_2) != len(set(sequence_2))
print("Имеются повторяющиеся элементы" if is_repeatable2 else "Все элементы уникальны")

is_repeatable3 = len(sequence_3) != len(set(sequence_3))
print("Имеются повторяющиеся элементы" if is_repeatable3 else "Все элементы уникальны")


#____________________________problem5______________________________

keys_values = ('one', 1, 2, 'two', 3, 'three', 'four', 4, 'five', 5, 6, 'six', 7, 'seven', 'eight', 8, 'nine',9, 10, 'ten', 11, 'eleven', 12 ,'twelve') 
Dictionary_pairs = {} 
for i in range(len(keys_values)): 
    if i%2==0 and type(keys_values[i]) == str: 
        if i < 23: 
            Dictionary_pairs[keys_values[i]] = keys_values[(i+1)] 
    if i%2==0 and type(keys_values[i]) == int: 
        if i < 23: 
            Dictionary_pairs[keys_values[(i+1)]] = keys_values[i] 
print(Dictionary_pairs)


#____________________________problem6______________________________

f=lambda x :sorted(set(str(x)),reverse=True)==list(str(x)) 
print(f(int(input('enter a 4 digit number: '))))

#___________________________THE END________________________________