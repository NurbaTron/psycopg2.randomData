"""ООП, Класс и объекты"""
# # mystr = "python"
# mystr = 15
# mystr = True
# print(type(mystr))


# class Computer:         
#     model = "asus"    #атрибуты
#     ram = 32
#     hdd = 1000
#     is_working = False
#     jp = 3060
#     color = "Black"
#     display = 14.60
#     power = 100

#     def turnon(self):  #методы
#         self.is_working = True
#         self.power -= 1
#         print(f"{self.model}'s power is {self.is_working}")
#         # print(f"оперативная память - {self.ram} а экран - {self.jp}")

# def __str__(self):
#     return self.model

# asus = Computer()  #создали объект класса computer
# print(asus.ram)
# print(asus.model)
# asus.turnon()
# print(asus.color)
# print(asus.hdd)


# class Cat:
#     name = "Матроскин"
#     color = "черный"

#     def __str__(self):
#         pass

# cat = Cat
# print(f"Имя кота {Cat.name}а цвет {Cat.color}")

# class д:
#     loin = "Лев"
#     scream = "WRRYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"

#     def __str__(self):
#         pass

# dom = д
# print(f"это {д.loin}, а орёт он {д.scream}")


# class Counter:
#     def start_from(self, count = 0):
#         self.count = count
#     def increment(self):
#         self.count += 1

#     def display(self):
#         print(f'Текущее значение счётчика = {self.count}')

#     def reset(self):
#         self.count = 0

# myCount = Counter()
# myCount.start_from(55)
# myCount.increment()
# myCount.display()

# myCount.increment()
# myCount.display()

# myCount.increment()
# myCount.display()

# myCount.reset()
# myCount.display()
# myCount.increment()
# myCount.display

# """конструктор"""

# class  Human:
#     def __init__(self, name, sourname, age, gender):
#         self.name = name
#         self.sourname = sourname
#         self.age = age
#         self.gender = gender

# anna = Human("Anna", "Sol", 15, "Female")
# print(f"Name:{anna.name}")
# print(f"{anna.name}'s sourname:{anna.sourname}")
# print(f"{anna.name}'s gender: {anna.gender}")
# print(f"{anna.name}'s age: {anna.age}")

# ##########################f####################################

# class Me:
#     def __init__(self, name, sourname, age, gender):
#         self.name = name
#         self.sourname = sourname
#         self.age = age
#         self.gender = gender

# Loh = Me("Nurbek", "Kalushev", 18, "male")
# print(f"Name: {Loh.name}")
# print(f"{Loh.name}'s sourname:{Loh.sourname}")
# print(f"{Loh.name}'s gender: {Loh.gender}")
# print(f"{Loh.name}'s age: {Loh.age}")


# class Nout:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

# pack = Nout("Thinkpad", 5, "40000 сомиков")
# print(f"Брэнд у этого ноута {pack.brand}") 
# print(f"Модель у этого ноута {pack.model}")
# print(f"А цена {pack.price}")


class Soccerplayer:
    def __init__(self, name, sourname):
        self.name = name
        self.sourname = sourname
        self.goals = 0
        self.asis = 0
    
    def score(self, goals = 1):
        self.goals += goals

    def make_asis(self, asis = 1):
            self.asis += asis

    def statistics(self):
        print(f"{self.sourname} {self.name} - голы: {self.goals}, передачи: {self.asis}")
    
leo = Soccerplayer('Leo', 'Messi')
leo.score(700)
leo.score(700)
leo.make_asis(500)
leo.make_asis(200)
leo.statistics()
kokorin = Soccerplayer('Alex', 'Kokorin')
kokorin.score()
kokorin.statistics()