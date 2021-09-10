"""" 6 Функция split() """

# string = "Python Django PHP Laravel"
# print(string.split())

# word = "I$ live$ in$ KG"
# print(word.split("$"))


# numbers = "125 255 356 65"
# numbers = numbers.split()
# numbers = map(int, numbers)
# numbers = list(numbers)
# print(numbers)

# numbers = "5 6 8 54 98 6"
# numbers = numbers.split()
# numbers = map(int, numbers)
# numbers = list(numbers)
# print(numbers)


#print(list(map(int, input().split())))

# nums = map(int, input().split())
# nums = sum(nums)
# print(nums)

# a = list(map(int, input().split()))
# count = 0
# for i in a:
#     count = count + i
# print(count)

# l = [1, 2, 3, 4, 5, 6, 10, 11, 9]
# for i in range(len(l)):
#     if l[i] >= 10:
#         print(i)
#         break

"""continue в цикле"""

# lst = [5, 6, 7, 8, 9, 10]
# for i in lst:
#     if i ==7:
#         continue
#     print(i)

# mat = [
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16],
#     [17, 18, 19, 20]
# ]

# print(len(mat))
# for i in range(len(mat)):
#     print(mat[i])
#     print(f'Первое число:{mat[i][0]}, {i}-индекса')
#     print("Первое число: ",  mat[i][0],",", i, "-индекса")
#     print("Первое число: "+ str(mat[i][0])+","+ str(i)+ "-индекса")
#     print("Первое число:  {}, {}-индекса".format(mat[i][0],i))
#     print("Первое число:  {0}, {1}-индекса".format(mat[i][0],i))


# print(len(mat))
# for i in range(len(mat)):
#     print(mat[i][0])
#     print(mat[i][1])
#     print(mat[i][2])
#     print(mat[i][3])
#     print(mat[i][4])

# mat2 = [
#     [5, 6, 7, 8, 6, 8],
#     [9, 10, 11, 12, 6, 9],
#     [13, 14, 15, 16, 4, 3],
#     [17, 18, 19, 20, 1, 2]
# ]

# for i in range(len(mat2)):
#     print(mat2[3][0])
#     break

print("ZA" " WAARUDO")

l1 = [1, 2, 3]
l2 = [4, 5, 6]

l3 = l1 +l2
l1 += l2

# print(l1, l3)

# print(l3)
l3 = []
for x, y in zip(l1, l2):
    # print("l1", x)
    # print("l2", y)
    print(x + y)