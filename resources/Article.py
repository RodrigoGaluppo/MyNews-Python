from utils.NLPmodel import ArticleScraper
from flask_restful import Resource,reqparse
import re

def TextParser(text):
    return text.translate({ord('\"'):None}).translate({ord('\n'):None})

class Article(Resource):
    def post(self):
        arguments = reqparse.RequestParser()
        arguments.add_argument("link",type=str,required=True,help="the field link is required")
        data = arguments.parse_args()
       
        if data.get("link") != None and data.get("link") != "":

            ArticleData = ArticleScraper(link=data.get("link"))

            article = {
                "imgSrc":ArticleData.article.top_image,"title":ArticleData.article.title,"authors":ArticleData.article.authors,
                "description":ArticleData.article.summary,"content":ArticleData.article.text,"source":ArticleData.article.source_url
            }

            return {"article":article},200

        else:
            return {"message":"could not load the link"},404
        
        
