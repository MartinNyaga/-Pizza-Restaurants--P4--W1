#!/usr/bin/env python3

from flask import Flask, request, make_response,jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Home(Resource):
    def get(self):
        
        response_dict = {
            "/pizza": "Getting pizza resource",
            "/restaurant":"This gets you access to all restaurants",
            "message": "Welcome to the Restaurants API, Follow endpoints below",
        }
        
        response = make_response(
            response_dict,
            200
        )

        return response

api.add_resource(Home, '/')

class Restaurants(Resource):

    def get(self):

        restaurants = Restaurant.query.all()
        restaurant_list=[]
        for restaurant in restaurants:
            restaurant_dict = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
            }
            restaurant_list.append(restaurant_dict)
        response = make_response(jsonify(restaurant_list), 200)
        return response
    

api.add_resource(Restaurants, '/restaurant')

class RestaurantsByID(Resource):

    def get(self, id):

        response_dict = Restaurant.query.filter_by(id=id).first().to_dict()

        response = make_response(
            response_dict,
            200,
        )

        return response
    
    def delete(self, id):
        restaurant = Restaurant.query.filter(Restaurant.id == id).first()
        if restaurant:
            db.session.delete(restaurant)
            db.session.commit()
            response = make_response(jsonify({"message": "Restaurant deleted"}), 200)
        else:       
            response = make_response(jsonify({"error": "Restaurant not found"}), 404)
        return response

api.add_resource(RestaurantsByID, '/restaurant/<int:id>')

class Pizzas(Resource):
    def get(self):

        pizzas = Pizza.query.all()
        pizza_list=[]
        for pizza in pizzas:
            pizza_dict = {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients,
            }
            pizza_list.append(pizza_dict)
        response = make_response(jsonify(pizza_list), 200)
        return response
api.add_resource(Pizzas, '/pizza')

class RestaurantPizzas(Resource):
    
    def post(self):
        new_record = RestaurantPizza(
        price = request.form['price'],
        pizza_id = request.form['pizza_id'],
        restaurant_id = request.form['restaurant_id']
        )
        db.session.add(new_record)
        db.session.commit()
        
        record_dict = new_record.to_dict()
        response = make_response(jsonify(record_dict), 201)
        
        return response
    
api.add_resource(RestaurantPizzas, '/restaurantpizzas')

if __name__ == '__main__':
    app.run(port=5555, debug=True)