# EoY_Project

Author: Frank Schawillie

#### Use cases:
Recommendation Engine: Model users, products, views, purchases, and reviews as nodes and edges. Then use the graph to explore connections like what the user looked at or purchased, then recommend similar to items.  Compare this to a relationship-based SQL joins vs that of a GraphDB recommendations data structure (speed, query complexity, accurate). 

Movie Data Source
* MovieLens:: GroupLens Research has collected and made available rating datasets from their movie web site: https://grouplens.org/datasets/movielens/

load_data.py: based on the supplied connection details, will load movies, genres, ratings and create the required relationships need to supply the movies_api. 
movies_api.py: simple HTTP API that allow the user to serach for a movie by name or retrieve recommendations based on a movie's id. 
* Search Movie by Name: http://127.0.0.1:5000/search_movie?name=Toy%20Story
* Get recommendations by Movie ID: http://127.0.0.1:5000/recommend_movies?movieId=1
