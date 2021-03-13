from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import numpy as np

class Scraper():
    def __init__(self,lang,query) :

        if lang == "en-US":
            self.root = f"https://news.search.yahoo.com/search?p={query}&b="
        else:

            location = lang.split("-")[1].lower()
            self.root = f"https://{location}.news.search.yahoo.com/search?p={query}&b="

    def Start(self):
        news = np.array([])
        for c in range(0,2):
            
            if c == 0:
                link = self.root + "1"

            elif c == 1:
                link = self.root + "11"

            elif c == 2:
                link = self.root + "21"

            response = requests.get(link,headers={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'pt-BR,en;q=0.9',
                'referer': 'https://www.google.com',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.44'
            })

            with requests.Session() as c:
                soup = BeautifulSoup(response.text,"html5lib")
                #print(soup)

                listItems = soup.find_all("div","NewsArticle") 
                
                for item in listItems:
                    try:
                        title = item.find("h4", "s-title").text
                        source = item.find("span", "s-source").text
                        timeStamp = item.find("span","s-time").text
                        link = item.find("a").get("href")

                        imgSrc = item.find("img","s-img").get("data-src")

                        news = np.append(news,{"link":link,"title":title,"source":source,"timeStamp":timeStamp,"imgSrc":imgSrc})
                    except:pass

        return news.tolist()