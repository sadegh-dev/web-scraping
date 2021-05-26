import requests
from bs4 import BeautifulSoup

url = 'http://www.webscrapingfordatascience.com/postform3/'

r = requests.get(url)
html = BeautifulSoup(r.text, 'html.parser')
protection = html.find('input',{'name':'protection'}).get('value')

formData = {
    'name' : 'charlie' ,
    'gender' : 'M' ,
    'pizza' : 'like' ,
    'salad' : 'like' ,
    'haircolor' : 'black' ,
    'comments' : 'How are you ?' ,
    'protection' : protection ,
}

result = requests.post(url, data=formData)
print(result.text)

