import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#Add Url
url = ''
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find('table', attrs={'id':'example'})
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td', class_="text-left") 
    contents = cols[0].contents
    
    
    print(contents[0].strip())
    if (len(contents) > 2):
        print(contents[2].text.strip())
    
    print(cols[1].text.strip())
    print("\n")
