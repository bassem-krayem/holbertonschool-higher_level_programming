import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json') as json_file:
        data = json.load(json_file)
    item_list = data.get('items', [])
    return render_template('items.html', items = item_list)


def read_json(file_path):
    """Read and parse JSON file."""
    try:
        with open(file_path) as json_file:
            data = json.load(json_file)
            return data  # Return the list directly
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
        return []


def read_csv(file_path):
    """Read and parse CSV file."""
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]
    except FileNotFoundError as e:
        print(f"Error reading CSV file: {e}")
        return []


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source. Please use 'json' or 'csv'.")

    products = []
    if source == 'json':
        products = read_json('products.json')
    elif source == 'csv':
        products = read_csv('products.csv')

    # Filter by ID if provided
    if product_id is not None:
        products = [product for product in products if int(product['id']) == product_id]
        if not products:  # If no products found
            return render_template('product_display.html', error="Product not found.")

    return render_template('product_display.html', products=products)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
