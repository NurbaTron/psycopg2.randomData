# class Solution:
#     def isPalindrome(self, x):
#         x=str(x)
#         if x[0]=='-':
#             return False
#         if x == x[::-1]:
#             return True
#         return False

# what = Solution()
# print(what.isPalindrome(-44444))
# pass


class Solution(object):
    def twosum(self, nums, target):
        pass


# obj = Solution
# print(obj.twosum([2, 7, 11, 15], 9))
# print(obj.twosum([3, 2, 4], 6))
# print(obj.twosum([3, 2, 4, 5, 1], 9))
# res = [0, 1]
# res = [1, 2]
# res = [2, 4]

grid = [
    [4, 3, 2, -1],
    [3, 2, 1, -1],
    [1, 1, -1, -2],
    [-1, -1, -2, -3],
    ]

# for i in grid:
count = 0
for i in grid:
    for j in i:
        if j < 0:
            count += 1
print(count)



"""open()"""

myopen = open("notebook.txt", "r")
# print(myopen.read(56))
print(myopen.readline())
print(myopen.readline())


add = open("notebook.txt", "a")
add.write("ITCBootcamp")
# add.close()

myopen = open("notebook.txt", "r")
add.read