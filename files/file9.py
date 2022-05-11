import requests

url = 'http://www.webscrapingfordatascience.com/postform2/'


formData = {
    'name' : 'charlie' ,
    'gender' : 'M' , 
    'pizza' : 'like' , 
    'salad' : 'like' , 
    'haircolor' : 'black' , 
    'comments' : 'How are you ?' , 
}



result = requests.post(url, data=formData)

print(result.text)

