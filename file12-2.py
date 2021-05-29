import requests

url = 'http://www.webscrapingfordatascience.com/redirlogin/'

rp = requests.post(url, data={'username':'charlie', 'password':'1234'},allow_redirects=False)


print(rp.cookies)

