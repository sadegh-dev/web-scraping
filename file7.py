import requests
from bs4 import BeautifulSoup
import re

url = 'https://en.wikipedia.org/wiki/Game_of_Thrones'

result = requests.get(url)

content = BeautifulSoup(result.text, 'html.parser')

#1
answer1 = content.find(re.compile('^d'))
#2
answer2 = content.select('div#logo', limit=2)
answer2 = content.select('tr.vevent', limit=2)
answer2 = content.select('a[href^="/wiki/"]', limit=2)


print(answer2)


