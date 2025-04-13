import pandas as pd
from neo4j import GraphDatabase

def load(file_root, uri, username, password):

    print('Start: Importing genres.csv in remote DB instance:' + uri)
    
    # Load the CSV file
    df = pd.read_csv(file_root + 'genres.csv')
    
    # Initialize the Neo4j driver
    driver = GraphDatabase.driver(uri, auth=(username, password))
    
    # Iterate over the rows in the dataframe and create Genre nodes in Neo4j
    with driver.session() as session:
        for _, row in df.iterrows():
            genre_name = row['genres']
            session.write_transaction(load_genre, genre_name)

    # Close the driver
    driver.close()
    print("Genres load complete.")

def load_genre(tx, genre_name):
    # Create the Genre node with the genre name property
    query = (
        "MERGE (g:Genres {name: $genre_name})"
    )
    tx.run(query, genre_name=genre_name)