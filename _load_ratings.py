import pandas as pd
from neo4j import GraphDatabase

def load(file_root, uri, username, password):

    print('Start: Importing ratings.csv in remote DB instance:' + uri)
    
    # Load the CSV file
    df = pd.read_csv(file_root + 'ratings.csv')
    
    # Initialize the Neo4j driver
    driver = GraphDatabase.driver(uri, auth=(username, password))
    
    # Iterate over the rows in the dataframe and create Rating nodes in Neo4j
    with driver.session() as session:
        for _, row in df.iterrows():
            rating_name = row['ratings']
            session.write_transaction(load_rating, rating_name)

    # Close the driver
    driver.close()
    print("Ratings load complete.")

def load_rating(tx, rating_name):
    # Create the Rating node with the rating name property
    query = (
        "MERGE (g:Ratings {name: $rating_name})"
    )
    tx.run(query, rating_name=rating_name)

