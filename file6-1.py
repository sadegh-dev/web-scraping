import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Game_of_Thrones'

result = requests.get(url)

content = BeautifulSoup(result.text, 'html.parser')

#1
answer1 = content.find('h1')


print(answer1)
print(answer1.name)
print(answer1.text)
print(answer1.get_text())
print(answer1.contents)
print(answer1.attrs)
print(answer1.get('id'))