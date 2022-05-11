import requests

######## Example 1 ##########

url = 'http://www.webscrapingfordatascience.com/paramhttp/'


parameters = {
    'query' : 'charlie',
}

result = requests.get(url, parameters)

print(result.text)


######## Example 2 ##########

url = 'http://www.webscrapingfordatascience.com/calchttp/'


parameters = {
    'a' : 10 ,
    'b' : 5 ,
    'op' : '+' ,
}

result = requests.get(url, parameters)

print(result.text)

