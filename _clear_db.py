from neo4j import GraphDatabase

def clear(uri, username, password):

    # Initialize the Neo4j driver
    driver = GraphDatabase.driver(uri, auth=(username, password))

    def clear_database(tx):
        # This Cypher query deletes all nodes and relationships in the database
        query = "MATCH (n) DETACH DELETE n"
        tx.run(query)

    # Execute the function in a session
    with driver.session() as session:
        session.write_transaction(clear_database)

    # Close the driver
    driver.close()

    print("Database cleared successfully!")