import nltk
from newspaper import Article
import numpy as np
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests

class ArticleScraper():

    
    def __init__(self,link):
        URL = self.ScrapeTrueLink(link)
        print(URL)
        self.Setup(link=URL)

    def ScrapeTrueLink(self,link):
        req = Request(link,headers={"User-Agent":"Mozila/5.0"})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage,"html5lib")
        URL = soup.find("meta",attrs={"http-equiv":"refresh"})["content"]
        return URL.split("URL=")[1].replace("'","")

    def Setup(self,link):
        self.article = Article(link)
        self.article.download()
        self.article.parse()
        nltk.download("punkt")
        self.article.nlp()