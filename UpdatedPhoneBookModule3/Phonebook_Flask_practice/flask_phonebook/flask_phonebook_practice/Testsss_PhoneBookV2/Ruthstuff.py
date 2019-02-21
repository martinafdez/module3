# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:13:42 2019

@author: mluci
"""
from sqlite3 import connect
from os.path import exists
from math import sin, cos, sqrt, atan2, radians

###Ruth code###

db_path = "Phonebook.db"

def check_db():
    if exists(db_path):
        return True
    else:
        return False
check_db()

def connect_db():
    try:
        connection = connect(db_path)
        cursor = connection.cursor()
        return (connection, cursor)
    except:
        return None
connect_db()

def query_db(query):
    try:
        connection, cursor = connect_db()
        results = cursor.execute(query).fetchall()
        connection.close()
        return results
    except:
        return None

    
    
def distance(lat1,long1,lat2,long2):

    R = 6373.0 # approximate radius of earth in km

    dlon, dlat = radians(long2) - radians(long1), radians(lat2) - radians(lat1)
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    a=abs(a)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    hdist = R * c
    return hdist

#distance(lat1,long1,lat2,long2)

def get_nearest_neighbors():
    # get all postcodes in database
    query = "SELECT postcode, latitude, longitude FROM coordinates"
    results = query_db(query)
    #print(results, "results")
    
    postcode=input("enter your postcode: ")
    # get longitude and latitude of given postcode
    test = [i for i in results if i[0].lower().strip() == postcode.lower().strip()]
   #print(test, "tests")
    
    if len(test) > 0:

        # select latitude and longitudes of matched postcode
        coords1 = (test[0][1],test[0][2])
        #print(coords1, "coords1")

        distances = [distance(test[0][1],test[0][2],i[1], i[2]) for i in results]
        results = [results[i]+(distances[i],) for i in range(len(distances))]
        results.sort(key=lambda x: x[-1])
        print(distances, "distances")
        #print(results)
        return results
    else:
        print("No Postcode Match fOUND")
        
get_nearest_neighbors()        
