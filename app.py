from flask import Flask
from flask_restful import Api
from resources.GoogleScraper import GoogleScraper
from resources.Article import Article
from resources.YahooScraper import YahooScraper
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)

@app.route("/")
def index():
    return "<h1>please access the news in the required endpoints</h1>"

api.add_resource(YahooScraper,"/yahoonews")
api.add_resource(GoogleScraper,"/googlenews")
api.add_resource(Article,"/article")

cors = CORS(app)

if __name__ == "__main__":
    print("running")
    app.run()