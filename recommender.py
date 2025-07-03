import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        
        self.df.reset_index(inplace=True)
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.df['Description'])
        self.similarity = cosine_similarity(self.tfidf_matrix)

    def get_recommendations(self, title, genre=None, min_rating=None, top_n=5):
        if title not in self.df['Title'].values:
            return []

        idx = self.df[self.df['Title'] == title].index[0]
        sim_scores = list(enumerate(self.similarity[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:]

        recommendations = []
        for i, score in sim_scores:
            movie = self.df.iloc[i]
            if genre and genre.lower() not in str(movie['Genre']).lower():
                continue
            if min_rating and movie.get("Rating", 0) < float(min_rating):
                continue
            recommendations.append(movie)
            if len(recommendations) == top_n:
                break

        return recommendations