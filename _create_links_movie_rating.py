import pandas as pd
from neo4j import GraphDatabase

def create_links(file_root, uri, username, password):

    print('Start: Creating HAS_RATING relationships between Movies and Ratings in remote DB instance:' + uri)
    
    # Load the CSV file
    df = pd.read_csv(file_root + 'users_movies_ratings.csv')
    
    # Initialize the Neo4j driver
    driver = GraphDatabase.driver(uri, auth=(username, password))

    # Get the first rating for each movieId (this will take the first rating based on the timestamp)
    first_ratings_df = df.sort_values(by="timestamp").groupby("movieId").first().reset_index()

    # Iterate over the first ratings and create relationships in Neo4j
    with driver.session() as session:
        for _, row in first_ratings_df.iterrows():
            movie_id = row['movieId']
            rating_value = row['rating']
            session.execute_write(create_movie_rating_relationship, movie_id, rating_value)

    # Close connection.
    driver.close()
    print("HAS_RATING relationships load complete.")

def create_movie_rating_relationship(tx, movie_id, rating_value):
    # Create the Movie and Rating nodes if they don't exist and create the relationship
    query = (
        "MERGE (m:Movies {movieId: $movie_id}) "
        "MERGE (r:Ratings {Rating: $rating_value}) "
        "MERGE (m)-[:HAS_RATING]->(r)"
    )
    tx.run(query, movie_id=movie_id, rating_value=rating_value)