from flask_restful import Resource,reqparse

class Languages(Resource):
    def get(self):
        arguments = reqparse.RequestParser()

        return {"languages": [
        "pt-BR",
        "en-US",
        "es-ES"
        ] },200
