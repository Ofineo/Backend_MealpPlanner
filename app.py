import os
from flask import Flask, request, abort, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Ingredients, Meals


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

        main_message = 'Hi There. Backend it\'s running!'

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
            'status': True,
            'ingredients': ingredients
        })

    @app.route('/meals')
    def get_meals():

        meals = []

        try:
            selection = Meals.query.all()

            if selection:
                for meal in selection:
                    meals.append(meal.format())
            else:
                meals.append('Nothing here yat')
        except Exception as e:
            print(e)

        return jsonify({
            'status': True,
            'meals': meals
        })

    @app.route('/meals', methods=['POST'])
    def post_meal():
        res = request.get_json()
        print(res)

        try:
            ingredient = Ingredients(
                name='radish',
                quantity=3
            )

            meal = Meals(
                category=res['category'],
                title=res['title'],
                affordability=res['affordability'],
                complexity=res['complexity'],
                imageUrl=res['imageUrl'],
                duration=res['duration'],
                steps=res['steps'],
                glutenfree=res['glutenfree'],
                vegan=res['vegan'],
                vegetarian=res['vegetarian'],
                lactosefree=res['lactosefree'],
            )

            meal.insert()

        except Exception as e:
            print('------------------------------------------', e)

        return jsonify({
            'status': True,
            'meals': meal.format()
        })

    @app.route('/ingredients', methods=['POST'])
    def add_ingredient():
        res = request.get_json()
        print(res)

        try:
            ingredient = Ingredients()

            if 'name' in res:
                ingredient.name = res['name']
            else:
                raise Exception("it's missing the ingredient name key:value")

            if 'quantity' in res:
                ingredient.quantity=res['quantity']
            else:
                raise Exception("it's missing the ingredient quantity key:value")

            if 'meal_id' in res:
                ingredient.meal_id =1
            else:
                ingredient.meal_id =1
                #raise Exception("it's missing the ingredient meal_id key:value")

            ingredient.insert()

        except Exception as e:
            print(e)

        new_ingredient = Ingredients.query.filter(Ingredients.name == res['name'], Ingredients.meal_id==1).one_or_none()
        print('-----------------',new_ingredient)

        return jsonify({
            'status': True,
            'ingredient': new_ingredient.format()
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
