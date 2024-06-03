from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

default_data = [
    {"id": 1, "name": "Toko Sepatu", "items":{"name": "Adidas", "price": 9000}},
    {"id": 2, "name": "Toko Baju", "items":{"name": "Adidas", "price": 9000}}
]

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/pilihan", methods=["GET"])
def pilihanGet():
    return jsonify({"status": 200, "datas": default_data}), 200

@app.route("/pilihan/post", methods=["POST"])
def pilihanPost():
    if request.method == "POST":
        new_store = request.get_json()
        
        if not all(key in new_store for key in ("id", "name", "items")):
            return jsonify({"message": "Missing required fields"}), 400

        if any(store["id"] == new_store["id"] for store in default_data):
            return (
                jsonify({"message": "Store with this ID already exists"}),
                409,
            )

        default_data.append(new_store)
        return jsonify({"message": "add data succesfully", "new data": new_store}), 201
if __name__ == '__main__':
    app.run(debug=True)