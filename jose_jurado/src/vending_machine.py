import os
import json

from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)

app.config.from_file("config.json", load=json.load)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        print(request.form)
    return render_template("base.html")


@app.route("/utils/list-valid-coins")
def list_valid_coins():
    valid = {}
    coins = app.config["COINS"]
    for coin, properties in coins.items():
        if properties["validity"] == "True":
            valid[coin] = properties

    return valid


@app.route("/utils/list-inventory-options")
def list_inventory_options():
    print(app.config["INVENTORY"])
    return app.config["INVENTORY"]


if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)
