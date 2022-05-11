import requests

url = 'http://www.webscrapingfordatascience.com/cookielogin/secret.php'

myCookie = {
    'ga' : 'GA1.2.2017735998.1622013604',
    '_gid' : 'GA1.2.1523074542.1622013604',
    'PHPSESSID' : 'mt21iv5udo52325agd72rd0lkm',
}


r = requests.get(url, cookies= myCookie)

print(r.text)

