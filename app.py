from flask import Flask

app = Flask(__name__)

@app.route("/", method=['GET'])
def home():
    print "Hello"

if __name__ == "__main__":
    app.run()

