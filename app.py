from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tablaDePosiciones")
def tablaPosiciones():
    return render_template("tablaDePosiciones.html")
@app.route("/copaArgentina")
def copaArgentina():
    return render_template("copa-argentina.html")

if __name__ == "__main__":
    app.run(debug=True)
