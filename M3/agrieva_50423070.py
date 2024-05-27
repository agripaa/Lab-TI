from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello World</h1>"


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/<name>")
def my_self(name):
    return f"<h1>My name is {name}</h1>"


@app.route("/form")
def show_form():
    return render_template("form.html")


@app.route("/submit_form", methods=["POST"])
def submit_form():
    if request.method == "POST":
        nama = request.form["nama"]
        kelas = request.form["kelas"]
        npm = request.form["npm"]
        learn = request.form["learn"]

        return redirect(
            url_for("show_info", nama=nama, kelas=kelas, npm=npm, learn=learn)
        )


@app.route("/info")
def show_info():
    nama = request.args.get("nama")
    kelas = request.args.get("kelas")
    npm = request.args.get("npm")
    learn = request.args.get("learn")

    return f"""
        <h1>Informasi Mahasiswa:</h1>
        <p>Nama: {nama}</p>
        <p>Kelas: {kelas}</p>
        <p>NPM: {npm}</p>
        <p>Learn: {learn}</p>
    """


if __name__ == "__main__":
    app.run(debug=True)
