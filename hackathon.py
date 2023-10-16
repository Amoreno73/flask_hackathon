from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return (f"testing")

# f = open('movies.json')
# data = json.load(f)

# def home():
#     pass
# def movie_detail(title):
#     pass
# def genre_page(genre_name):
#     pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)

