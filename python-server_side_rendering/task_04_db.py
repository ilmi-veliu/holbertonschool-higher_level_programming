#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


@app.route('/products')
def show_products():
    source = request.args.get('source')
    id = request.args.get('id')
    data = []

    if source == "json":
        try:
            with open("products.json", "r") as file:
                data = json.load(file)
        except Exception:
            return render_template("product_display.html", error="Error reading JSON file")

    elif source == "csv":
        try:
            with open("products.csv", "r") as file:
                reader = csv.DictReader(file)
                data = list(reader)
        except Exception:
            return render_template("product_display.html", error="Error reading CSV file")

    elif source == "sql":
        try:
            conn = sqlite3.connect("products.db")
            cursor = conn.cursor()

            if id:
                cursor.execute("SELECT * FROM Products WHERE id = ?", (id,))
            else:
                cursor.execute("SELECT * FROM Products")

            rows = cursor.fetchall()
            # Transformation en liste de dictionnaires
            for row in rows:
                data.append({
                    "id": row[0],
                    "name": row[1],
                    "category": row[2],
                    "price": row[3]
                })

            conn.close()
        except Exception:
            return render_template("product_display.html", error="Database error")


    else:
        return render_template("product_display.html", error="Wrong source")

    if id and source in ["json", "csv"]:
        data = [product for product in data if str(product["id"]) == id]
        if not data:
            return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=data)

if __name__ == "__main__":
    app.run(debug=True)
