import requests

myurl = "https://nurbatron.github.io/myport/"
respone = requests.get(myurl)
print(respone)
print(respone.text)
lst = respone.text.split("\n")
print("кол-во строчек кода", len(lst))
c = 0
print("код статуса",respone.status_code)
print("тип запроса", respone.request)
print("тип запроса", respone.request.method)
print("URL сайт", respone.url)
print(respone.encoding)
print("контент чайта", respone.content)