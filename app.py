from flask import Flask
from flask_restful import Api, Resource
from rutas import crear_rutas


app = Flask(__name__)
api= Api(app)
crear_rutas(api)



app.run(port=8080, debug=True)
