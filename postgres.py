import psycopg2 

database = 'data'
user = 'postgres'
password = 'rem'
# host = 'vocalhost'
host = '127.0.0.1'
port = '5432'

connection = psycopg2.connect(
    database=database,
    user=user,
    password=password,
    host=host,
    port=port
)

print('продключение к базе данных прошла успешно')

cursor = connection.cursor()

# cursor.execute("""
#     CREATE TABLE users(id SERIAL PRIMARY KEY, name VARCHAR(255), last_name VARCHAR(255), age INTEGER)
# """)

# values = ('Erbol', 'Ali', 15)

# name = input('Input your name: ')
# last_name = input("Input your last name: ")
# age = int(input("Input your age: "))

# values = (name, last_name, age)
# query = f"INSERT INTO users (name, last_name, age) VALUES {values}"
# cursor.execute(query)


# cursor.execute("SELECT * FROM users")
# my_data = cursor.fetchone() #только один
# print(my_data)
# print(type(my_data))

# my_data = cursor.fetchall() #все
# print(my_data)
# print(type(my_data))

# my_data = cursor.fetcany(size=3) выводит выбранную
# print(my_data)
# cursor.execute("UPDATE users SET age = 20 WHERE id=4")

# for i in my_data:
    # print(i)
    # print(type(i))
    # print(f'name: {i[1]}, last name {i[2]}, age {i[3]}')



def searchname(username):
    cursor.execute("SELECT * FROM users")
    allusers = cursor.fetchall()
    for i in allusers:
        if i[1] == username:
            print("name: ", i[1])
            print("last name: ", i[2])
            print("age: ", i[3])
    # print(allusers)

searchname("Erbolb")
connection.commit()
cursor.close()
connection.close()

