import os
from flask import Flask, request, abort, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Ingredients


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers', 'Content-Type,Authorization,true'
        )
        response.headers.add(
            'Access-Control-Allow-Methods', 'GET,POST,DELETE,OPTIONS,PATCH'
        )
        return response

    @app.route('/')
    def main():

        main_message = 'Hi There. Its running!'

        return main_message

    @app.route('/ingredients')
    def get_ingredients():
        ingredients = []
        try:

            selection = Ingredients.query.all()

            if selection:
                for ingredient in selection:
                    ingredients.append(ingredient.format())
                else:
                    ingredients.append(
                        'There are no ingridients yet. Why dont you put some?')
        except Exception as e:
            print(e)

        return.jsonify({
            'status': 'ok',
            'ingredients': ingredients
        })

    return app


APP = create_app()
