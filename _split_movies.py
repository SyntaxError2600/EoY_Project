# This will split the defualt movies.csv file into seperate movies_only.csv and movies_genres.csv files..  

import pandas as pd

def split_movies(file_root):

    print("Start: Splitting Movies.csv into movies_only.csv and movies_genres.csv files.")

    # Load the CSV file
    df = pd.read_csv(file_root + 'movies.csv')

    # First file: movieId and title
    df_movies = df[['movieId', 'title']]

    # Second file: movieId and one row per genre
    df_genres = df[['movieId', 'genres']].copy()
    df_genres = df_genres.assign(genres=df_genres['genres'].str.split('|')).explode('genres').reset_index(drop=True)

    # Save the files
    df_movies.to_csv(file_root + 'tmp_movies.csv', index=False)
    df_genres.to_csv(file_root + 'tmp_movies_genres.csv', index=False)

    print("Complete.")