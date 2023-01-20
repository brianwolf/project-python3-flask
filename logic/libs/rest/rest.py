"""
Rest
----
1.0.0

Dependencias:
* logger
* exception
* reflection

Configura el app de Flask para cargar blueprints dinamicamente, agregar JSON decoders que sigan un estandar, 
agregar handlers para manejo automatico de errores, entre otros.
"""
from flask import Flask
from logic.libs.reflection import reflection
from logic.libs.rest.src.decorators import add_decorators
from logic.libs.rest.src.json import config_encoders


def setup(app, path) -> Flask:
    '''
    Configura la app de Flask
    '''
    app.config.setdefault('ERROR_INCLUDE_MESSAGE', False)
    add_decorators(app)
    config_encoders(app)

    load_routes_by_regex_path(app, path)

    return app


def load_routes_by_regex_path(app: Flask, path: str):
    '''
    Carga los blueprints al app de Flask
    '''
    for module in reflection.load_modules_by_regex_path(path):
        if hasattr(module, 'blue_print'):
            app.register_blueprint(module.blue_print)
