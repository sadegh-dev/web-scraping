import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Game_of_Thrones'

result = requests.get(url)

content = BeautifulSoup(result.text, 'html.parser')

#1
answer1 = content.findAll(['h1','h2'])
#2
answer2 = content.find(['h1','h2'],{'id':'mw-toc-heading'})
#3
answer3 = content.find(['h1','h2'],class_='firstHeading')
#4
answer4 = content.findAll('span',class_='mw-headline', limit=10)
#print(len(answer4))



print(len(answer4))


