from flask import Flask, render_template, request


app = Flask(__name__)

movies = [
    {"title": "The Matrix", "year": 1999, "cast": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"], "genre": "Sci-Fi"},
    {"title": "Inception", "year": 2010, "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"], "genre": "Sci-Fi"},
    {"title": "The Godfather", "year": 1972, "cast": ["Marlon Brando", "Al Pacino", "James Caan"], "genre": "Crime"},
    {"title": "Pulp Fiction", "year": 1994, "cast": ["John Travolta", "Uma Thurman", "Samuel L. Jackson"], "genre": "Crime"},
    {"title": "The Shining", "year": 1980, "cast": ["Jack Nicholson", "Shelley Duvall", "Danny Lloyd"], "genre": "Horror"}
  ]

@app.route("/home.html")
def index():
    return render_template('home.html', movies = movies)

# @app.route("/")
# def home():
#     pass

# @app.route("/movie/<title>")
# def movie_detail(title):
#     pass

# @app.route("/genre/<genre.name>")
# def genre_page(genre_name):
#     pass


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)

