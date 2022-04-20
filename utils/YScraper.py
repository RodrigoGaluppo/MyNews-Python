from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import numpy as np
from slugify import slugify

class Scraper():
    def __init__(self,lang,query) :

        if lang == "en-US":
            self.root = f"https://news.search.yahoo.com/search?p={query}&b="
        else:
            location = lang.split("-")[1].lower()
            print(location)
            self.root = f"https://{location}.news.search.yahoo.com/search?p={query}&b="
            print(self.root)

        if query == "":
            self.root = f"https://news.search.yahoo.com/search?p=news&b="

    def Start(self):
        news = np.array([])
        for c in range(0,2):

            link = self.root + f"{1 + c * 10 }"

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
                        link = item.find("a").get("href").split("https://")[1].split("RU=")[1]
                        link="URL="+link
                        slug = slugify(title)
                    except:
                        pass

                    try:
                        description = item.find("p","s-desc").text
                    except:
                        description = ""

                    try:
                        imgSrc = item.find("img","s-img").get("data-src")

                        if(imgSrc == None):
                            imgSrc = "https://s.yimg.com/rz/stage/p/yahoo_news_en-US_h_p_newsv2.png"
                    except:
                        imgSrc = "https://s.yimg.com/rz/stage/p/yahoo_news_en-US_h_p_newsv2.png"

                    news = np.append(news,{"link":link,"title":title,"description":description,"source":source,"timeStamp":timeStamp,"slug":slug,"imgSrc":imgSrc})


        return news.tolist()
