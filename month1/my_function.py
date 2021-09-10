# def my_title(text):
#     return text.title()
# print(my_title("python language"))

# def mysum(a, b):
#     print(a + b)

# def bigword(a):
#     s = list()
#     s1 = a.upper()
#     a.title()
#     for i in range(len(a)):
#         if (a[i])==s1[i] and a[i]!=" ":
#             s.append(a[i])
#     print(*s,sep=" ")


mylist = [5, 6, 8, 987, 22]

my_lambda = map(lambda x: x * 2, mylist)
my_lambda = list(my_lambda)