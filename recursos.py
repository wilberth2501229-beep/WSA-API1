from flask_restful import (Resource)
from flask import make_response, render_template, request
from extensiones import inicializar_db

cliente = inicializar_db()

class PantallaInicio(Resource):
    def get(self):
        contenido = render_template("index.html")
        return make_response(contenido)


class HolaMundo(Resource):
    def get(self):
        return{'hola':'mundo'}

class LoginPage(Resource):
    def get(self):
        contenido = render_template("loginpage.html")
        return make_response(contenido)
    def post(self):
        print('Esto se ejecuta cuando se llama un post')
        datos = request.form.to_dict()
        print(datos)
        return (datos)

class SignUpPage(Resource):
    def get(self):
        contenido = render_template("signup.html")
        return make_response(contenido)
    def post(selfs):
        datos = request.form.to_dict()
        return cliente.table('usuarios').insert(datos).execute()

