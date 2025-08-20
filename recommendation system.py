import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

data = {
    'movie_id': [1,2,3,4,5],
    'title': ["Inception", "The Matrix", "Interstellar", "The Prestige", "The Dark Knight"],
    'genre': ["Sci-Fi Thriller", "Sci-Fi Action", "Sci-Fi Adventure", "Mystery Thriller", "Action Crime"]
}

movies = pd.DataFrame(data)
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(movies['genre'])
similarity = cosine_similarity(genre_matrix)

def recommend(movie_title, n=3):
    if movie_title not in movies['title'].values:
        return ["Movie not found!"]
    idx = movies[movies['title'] == movie_title].index[0]
    scores = list(enumerate(similarity[idx]))
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    top_movies = [movies.iloc[i[0]]['title'] for i in sorted_scores[1:n+1]]
    return top_movies
    
movie_name = input("Enter a movie name: ")
print(f"\n🔎 Recommendations for '{movie_name}':")
print(recommend(movie_name))




