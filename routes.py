import os
from flask import Flask, render_template

app = Flask(__name__)
app.config.update(
        DEBUG = True,
)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/ninjas")
def ninjas():
    return render_template("ninjas.html")

@app.route('/ninjas/api/list', methods = ['GET'])
def get_ninjas():
    return jsonify( { 'ninjas': ninjas } )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
