#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

@app.route('/products')
def show_product():
    source = request.args.get('source')
    id = request.args.get('id')

    data = []

    if source == "json":
        with open('products.json', "r") as file:
            data = json.load(file)

    elif source == "csv":
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            data = list(reader)

    else:
        return render_template("product_display.html", error="Wrong source")

    if not id or id.strip() == "":
        return render_template("product_display.html", error="Missing product ID")

    filtered = [product for product in data if str(product["id"]) == id]

    if not filtered:
        return render_template("product_display.html", error="Product not found")
    else:
        return render_template("product_display.html", products=filtered)
