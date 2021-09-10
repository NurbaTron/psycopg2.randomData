# delete_probel = "T E S T" # Test
# delete = (delete_probel.replace(" ", ""))
# print(delete.title())

# text = "ISSYK KUL"
# text_fin = (text.replace(" ", "-"))
# print(text_fin.title())

# print("кол-во букв 'I'", text.count("I"))
# print("кол-во букв 'S'", text.count("S"))
# print("кол-во букв 'Y'", text.count("Y"))
# print("кол-во букв 'K'", text.count("K"))
# print("кол-во букв 'U'", text.count("U"))
# print("кол-во букв 'L'", text.count("L"))

#срез и индекс строки


# индекс


# txt =   "cars"
# print(txt[0])
# print(txt[1])
# print(txt[2])

# course = "ITCBootcamp"

# # print(course[-1])
# # print(course[10])

# print(course[3:])

# cource2 = "ITC-Bootcamp"
# print(cource2.replace("-", ""))

# lake = "CHOLPONATA"
# LAKE2 = (lake.replace("NA", "N-A"))
# print(LAKE2.title())

# cholpon = lake[0:7].title()
# ata = lake[7:].title()
# print(cholpon,"-",ata)

# city = "newyork"
# city1 = (city.replace("wy", "w y"))
# print(city1.title())

# letter = "o"
# letter2 = "B"
# letter1 = "k"
# letter3 = print(letter1+letter*2+letter2)

# kg = "KYRGYZSTAN"

# print(kg[0:-1:2])

# print(kg[9::-1])


# List and Tuples


lst = [55, 4, 23, "Cat", True, 8, False]
print(type(lst))

lst2 = list()
lst2.append(45)
lst2.append(75)
lst2.append(12)
lst2.append(True)
lst2.append("GAAAS")

print(lst2)

lst.append("GAAAS")
lst.append(45)
lst.append("GAAAAAAAAAAAAAS")
lst.append(False)
lst.append(56)
print(lst)
print(lst[1])

animals = ["bear", "pig", "lion", "horse", "sheep"]
print(animals[4])
print(len(animals))

numbers = [55, 89, 6, 55, 8, 6, 44, 3, 5, 3,]
print(numbers[-2])
print(len(numbers))
print("Кол-во чисел 55 -", numbers.count(55))
print("Кол-во чисел 89 -", numbers.count(89))
print("Кол-во чисел 6 -", numbers.count(6))
print("Кол-во чисел 8 -", numbers.count(8))
print("Кол-во чисел 44 -", numbers.count(44))
print("Кол-во чисел 3 -", numbers.count(3))
print("Кол-во чисел 5 -", numbers.count(5))

numbers.remove(55),numbers.remove(6),numbers.remove(3),numbers.remove(3)
print(numbers)