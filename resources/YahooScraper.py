from utils.YScraper import Scraper
from flask_restful import Resource,reqparse

class YahooScraper(Resource):
    def post(self):
        arguments = reqparse.RequestParser()
        arguments.add_argument("query",type=str,required=True,help="the field query is required")
        arguments.add_argument("lang",type=str,required=False)
        #arguments.add_argument("page",type=int,required=False)
        
        data = arguments.parse_args()

        default_language = "pt-BR"
        
        if data.get("lang"):
            default_language =  data.get("lang")

        newsScraper = Scraper(lang=default_language,query=data.get("query"))
        news = newsScraper.Start()
        return {"news": news},200
        
