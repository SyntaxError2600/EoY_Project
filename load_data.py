# This program will clear and load movie related data into the remote instance of Noe4j.
# Used the Data from: MovieLens' GroupLens Research that collected and made available rating datasets from their movie web site: https://grouplens.org/datasets/movielens/
# Warning: this load program may take up to a couple of hours (Aprox 8) to complete, so be very patience!!
# Author = Frank Schawillie

import os
import glob
import _clear_db as cdb
import _split_movies as sm
import _load_movies as lm
import _load_genres as lg
import _load_ratings as lr
import _create_links_movie_genre as clmg
import _create_links_movie_rating as clmr

file_root = 'data\\'
uri = "neo4j+s://0010002b.databases.neo4j.io"  
username = "neo4j"  
password = "hYe_cBlsLPUwCNJkQrmBoDeasDkAtd3zMEyAB1UsQYE" 
# AURA_INSTANCEID=0010002b
# AURA_INSTANCENAME=Instance01

def main():
    # Clean DB
    cdb.clear(uri=uri, username=username, password=password)
    # Split the movie file in Movies Only & Genres
    sm.split_movies(file_root)
    # Load Movies resources in DB
    lm.load(file_root=file_root, uri=uri, username=username, password=password)
    # Load Genres resources
    lg.load(file_root=file_root, uri=uri, username=username, password=password)
    # Load Ratings
    lr.load(file_root=file_root, uri=uri, username=username, password=password)
    # Create Genres to Movies links
    clmg.create_links(file_root=file_root, uri=uri, username=username, password=password) 
    # Create Ratings to Movies links
    clmr.create_links(file_root=file_root, uri=uri, username=username, password=password) 
    # Delete tmp_ files
    delete_tmp(file_root=file_root)
    
def delete_tmp(file_root):

    files_to_delete = glob.glob(os.path.join(file_root, 'tmp_*'))

    # Loop through the files and delete any 'tmp_' files
    for file_path in files_to_delete:
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

if __name__ == "__main__":
    main()