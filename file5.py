import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Game_of_Thrones'

result = requests.get(url)

content = BeautifulSoup(result.text, 'html.parser')

one = content.find('h2')
print(one)

other = content.findAll('h2')
print(other)

for a in other :
    print(a)

