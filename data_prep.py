# Remember to pip install pandas
# Used the Data from: MovieLens' GroupLens Research that collected and made available rating datasets from their movie web site: https://grouplens.org/datasets/movielens/
# This will split the defualt movies.csv file to seperate out into movies_only and movies_genres files..  

import pandas as pd

# Load the uploaded CSV file
df = pd.read_csv(r"C:\\Users\\Frank\\Desktop\\EoY_Project\data\\movies.csv")

print("Start: Splitting Movies.csv into movies_only and movies_genres files.")

# First file: movieId and title
df_movies = df[['movieId', 'title']]

# Second file: movieId and one row per genre
df_genres = df[['movieId', 'genres']].copy()
df_genres = df_genres.assign(genres=df_genres['genres'].str.split('|')).explode('genres').reset_index(drop=True)

# Save the files
movies_file = "C:\\Users\\Frank\\Desktop\\EoY_Project\\data\movies_only.csv"
genres_file = "C:\\Users\\Frank\\Desktop\\EoY_Project\\data\movies_genres.csv"

df_movies.to_csv(movies_file, index=False)
df_genres.to_csv(genres_file, index=False)

print("Complete: Splitting Movies.csv into movies_only and movies_genres files.")

# Used the Neo4j Aura file import to create the Movies nodes.