"""ООП композиция"""

"""класс композиций  - это у которого атрyибут является объектом другого класса"""

# class Adress:
#     def __init__(self, streetname, city, homenum):
#         self.streetname = streetname
#         self.city = city
#         self.homenum = homenum


# class Job:
#     def __init__(self, jobname, salary, time):
#         self.jobname = jobname
#         self.salary = salary
#         self.time = time

# class Worker:
#     def __init__(self, name, streetname, city, homenumber, jobname, salary, time):
#         self.name = name
#         self.adress = Adress(streetname = streetname, city = city, homenum = homenumber)
#         self.job = Job(jobname = jobname, salary = salary, time = time)



#     def show_data(self):
#         return f"{self.name} {self.job.jobname}, он живёт в {self.adress.city} на улице {self.adress.streetname}, а ЗП {self.job.salary} HUNDRED BUKS, а времени на работу тратит {self.job.time} часа"


# work = Worker("салокхидин", "ленин", "Оше", 11, "програмист питон", 3, 3)
# print(work.show_data())



class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Araon:
    def __init__(self, works, proffesion):
        self.works = works
        self.proffesion = proffesion

class Worker:
    def __init__(self, name, age, gender, works, proffesion):
    
        self.human = Human(name = name, age = age, gender = gender)
        self.work =Araon(works = works, proffesion = proffesion)

    def show_dat(self):
        return f"My name is {self.human.name}, I am {self.human.age}, years old, I am {self.human.gender} and my proffecion is {self.work.proffesion}"

sas = Worker("Andrey", "23", "male", "in England", "builder")
print(sas.show_dat())



class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_data(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_data(self):
        return f"{self.name} is {self.age} years old. He is {self.gender}"

class Worker2:
    def __init__(self, proffesion, name, age, gender):
        self.proffesion = proffesion
        self.about = Human(name = name, age = age, gender = gender)

    def show_info(self):
        return f"""My name is {self.about.name}, I am {self.about.age} years old, I am a {self.about.gender}, I am a {self.proffesion}""" 

w = Worker2("developer", "Asian", 23, "man")
print(w.show_info())


class A:
    number = 89
    color = "red"

    def show(self):
        return f"число {self.number}"

class B(A):
    pass

clasb = B()
print(clasb.show())


str1 = "apple"
print(len(str1))

lst = [5, 6, 54, True]
print(len(lst))

dict2 = {"name":"Lera", "age":17, "gender":"female"}
print(dict(dict2))


