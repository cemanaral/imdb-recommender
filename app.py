from flask import Flask, render_template, request
from data import movie_names, critics, get_ratings
from recommendations import getRecommendations

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        results = {}
        
        # find imdb url
        url = request.form.get("ratings-url")

        # parse ratings
        ratings = get_ratings(url)
        critics["user"] = ratings

        # run getRecommendations
        results = getRecommendations(critics, "user")
        results = {score: imdbID for score, imdbID in results if score > 3}

        return render_template("index.html", results=results, movie_names=movie_names)
    
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
