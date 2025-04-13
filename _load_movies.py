import pandas as pd
from neo4j import GraphDatabase

def load(file_root, uri, username, password):
    
    print('Start: Importing movies.csv in remote DB instance:' + uri)
    
    # Load the CSV file
    df = pd.read_csv(file_root + 'movies.csv')
    
    # Initialize the Neo4j driver
    driver = GraphDatabase.driver(uri, auth=(username, password))
    
    # Iterate over the rows in the dataframe and create Movie nodes in Neo4j
    with driver.session() as session:
        for _, row in df.iterrows():
            movie_id = row['movieId']
            title = row['title']
            session.write_transaction(load_movie, movie_id, title)
            
    # Close connection.
    driver.close()
    print('Movie load complete.')
    
def load_movie(tx, movie_id, title):
    # Create the Movie node with movieId and title properties
    query = (
        "MERGE (m:Movies {movieId: $movie_id, title: $title})"
    )
    tx.run(query, movie_id=movie_id, title=title)