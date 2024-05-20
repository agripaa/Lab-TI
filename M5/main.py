from flask import Flask, request, jsonify

app = Flask(__name__)
datas = [
    {
        "id": 1,
        "penjual": "asep",
        "items": [{"name": "Bunga Kecombrang", "price": 5000}],
        "category_toko": [{"nama_toko": "Bunga terakhir", "berjualan": "bunga"}],
    },
    {
        "id": 2,
        "penjual": "ujang",
        "items": [{"name": "Buku Tangkuban Perahu", "price": 15000}],
        "category_toko": [{"nama_toko": "Buku Indonesia", "berjualan": "Buku"}],
    },
    {
        "id": 3,
        "penjual": "septian",
        "items": [{"name": "Kamera SP500", "price": 4000000}],
        "category_toko": [{"nama_toko": "Buku Indonesia", "berjualan": "Buku"}],
    },
    {
        "id": 4,
        "penjual": "djarot",
        "items": [{"name": "mesin kopi", "price": 230000}],
        "category_toko": [{"nama_toko": "kopi ati", "berjualan": "kopi"}],
    },
    {
        "id": 5,
        "penjual": "udin",
        "items": [{"name": "baju bayi", "price": 340000}],
        "category_toko": [
            {"nama_toko": "baby indonesia", "berjualan": "aksesoris bayi"}
        ],
    },
]


@app.route("/store")
def get_all_stores():
    return jsonify(datas)


@app.route("/store/<int:store_id>")
def get_store_by_id(store_id):
    store = next((store for store in datas if store.get("id") == store_id), None)
    if store:
        return jsonify(store)
    return jsonify({"message": "Store not found"}), 404


@app.route("/store", methods=["POST"])
def add_store():
    new_store = request.get_json()
    if not all(key in new_store for key in ("id", "penjual", "items", "category_toko")):
        return jsonify({"message": "Missing required fields"}), 400

    if any(store["id"] == new_store["id"] for store in datas):
        return (
            jsonify({"message": "Store with this ID already exists"}),
            409,
        )

    datas.append(new_store)
    return jsonify({"message": "add data succesfully", "new data": new_store}), 201


@app.route("/store/<int:store_id>", methods=["DELETE"])
def delete_store(store_id):
    global datas
    datas = [store for store in datas if store.get("id") != store_id]
    return jsonify({"message": "Store deleted"})


@app.route("/store/<int:store_id>", methods=["PATCH"])
def update_store_partially(store_id):
    store = next((store for store in datas if store.get("id") == store_id), None)
    if not store:
        return jsonify({"message": "Store not found"}), 404

    update_data = request.get_json()
    for key in update_data:
        if key in store:
            store[key] = update_data[key]
    return jsonify({"message": "Store updated", "store": store})


@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Not found"}), 404


@app.route("/")
def home():
    return "Hello peeps!"


if __name__ == "__main__":
    app.run(debug=True)
