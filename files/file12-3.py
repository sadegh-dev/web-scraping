import requests

url = 'http://www.webscrapingfordatascience.com/trickylogin/'

rg1 = requests.get(url)
rg1Cookie = { 'PHPSESSID' : rg1.cookies['PHPSESSID'] }


rp1 = requests.post(url, params={'p':'login'}, data={'username':'charlie', 'password':'123'} ,allow_redirects = False, cookies = rg1Cookie )
rp1Cookie = {'PHPSESSID' : rp1.cookies['PHPSESSID']}

rg2 = requests.get(url, params={'p':'protected'}, cookies = rp1Cookie)

print(rg2.text)




