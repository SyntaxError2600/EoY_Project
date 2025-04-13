# EoY_Project

Author: Frank Schawillie

#### Use cases:
Recommendation Engine: Model users, products, views, purchases, and reviews as nodes and edges. Then use the graph to explore connections like what the user looked at or purchased, then recommend similar to items.  Compare this to a relationship-based SQL joins vs that of a GraphDB recommendations data structure (speed, query complexity, accurate). 

Movie Data
* MovieLens:: GroupLens Research has collected and made available rating datasets from their movie web site: https://grouplens.org/datasets/movielens/

Setup and Execution
load_data
movies_api
   Search Movie by Name: http://127.0.0.1:5000/search_movie?name=Toy%20Story
   Get recommendations by Movie ID: http://127.0.0.1:5000/recommend_movies?movieId=1
