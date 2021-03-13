from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import numpy as np

class Scraper():
    def __init__(self,lang,query):

        location = lang.split("-")[1]

        self.root = "https://news.google.com"
        link = f"https://news.google.com/search?q={query}&hl={lang}"
        req = Request(link,headers={"User-Agent":"Mozila/5.0"})
        self.webpage = urlopen(req).read()

    def Start(self):
        with requests.Session() as c:
            
            soup = BeautifulSoup(self.webpage,"html5lib")
            listItems = np.array(soup.find_all("div",attrs={"class":"NiLAwe"})[:20])
            
            news = np.array([])

            for item in listItems:
                
                try:
                    raw_link = self.root + "/" + item.find("a",href=True)["href"].split("./")[1]
                    title = (item.find("a",attrs={"class":"DY5T1d RZIKme"}).get_text())
                    source = (item.find("a",attrs={"class":"wEwyrc AVN2gc uQIVzc Sksgp"}).get_text())
                    timeStamp = (item.find("time",attrs={"class":"WW6dff uQIVzc Sksgp"}).get_text())
                    imgSrc = item.find("img",src=True)["src"]

                except:
                    
                    pass

                news = np.append(news,{"link":raw_link,"title":title,"source":source,"timeStamp":timeStamp,"imgSrc":imgSrc})
     
        return news.tolist()