import pandas as pd
from neo4j import GraphDatabase

def create_links(file_root, uri, username, password):

    print('Start: Creating BELONGS_TO relationships between Movies and Genres in remote DB instance:' + uri)
    
    # Load the CSV file
    df = pd.read_csv(file_root + 'tmp_movies_genres.csv')
    
    # Initialize the Neo4j driver
    driver = GraphDatabase.driver(uri, auth=(username, password))

    # Iterate over the rows in the dataframe and create the relationships
    with driver.session() as session:
        for _, row in df.iterrows():
            movie_id = row['movieId']
            genre_name = row['genres']
            session.execute_write(create_movie_genre_relationship, movie_id, genre_name)

    # Close the driver
    driver.close()
    print("BELONGS_TO relationships load complete.")

def create_movie_genre_relationship(tx, movie_id, genre_name):
    # Create the Movie and Genre nodes if they don't exist and create the relationship
    query = (
        "MERGE (m:Movies {movieId: $movie_id}) "
        "MERGE (g:Genres {Genres: $genre_name}) "
        "MERGE (m)-[:BELONGS_TO]->(g)"
    )
    tx.run(query, movie_id=movie_id, genre_name=genre_name)

