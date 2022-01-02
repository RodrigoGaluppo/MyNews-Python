from utils.YScraper import Scraper
from flask_restful import Resource,reqparse

class YahooScraper(Resource):

    def post(self):
        arguments = reqparse.RequestParser()

        arguments.add_argument("query",type=str,help = "the field query is required")
        arguments.add_argument("lang",type=str,required=False)
        #arguments.add_argument("page",type=int,required=False)

        data = arguments.parse_args()

        default_language = "en-US"
        default_query = "news"

        if data.get("lang"):
            if(data.get("lang") in ["pt-BR",
            "en-US",
            "es-ES",
            "en-UK"]):
                default_language =  data.get("lang")

        newsScraper = Scraper(lang=default_language,query=default_query)
        try:
            news = newsScraper.Start()
        except:
            return {"news": []},400
        return {"news": news},200
