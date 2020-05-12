from bs4 import BeautifulSoup
import requests

data='C:/WEBSCRAPING.txt'
def getLinks(url):
    html_page = url
    r = requests.get(html_page)
    soup = BeautifulSoup(r.text,'html.parser')
    links = []

    for link in soup.findAll('a'):
        links.append(link.get('href'))
    
    return links

alllinks = getLinks("https://nptel.ac.in/courses/106/105/106105184/")

for linky in alllinks:
    f=open(data,'a')
    f.write(linky+'\n')
    f.close()
    
