# strl1 = "I live in Japan"
# strl2 = "I live in Japan"

# text1 = '''

#     i live in Japan
#     i love Amerika
#     obama is monke

#     '''

# text2 = '''
    
#     I live in Japan
#     I have a girlfriend
#     I love manga
    
#     '''

# apostrof = "привет д'фыв"
# apostrof = "привет д'фыв"
# txt = "I love manga"
# print(apostrof)
# print(apostrof)


# country= "киргизтан"
# print(country.replace("и", "ы"))

# str2 = "{}блак{}"
# print(str2.replace("{}", "о"))

# note = "камп"
# print(note.replace("а", "о"))

# str3 = "м{}л{}к{}"
# print(str3.replace("{}", "о"))

# str3 = "(){}л{}[]{}"
# print(str3.replace("{}", "о").replace("[]", "к").replace("()" , "м"))  


# my_country = "кыргызская республика"
# print(my_country.title())

# writer = "калышев нурбек"
# writer = writer.title()
# print(writer)

# county = "кр"
# county = county.upper()
# print(county)

# course = "itc"
# cource = course.upper()
# print(cource)

# channel = "орт"
# channel = channel.upper()
# print(channel)


# text2 = "Я РУССКИЙ"
# print(text2.lower())

# text3 = "АНГЛИЙСКИЙ ЯЗЫК"
# print(text3.lower())

# aboutMe = "{who} am a Python Develover".format(who = "I")
# aboutMe2 = "{txt} a a Python Develover".format(txt = "Ali")
# aboutMe3 = "{0} a a Python Develover {1}".format("Nurbik", "in the USA")
# aboutMe4 = "{} a a Python Develover".format("Nurbek")

# a = "Amantur"
# b = "in USA" 
# aboutMe5 = a + " is a Python Develover" + b

# print(aboutMe)
# print(aboutMe2)
# print(aboutMe3)
# print(aboutMe4)
# print(aboutMe5)

# about = "My name is {name}, I'm {age}"


# print(about.format(name = "Nurbek", age = 17))

# my = "I speac {lang}, my favorite language is {fav}"
# print(my.format(lang = "Russia", fav = "English"))

# mytext = "DIO is vampire"

# firtsword= mytext.endswith("DIO")
# lastword = mytext.startswith("DIO")

# print(firtsword)
# print(lastword)

# inputText = input("students name: ").title()
# if inputText.startswith("Yakhyo"):
#     print("Yes Yakhyo is student at ITCBootcamp")
# elif inputText.startswith("Dior"):
#     print("Yes Dior is student at ITCBootcamp")
# elif inputText.startswith("Salokhidin"):
#     print("Yes Salokhidin is student at ITCBootcamp")
# elif inputText.startswith("Abdulhkahim"):
#     print("Yes Adbulhkahim is student at ITCBootcamp")
# elif inputText.startswith("Nurbek"):
#         print("Yes Nurbek is student at ITCBootcamp")
# elif inputText.startswith("Amantur"):
#     print("Yes Amantur is student at ITCBootcamp")
# elif inputText.startswith("Yraznapali"):
#     print("Yes Yraznapali is student at ITCBootcamp")
# elif inputText.startswith("Erbol"):
#     print("Yes Erbol is student at ITCBootcamp")
# else:
#     print("{inputText} is not a student of ITCBootcamp".format(inputText = inputText))



my_fruits = "apple, apple, banana,"
print(my_fruits.count("apple"))
print(my_fruits.count("banana"))

fruit = "apple"
lenth_of_apple = len(fruit)
print("Word {fruit} consist {lenth} letter".format(fruit = fruit, lenth = lenth_of_apple))

#введите ваше имя
#ваше имя ... оно имеет ... букв

myName = input("Введите ваше имя: ").title()
print("Ваше имя", myName,"Там", len(myName), "Букв")

#problem23




number_of_school=input("Введите номер вашей школы ")
if number_of_school.isalpha():#проверяем , что слово состоит только из букв или символов
    print("Оо круто")
else:
    print("Введите номер вашей школы")
print("----------------------------")
number_of_school=input("Введите номер вашей школы ")
if number_of_school.isdigit():#проверяет, что слова состоит только из чисел
    print("Оо круто")
else:
    print("Введите номер вашей школы")