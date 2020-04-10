from flask import Flask
app = Flask(__name__)

# Dictionary to add and delete elemets
stores= {
  "store1": [
    {
      "items": [
        {
          "name": "cookie",
          "price": 20
        },
        {
          "name": "chocolate",
          "price": 40
        }
      ]
    }
  ],
  "store2": [
    {
      "items": [
        {
          "name": "chips",
          "price": 20
        },
        {
          "name": "candies",
          "price": 60
        }
      ]
    }
  ],
  "store3": [
    {
      "items": [
        {
          "name": "peanuts",
          "price": 10
        },
        {
          "name": "candies",
          "price": 50
        }
      ]
    }
  ]
}

@app.route('/')
def hello_world():
    return 'Great!!!, This is my first web page'

@app.route('/all_stores')
def all_stores():
    return stores