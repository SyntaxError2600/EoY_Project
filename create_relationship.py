# Remember to pip install pandas, neo4j
# Used the Data from: MovieLens' GroupLens Research that collected and made available rating datasets from their movie web site: https://grouplens.org/datasets/movielens/
# You'll need to run data_prep.py on the defualt movies.csv file to seperate out the Movies from the Genres..  
# This program is rerunnable and won't overwrite existing relationships. 

import pandas as pd
from neo4j import GraphDatabase

# Load the CSV file to inspect its contents
df = pd.read_csv(r"C:\\Users\\Frank\Desktop\\EoY_Project\\data\\movies_genres.csv")

print("Creating BELONGS_TO relationships between Movies and Genres.")

# Connect to the Neo4j database
uri = "neo4j+s://50189fd8.databases.neo4j.io"  # Neo4j instance URI
username = "neo4j"  # The username
password = "UtF4qlyIsbTYS4m36DDBX-pKmPA3KJdo1kfVehfXsdU"  # The password
# AURA_INSTANCEID=50189fd8
# AURA_INSTANCENAME=Instance01

# Initialize the Neo4j driver
driver = GraphDatabase.driver(uri, auth=(username, password))

def create_movie_genre_relationship(tx, movie_id, genre_name):
    # Create the Movie and Genre nodes if they don't exist and create the relationship
    query = (
        "MERGE (m:Movie {movie_id: $movie_id}) "
        "MERGE (g:Genre {Genres: $genre_name}) "
        "MERGE (m)-[:BELONGS_TO]->(g)"
    )
    tx.run(query, movie_id=movie_id, genre_name=genre_name)

# Iterate over the rows in the dataframe and create the relationships
with driver.session() as session:
    for _, row in df.iterrows():
        movie_id = row['movieId']
        genre_name = row['genres']
        session.execute_write(create_movie_genre_relationship, movie_id, genre_name)

# Close the driver
driver.close()

print("Relationships created successfully!")