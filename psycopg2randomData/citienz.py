import psycopg2
import random as rd
from datas import logins, domains, professions, countries, pswd_symbols, streets
# num = rd.randint(0, 10)


# print(num)

password = input('введите пароль прошу тебя: ')
connection = psycopg2.connect(
            database = 'citizens', 
            user = 'postgres', 
            password = password, 
            host = 'localhost', 
            port = '5432')

cursor = connection.cursor()

passwords = []
emails = []
phone_num = []
address = []
addresses = []
followers = tuple(rd.randint(1, 10000000) for i in range(5000))
# print(followers)

for name in logins:
    email = name + domains[rd.randint(0, len(domains)-1)]
    emails.append(email)

print(emails)

for i in range(5000):
    pasw = ''
    for p in range(rd.randint(8, 15)):
        pasw += pswd_symbols[rd.randint(0, len(pswd_symbols)-1)]
    passwords.append(pasw)

# print(passwords)

codes = ('75', '55', '77', '78', '50', '99')


for num in range(5000):
    number = '+996' + str(codes[rd.randint(0, len(codes)-1)]) + str(rd.randint(0, 9))+str(rd.randint(111111, 999999))
    phone_num.append(number)

print(phone_num)

for i in range(5000):
    address = streets[rd.randint(0, len(streets)-1)] + " " + str(rd.randint(0, 500))
    addresses.append(address)

# print(address)
# print(len(addresses))


cursor.execute("""CREATE TABLE users(user_id serial primary key, login varchar(20) not null, password varchar(100) not null, 
email varchar(100) not null, phone_number varchar(20) not null, country varchar(50) not null, address varchar(50) not null, 
proffesion varchar(50) not null, followers int not null)""")

query = '''insert into users(login, password, email, phone_number, country, address, proffesion, followers) values'''

for _ in range(10000):
    query += f"""(
        '{logins[rd.randint(0, len(logins)-1)]}',
        '{passwords[rd.randint(0, len(passwords)-1)]}',
        '{emails[rd.randint(0, len(emails)-1)]}',
        '{phone_num[rd.randint(0, len(phone_num)-1)]}',
        '{countries[rd.randint(0, len(countries)-1)]}',
        '{addresses[rd.randint(0, len(addresses)-1)]}',
        '{professions[rd.randint(0, len(professions)-1)]}',
        '{followers[rd.randint(0, len(followers)-1)]}'
    ),"""

sql_query = query[:-1] + ';'

cursor.execute(sql_query)
connection.commit()

cursor.close()
connection.close()