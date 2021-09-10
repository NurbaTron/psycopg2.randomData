"""Принцы ООП - инкапсуляция"""

# 1. Public -  публичный
# 2. Protected - защищённый
# 3. Private - приватный

# class Bankomat:
#     def __init__(self, name, id, password):
#         self.name = name              #Публичный 
#         self._id = id                 #Защещённый
#         self.__password = password    #Приватный  

#     def printpubdat(self):  #Публичный метод
#         print("Name", self.name)

#     def printprotecteddat(self): #Защищённый метод
#         print(self.name, self._id, self.__password)

#     def __printprivatedata(self):
#         print(self.name, self._id, self.__password)


# mycart = Bankomat("Nurbek", 419856, 1234)
# print(mycart.name)
# print(mycart._id)
# print(mycart._Bankomat__password)
# mycart.printpubdat()
# mycart.printprotecteddat()
# mycart._Bankomat__printprivatedata()


# class Account:
#     def __init__(self, nickname, realname, password):
#         self.nickname = nickname
#         self._realname = realname
#         self.__password = password

#     def printmyacc(self):
#         print(self.nickname)

#     def _printmyrealname(self):
#         print(self._realname)

#     def __printmypassword(self):
#         print(self._Account__password)

# myacc = Account("NurbaTron Studios", "Nurbek", "t22r10o20n03")
# myacc.printmyacc()
# myacc._printmyrealname()
# myacc._Account__printmypassword()


#создать класс instagramm, 3

"""Геттер, сеттер"""

# class Valut:
#     def __init__(self):
#         self._number = None

#     def setnumber(self, num):  #Сеттер
#         self._number = num

#     def getnumber(self):
#         return self._number   #Геттер

#     def delnumber(self):
#         del self._number

#     myproperty = property(getnumber, setnumber)

# mynum = Valut()
# # mynum.setnumber(6)
# # print(mynum.getnumber())
# # mynum.delnumber()
# # mynum.setnumber(8)
# # print(mynum.getnumber())

# mynum.myproperty = 15
# print(mynum.myproperty)

# class Salary:
#     def settory(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def getory(self):
#         return self.salary

#     def year(self):
#         print(self.salary*12)

# p = Salary()
# p.settory("cas",500)
# print(p.getory())
# p.year()