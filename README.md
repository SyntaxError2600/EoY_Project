# EoY_Project

Author: Frank Schawillie

* Core Concepts
* Benefits
* Issues
* Compare and contrast GraphDB vs. RDBMS
### Leading GraphDB on the Market & Strengths
| **Database**      | **Type**                           | **License**                   | **Query Language**                | **Scalability**                        | **Cloud Support**                     | **Use Cases**                                               |
|-------------------|------------------------------------|-------------------------------|-----------------------------------|----------------------------------------|---------------------------------------|-------------------------------------------------------------|
| **Neo4j**         | Property Graph                     | Open Source / Enterprise      | Cypher                            | Good (with clusters)                   | Yes (Self-hosted & Cloud)             | Social networks, recommendations, fraud detection           |
| **Amazon Neptune**| Property Graph / RDF               | Commercial                    | Gremlin / SPARQL                  | Good (fully managed service)           | Yes (Fully managed AWS service)       | Social networks, knowledge graphs, fraud detection          |
| **ArangoDB**      | Multi-model (Graph, Document)      | Open Source                   | AQL (Arango Query Language)       | Good (with sharding)                   | Yes (Self-hosted & Cloud)             | Social networks, real-time analytics, IoT                   |
| **OrientDB**      | Multi-model (Graph, Document)      | Open Source / Enterprise      | SQL / Gremlin                     | Good (with sharding)                   | Yes (Self-hosted & Cloud)             | Graph-based applications, real-time analytics               |
| **TigerGraph**    | Native Graph                       | Commercial                    | GSQL                              | Excellent (highly scalable)            | Yes (Fully managed service)           | Deep link analytics, real-time analytics, AI-powered apps   |

    * Use of GraphDBs in the AI/LLMs

#### Use cases:
Recommendation Engine: Model users, products, views, purchases, and reviews as nodes and edges. Then use the graph to explore connections like what the user looked at or purchased, then recommend similar to items.  Compare this to a relationship-based SQL joins vs that of a GraphDB recommendations data structure (speed, query complexity, accurate). 

Code: https://github.com/SyntaxError2600/EoY_Project

Movie Data
* MovieLens:: GroupLens Research has collected and made available rating datasets from their movie web site: https://grouplens.org/datasets/movielens/

Setup and Execution
load_data
movies_api
    example: http://127.0.0.1:5000/search_movie?name=Powder, http://127.0.0.1:5000/recommend_movies?movieId=24