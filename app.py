from flask import Flask, render_template, request
from recommender import MovieRecommender

app = Flask(__name__)
recommender = MovieRecommender("data/movies.csv")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    title = request.form.get("title")
    genre = request.form.get("genre")
    rating = request.form.get("rating")

    results = recommender.get_recommendations(title, genre, rating)
    return render_template("result.html", movies=results, input_title=title)

if __name__ == "__main__":
    app.run(debug=True)