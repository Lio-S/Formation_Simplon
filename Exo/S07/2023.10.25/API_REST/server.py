import json
from flask import Flask, request

app = Flask(__name__)
app.testing = True # <> à flask --app server.py --debug run
app.config.update( # Update automatique des templates 
    TEMPLATES_AUTO_RELOAD = True
)

@app.route("/products", methods=["GET"])
def get_products():
    products = [
        {
            "name": "Product 1",
            "price": 100
        },
        {
            "name": "Product 2",
            "price": 200
        },
    ]
    response = json.dumps(products)
    return response, 200

if __name__ == "__main__":
    app.run(port=8080)