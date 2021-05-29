import requests

url = 'http://www.webscrapingfordatascience.com/trickylogin/'

mySession = requests.Session()

mySession.headers.update({ 'User-Aget' : 'Mongard' })


r = mySession.get(url)
r = mySession.post(url, params={'p' : 'login'}, data={'username':'charlie', 'password':'123'})
r = mySession.get(url, params={'p':'protected'})

print(r.rerquest.headers)
print(r.text)


