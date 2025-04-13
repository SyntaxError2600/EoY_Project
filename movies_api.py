from flask import Flask, request, jsonify
from neo4j import GraphDatabase

# Neo4j connection details from the file
NEO4J_URI = "neo4j+s://0010002b.databases.neo4j.io"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "hYe_cBlsLPUwCNJkQrmBoDeasDkAtd3zMEyAB1UsQYE"

# Initialize Flask app
app = Flask(__name__)

# Initialize Neo4j driver
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

def search_movie_by_name(tx, movie_name):
    # Cypher query to search for movies by name
    query = (
        "MATCH (m:Movies) "
        "WHERE m.title CONTAINS $movie_name "
        "RETURN m.title AS title, m.movieId AS movieId, m.rating AS rating"
    )
    result = tx.run(query, movie_name=movie_name)
    return [{"title": record["title"], "movieId": record["movieId"], "rating": record["rating"]} for record in result]

def recommend_similar_movies(tx, movie_id, rating):
    # Cypher query to recommend similar movies based on the same genre and similar rating
    query = (
        "MATCH (m:Movies)-[:BELONGS_TO]->(g:Genres)<-[:BELONGS_TO]-(recommended:Movies) "
        "WHERE m.movieId = $movie_id "
        "RETURN recommended.title AS title, recommended.movieId AS movieId "
        "LIMIT 10"
    )
    result = tx.run(query, movie_id=movie_id, rating=rating)
    return [{"title": record["title"], "movieId": record["movieId"]} for record in result]

@app.route('/search_movie', methods=['GET'])
def search_movie():
    movie_name = request.args.get('name', '')
    if not movie_name:
        return jsonify({"error": "Movie name is required"}), 400

    # Query Neo4j database
    with driver.session() as session:
        movies = session.read_transaction(search_movie_by_name, movie_name)
    
    if not movies:
        return jsonify({"message": "No movies found"}), 404
    
    return jsonify({"movies": movies})

@app.route('/recommend_movies', methods=['GET'])
def recommend_movies():
    movie_id = request.args.get('movieId', type=int)
    if not movie_id:
        return jsonify({"error": "MovieId is required"}), 400

    # Query Neo4j database to get the movie and its rating
    with driver.session() as session:
        movie = session.read_transaction(search_movie_by_name, movie_name='')
        movie = next((m for m in movie if m['movieId'] == movie_id), None)
        if not movie:
            return jsonify({"error": "Movie not found"}), 404
        
        # Get recommendations based on the movie's genre and rating
        recommendations = session.read_transaction(recommend_similar_movies, movie_id, movie['rating'])
    
    if not recommendations:
        return jsonify({"message": "No recommendations found"}), 404

    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)