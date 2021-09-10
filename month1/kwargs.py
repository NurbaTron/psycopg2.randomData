def add(*num):
    sum = 0

    for n in num:
        sum = sum + n

    print(sum)

add(2, 5, 12, 44)

def rem(**data):
    print(data)
    for key, value in data.items():
        print("{} - {}".format(key, value))

rem(name = "john", age = 15, sourname = "Vud", number = 1234567890)      



