import requests
from bs4 import BeautifulSoup as BS
import json
data='C:/test.json'
url="https://www.scrapehero.com/how-to-scrape-amazon-product-reviews/"

r=requests.get(url)
print(r.text)
soup=BS(r.content,features="html.parser")
links=soup.find_all("p")
#print soup.prettify()

for link in links:
    connections=link.text
    f=open(data,'w')
    f.write(json.dumps(connections,indent=1))
    f.close()
