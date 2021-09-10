#__str__

#ООП - наследование

# class Cat:
#     def __init__(self, name2, age, tail, color, paws):
#         self.name = name2
#         self.age = age
#         self.tale = tail
#         self.color = color
#         self.paws = paws

#     def __str__(self):
#         return self.name

# class Tiger(Cat):
#     def say(self, a):
#         print(f"{self.name} says '{a}'")

# class Tiger(Cat):
#     pass

#     def say(self,a):
#         print(f"{self.name} says '{a}'")

# mur = Cat("Baranduga", 1.5, 1, "yellow", 4)
# print(mur.name)
# print(mur)
# tiger = Tiger("Тигруля", 9, 1, "orange", 4)
# print(tiger.name)
# print(tiger.paws)
# print(tiger)
# tiger.say("Askar")

from numbers import operators
class Cheknum :

    def chekphonenum(self, number):
        if len(number) == 10 and number[0] == "0":
            print("Ваш намбер валит на гелике")
            code = number[1:4]
            if code in operators["megacom"]:
                print("Ваш апарат Мигаком")
            elif code in operators["beeline"]:
                print("Пчел ты...")
            elif code in operators["O"]:
                print("у тебя О")
        else:
            print("Ваш намбер инвалид, он не можит спустится, купитэ ему пашаговою инструкцию")


numberInput = input("Водите ваш намбер: ")
myNumber = Cheknum()
myNumber.chekphonenum(numberInput)



# class Human:
#     def __init__(self, name, sourname, gender = "male"):
#         self.name = name
#         self.sourname = sourname
#         self.gender = gender


#     def __str__(self):
#         if self.gender == "male":
#             return f"гражданин {self.sourname} {self.name}"
#         elif self.gender == "female":
#             return f"гражданка {self.sourname} {self.name}"
#         else:
#             return f"{self.sourname} {self.name}"

# man = Human("Alex", "Tronhon")
# print(man.name)
# print(man.sourname)
# print(man.gender)

# print(man)

# woman = Human("Anna", "Woltsonn", "female")
# print(woman.name)
# print(woman.sourname)
# print(woman.gender)

# print(woman)

# class Publication:
#     def __init__(self, name, date, pages, library, type):
#         self.name = name
#         self.date = date
#         self.pages = pages
#         self.library = library
#         self.type = type

# class Book(Publication):
#     def __init__(self):
#         self.type = "book"

# book = Book()
# print(book.type)