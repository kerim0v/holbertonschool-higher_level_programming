import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_products():
    with open('products.json') as f:
        return json.load(f)


def read_csv_products():
    with open('products.csv', newline='') as f:
        reader = csv.DictReader(f)
        products = []
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
        return products


def read_sql_products():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    try:
        if source == 'json':
            data = read_json_products()
        elif source == 'csv':
            data = read_csv_products()
        elif source == 'sql':
            data = read_sql_products()
        else:
            return render_template('product_display.html', error="Wrong source", products=[])
    except sqlite3.Error as e:
        return render_template('product_display.html', error=f"Database error: {e}", products=[])

    if product_id is not None:
        product_id = int(product_id)
        data = [p for p in data if p['id'] == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found", products=[])

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)