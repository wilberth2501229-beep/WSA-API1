from recursos import *


def crear_rutas (api):

    api.add_resource(HolaMundo, '/hola')
    api.add_resource(PantallaInicio,'/')
    api.add_resource(LoginPage, '/login')
    api.add_resource(SignUpPage, '/signup')



