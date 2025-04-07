# Remember to pip install pandas, neo4j
# Used the Data from: MovieLens' GroupLens Research that collected and made available rating datasets from their movie web site: https://grouplens.org/datasets/movielens/
# You'll need to run data_prep.py and create_relationships.py before running this.  
# This program is rerunnable and won't overwrite existing relationships. 

import pandas as pd
from neo4j import GraphDatabase

# Load the ratings file to inspect its contents
rating_file_path = 'C:\\Users\\Frank\\Desktop\\EoY_Project\\data\\ratings.csv'
ratings_df = pd.read_csv(rating_file_path)

# Display the first few rows of the dataframe to understand its structure
ratings_df.head()

print("Creates relationship between a movie to its rating.")

# Connect to the Neo4j database
uri = "neo4j+s://50189fd8.databases.neo4j.io"  # Neo4j instance URI
username = "neo4j"  # The username
password = "UtF4qlyIsbTYS4m36DDBX-pKmPA3KJdo1kfVehfXsdU"  # The password
# AURA_INSTANCEID=50189fd8
# AURA_INSTANCENAME=Instance01

# Initialize the Neo4j driver
driver = GraphDatabase.driver(uri, auth=(username, password))

print("Starting to createing relationships.")

def create_movie_rating_relationship(tx, movie_id, rating_value):
    # Create the Movie and Rating nodes if they don't exist and create the relationship
    query = (
        "MERGE (m:Movie {movieId: $movie_id}) "
        "MERGE (r:Ratings {Rating: $rating_value}) "
        "MERGE (m)-[:HAS_RATING]->(r)"
    )
    tx.run(query, movie_id=movie_id, rating_value=rating_value)

# Get the first rating for each movieId (this will take the first rating based on the timestamp)
first_ratings_df = ratings_df.sort_values(by="timestamp").groupby("movieId").first().reset_index()

# Iterate over the first ratings and create relationships in Neo4j
with driver.session() as session:
    for _, row in first_ratings_df.iterrows():
        movie_id = row['movieId']
        rating_value = row['rating']
        session.execute_write(create_movie_rating_relationship, movie_id, rating_value)

# Close the driver
driver.close()

print("Relationships created successfully!")