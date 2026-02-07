from flask_restful import (Resource)
from flask import make_response, render_template

class PantallaInicio(Resource):
    def get(self):
        contenido = render_template("index.html")
        return make_response(contenido)


class HolaMundo(Resource):
    def get(self):
        return{'hola':'mundo'}