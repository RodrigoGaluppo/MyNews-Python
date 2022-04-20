from flask_restful import Resource,reqparse
from utils.langs import langsList
class Languages(Resource):
    def get(self):
        arguments = reqparse.RequestParser()

        return {"languages": langsList},200
