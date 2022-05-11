import requests

url = 'http://www.webscrapingfordatascience.com/usercheck/'


#normal
"""
r = requests.get(url)
print(r.text)
"""

#change User-Agent
myHeaders = {
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36' ,
}
r = requests.get(url, headers= myHeaders)
print(r.text)






url2 = 'http://www.webscrapingfordatascience.com/referercheck/secret.php'


#change Referer
myHeaders = {
    'Referer' : 'http://www.webscrapingfordatascience.com/referercheck/' ,
}
r = requests.get(url2, headers= myHeaders)
print(r.text)

