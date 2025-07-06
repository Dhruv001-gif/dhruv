# Movie dataset using a dictionary
movies = {
    "Inception": {"genres": ["Action", "Sci-Fi", "Thriller"]},
    "The Matrix": {"genres": ["Action", "Sci-Fi"]},
    "Titanic": {"genres": ["Romance", "Drama"]},
    "The Notebook": {"genres": ["Romance", "Drama"]},
    "John Wick": {"genres": ["Action", "Thriller"]},
    "Interstellar": {"genres": ["Sci-Fi", "Drama"]},
    "The Godfather": {"genres": ["Crime", "Drama"]},
    "Mad Max: Fury Road": {"genres": ["Action", "Adventure"]},
    "The Shawshank Redemption": {"genres": ["Drama", "Crime"]},
    "Avengers: Endgame": {"genres": ["Action", "Adventure", "Sci-Fi"]}
}

# Function to recommend movies by matching genres
def recommend_by_genre(movie_title, movies_dict, top_n=3):
    if movie_title not in movies_dict:
        return f"Movie '{movie_title}' not found in the dataset."

    input_genres = set(movies_dict[movie_title]["genres"])
    similarity_scores = {}

    for other_movie, data in movies_dict.items():
        if other_movie == movie_title:
            continue
        other_genres = set(data["genres"])
        # Jaccard similarity (intersection over union)
        score = len(input_genres & other_genres) / len(input_genres | other_genres)
        similarity_scores[other_movie] = score

    # Sort by similarity score (descending)
    recommended = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)

    return [movie for movie, score in recommended[:top_n] if score > 0]

# Example usage
movie_to_search = input("")
recommendations = recommend_by_genre(movie_to_search, movies)

print(f"Because you watched '{movie_to_search}', you may also like:")
for i, rec in enumerate(recommendations, 1):
    print(f"{i}. {rec}")
