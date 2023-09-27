# Pizza Restaurants

#### Created By Martin Nyaga 22-9-2023


## Introduction

For this assessment, you'll be working with a Pizza Restaurant domain.

The job here is to build out the Flask API to add the functionality described in the deliverables below.

Test you endpoints as stated below

Running the Flask server and using Postman to make requests

## Models

You need to create the following relationships:

- A `Restaurant` has many `Pizzas` through `RestaurantPizza`
- A `Pizza` has many Restaurants through `RestaurantPizza`
- A `RestaurantPizza` belongs to a `Restaurant` and belongs to a `Pizza`
  Start by creating the models and migrations for the following database tables:

## Validations

Add validations to the `RestaurantPizza` model:

- Must have a price between 1 and 30
  Add validations to `Restaurant` Model:

- must have a name less than 50 words in length
- must have a unique name

# Routes

Set up the following routes. Make sure to return JSON data in the format specified along with the appropriate HTTP verb.

## GET /restaurants

Return JSON data in the format below:

```
[
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "Good Italian, Ngong Road, 5th Avenue"
  },
  {
    "id": 2,
    "name": "Pizza Hut",
    "address": "Westgate Mall, Mwanzi Road, Nrb 100"
  }
]
```

## GET /restaurants/:id

If the `Restaurant` exists, return JSON data in the format below:

```
{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Italian, Ngong Road, 5th Avenue",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}
```

If the `Restaurant` does not exist, return the following JSON data, along with the appropriate HTTP status code:

```
{
  "error": "Restaurant not found"
}
```

## DELETE /restaurants/:id

If the `Restaurant` exists, it should be removed from the database, along with any `RestaurantPizzas` that are associated with it (a `RestaurantPizza` belongs to a `Restaurant`, so you need to delete the `RestaurantPizzas` before the `Restaurant` can be deleted).

After deleting the `Restaurant`, return an empty response body, along with the appropriate HTTP status code.

If the `Restaurant` does not exist, return the following JSON data, along with the appropriate HTTP status code:

```
{
  "error": "Restaurant not found"
}
```

## GET /pizzas

Return JSON data in the format below:

```
[
  {
    "id": 1,
    "name": "Cheese",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  {
    "id": 2,
    "name": "Pepperoni",
    "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
  }
]
```

## POST /restaurant_pizzas

This route should create a new `RestaurantPizza` that is associated with an existing `Pizza` and `Restaurant`. It should accept an object with the following properties in the body of the request:

```
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```

If the `RestaurantPizza` is created successfully, send back a response with the data related to the `Pizza`:

```
{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}
```

If the `RestaurantPizza` is not created successfully, return the following JSON data, along with the appropriate HTTP status code:

```
{
  "errors": ["validation errors"]
}
```

## Technologies used.

- Python3
- Flask
- SQLAlchemy

## Project Setup

1. Clone the repository: `git clone <repository-url>`.
2. Switch to a virtual environment `pipenv shell`.
3. Install dependencies: `pipenv install`
4. Navigate to cloned repository: `cd Pizza-Restaurants--P4--W1`.
5. Navigate to the server folder.
6. Run the `app.py` script.
7. Test your endpoints with the given routes in postman.
    - /restaurant - gives you a list of all restaurants
    - /restaurant/{id} - gives you a restaurant with specific id
    - /pizza - gives you a list of pizzas
    - /api/docs - gives you the api documentation from swagger


## Known Bugs

No known bugs at the moment

## Support and contact details 

To make a contribution to the code used or any suggestions you can click on the contact link and email me your suggestions.

- Email: martin.nyaga@student.moringaschool.com

## License

Copyright (c) {{ 2023 }}, {{ MARTIN NYAGA }}

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.