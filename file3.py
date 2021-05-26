import requests

url = 'http://www.webscrapingfordatascience.com/basichttp/'

result = requests.get(url)

# Response
print(result)

# text of website
print(result.text)

# 200 / 404
print(result.status_code)

# OK / Not Found
print(result.reason)

# Headers of Response
print(result.headers)

# details of Headers of Response with Title of Dictionary
print(result.headers['Server'])

# Request
print(result.request)

# Headers of Request
print(result.request.headers)



