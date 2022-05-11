import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Game_of_Thrones'

result = requests.get(url)

content = BeautifulSoup(result.text, 'html.parser')

#1
one = content.find('h2')
print(one)
#2
other = content.findAll('h2')
print(other)
#3
for a in other :
    print(a)

