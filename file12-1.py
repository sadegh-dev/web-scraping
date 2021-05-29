import requests

url = 'http://www.webscrapingfordatascience.com/cookielogin/'

rp = requests.post(url, data={'username':'charlie', 'password':'1234'})

cok = rp.cookies['PHPSESSID']

myCookie = {
    'PHPSESSID' : cok ,
}

r = requests.get(url + 'secret.php', cookies= myCookie)

print(r.text)





