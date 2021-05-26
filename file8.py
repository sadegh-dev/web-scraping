import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_episodes'

r = requests.get(url)

content = BeautifulSoup(r.text, 'html.parser')


episodes = []
epTables = content.select('table.wikiepisodetable')

for table in epTables :
    headers = []
    #rows = table.findAll('tr')   #all <tr> for all tables

    for header in table.find('tr').findAll('th'):
        headers.append(header.text)

    for row in table.findAll('tr')[1:]:
        values = []
        for col in row.findAll(['th','td']):
            values.append(col.text)
        if values:
            episodesDict = {headers[i]:values[i] for i in range(len(values))}
            episodes.append(episodesDict)


for ep in episodes :
    print(ep)



{
'No.overall': '73', 
'No. inseason': '6', 
'Title': '"The Iron Throne"', 
'Directed by': 'David Benioff & D. B. Weiss', 
'Written by': 'David Benioff & D. B. Weiss', 
'Original air date\u200a[20]': 'May\xa019,\xa02019\xa0(2019-05-19)', 
'U.S. viewers(millions)': '13.61[93]'

}
