import os
from faker import Faker
from flask import Flask, render_template, jsonify
# from flask.ext.restful import Api, Resource

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

@app.route('/api/ninjas.json', methods = ['GET'])
def get_ninjas():
    f = Faker()
    ninjas = []
    for ninja in range(5):
        name = f.name()
        phone = f.phonenumber()
        city = f.city()

        next_ninja = {
                'name':name,
                'phone':phone,
                'city':city
                }
        ninjas.append(next_ninja)
    return jsonify( { 'ninjas': ninjas } )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
