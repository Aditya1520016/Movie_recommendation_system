# 🎬 Movie Recommendation System
A simple yet stylish web-based Movie Recommendation System built with **Python**, **Flask**, and **scikit-learn**. It uses content-based filtering to suggest similar movies based on the user's input title and optional filters like **genre** and **IMDb rating**.

## 🚀 Features
- 🔍 Search for a movie by title
- 🎯 Filter by genre and minimum IMDb rating
- 🤖 Intelligent recommendations using TF-IDF + Cosine Similarity
- 🌙 Modern dark-themed UI with glowing neon effects
- 🎨 Light/clean code structure and styling (HTML, CSS, Flask)
- 🔁 "Try Again" button for quick searches

## 🧠 How It Works
1. TF-IDF vectorization is applied to the **Description** field of each movie.
2. Cosine similarity is calculated between all movies.
3. Recommendations are generated based on similarity to the selected title.
4. Additional filters (genre, rating) are applied before final results are returned.

## 🗃 Dataset

- Sample dataset: `movies.csv`  
- Columns used: `Title`, `Genre`, `Description`, `Rating`, `Year`, etc.
- You can replace the dataset with your own (ensure it has `Description`, `Title`, and `Genre` columns).
- 
# Install dependencies
pip install -r requirements.txt
pip install Flask pandas scikit-learn
