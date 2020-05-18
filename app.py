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
                    'There are no ingredients yet. Why dont you put some?')
        except Exception as e:
            print(e)

        return jsonify({
            'status': 'ok',
            'ingredients': ingredients
        })

    @app.route('/ingredients', methods=['POST'])
    def add_ingredient():
        res = request.get_json()

        try:
            ingredient = Ingredients(
                name=res['name'],
                quantity=res['quantity']
            )

            ingredient.insert()

        except Exception as e:
            print(e)

        return jsonify({
            'status': True,
            'ingredient': ingredient.format()
        })

    @app.route('/ingredients/<int:id>', methods=['PATCH'])
    def patch_ingredient(id):
        res = request.get_json()

        try:
            selection = Ingredients.query.filter(
                Ingredients.id == id).one_or_none()
            if 'name' in res:
                selection.name = res['name']
            if 'quantity' in res:
                selection.quantity = res['quantity']

            selection.update()
        except Exception as e:
            print(e)
        return jsonify({
            'status': True,
            'ingredient': selection.format()
        })

    return app


APP = create_app()
