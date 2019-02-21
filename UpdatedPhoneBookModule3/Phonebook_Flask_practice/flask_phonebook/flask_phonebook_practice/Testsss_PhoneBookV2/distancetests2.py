# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 11:40:06 2019

@author: mluci
"""

from sqlite3 import connect
from math import sin, cos, sqrt, atan2, radians
import sqlite3

conn = sqlite3.connect('phonebook.db') 
c = conn.cursor()

def typePostcodeOrCity():
    userInputPostcodeOrCity = input("Type in city or postcode: ")
    if userInputPostcodeOrCity.isalpha():
    #CITY
        userInputPostcodeOrCity = userInputPostcodeOrCity.title()
        print("it's a city!")
        print(userInputPostcodeOrCity)
        c.execute('SELECT * FROM business WHERE city = ?', (userInputPostcodeOrCity,) )
        resultsC = c.fetchall()
    
        if len(resultsC) == 0:
            print("Sorry, nothing in this city. Try again.")
            typePostcodeOrCity()
        else:
            typeBizType(userInputPostcodeOrCity)

    else: 
        #POSTCODE
        userInputPostcodeOrCity = userInputPostcodeOrCity.upper()
        while len(userInputPostcodeOrCity) < 6 or len(userInputPostcodeOrCity)>8:
            try:
                print("Please enter full postcode or name of a city")
                userInputPostcodeOrCity = input("Type in the postcode: ").upper()
    
            except  len(userInputPostcodeOrCity) == 3 or len(userInputPostcodeOrCity) == 2:
                print("Please enter both parts of the postcode")
                userInputPostcodeOrCity = input("Type in the postcode: ").upper()
    
        
        c.execute('SELECT * FROM business WHERE postcode = ?', (userInputPostcodeOrCity,) )
    
        resultsPC = c.fetchall()
    
        if len(resultsPC ) == 0:
            print("Sorry, nothing for this postcode! Try again.")
            typePostcodeOrCity()
        else:
            typeBizType(userInputPostcodeOrCity)

# ask for user input BIZTYPE, check if in 
def typeBizType(userInputPostcodeOrCity):
    userInputBizType = input("Type in biz type: ").title()

    c.execute('SELECT * FROM business WHERE postcode = ? AND typeBusiness  = ?', (userInputPostcodeOrCity, userInputBizType) )
    resultsFinalPc =  c.fetchall()
    if len(resultsFinalPc) != 0:
            print(resultsFinalPc)
    else:
        c.execute('SELECT * FROM business WHERE city = ? AND typeBusiness  = ?', (userInputPostcodeOrCity, userInputBizType) )
        resultsFinalC =  c.fetchall()
        
        if len(resultsFinalC) != 0:
            print(resultsFinalC)
        else:
            print("Sorry, nothing for " + userInputBizType + " in " + userInputPostcodeOrCity + ". Try again!")
            typePostcodeOrCity()

#typePostcodeOrCity()


def distance():
    userInputPostcodeOrCity=typePostcodeOrCity()
    postcode = userInputPostcodeOrCity
    
    resultsFinalC=typeBizType(userInputPostcodeOrCity)

    postcoderesults= typeBizType(userInputPostcodeOrCity)
    
    ###Get lang and longs for resulting postcodes##
    results_lat = ("SELECT latitude FROM postcodes where postcode = ?", (postcoderesults,))
    
    results_long = ("SELECT longitude FROM postcodes where postcode = ?", (postcoderesults,))
    
    input_long = ("SELECT longitude FROM postcodes where postcode = ?", (postcode,))
    
    input_lat = ("SELECT latitude FROM postcodes where postcode = ?", (postcode,))


  
    R = 6373.0 # approximate radius of earth in km

    dlon, dlat = radians(results_long) - radians(input_long), radians(results_lat) - radians(input_lat)
    a = sin(dlat / 2) ** 2 + cos(results_lat) * cos(input_lat) * sin(dlon / 2) ** 2
    a=abs(a)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    hdist = R * c
    return hdist
distance()

def get_nearest_neighbors():
    #get users postcode input#
    postcode = typePostcodeOrCity()
    #get results of business and location search#
    postcoderesults= typeBizType(userInputPostcodeOrCity)
    
    #get longitude and latitude of users postcode#
    test = [i for i in postcoderesults if i[0].lower().strip() == postcode.lower().strip()]
    print(test, "tests")
    
    
    if len(test) > 0:

        # select latitude and longitudes of matched postcode
        coords1 = (test[0][1],test[0][2])
        print(coords1, "coords1")

        distances = [distance(test[0][1],test[0][2],i[1], i[2]) for i in postcoderesults]
        postcoderesults = [postcoderesults[i]+(distances[i],) for i in range(len(distances))]
        postcoderesults.sort(key=lambda x: x[-1])
        print(distances, "distances")
        #print(results)
        return postcoderesults
    else:
        print("No Postcode Match fOUND")

get_nearest_neighbors()











#    ###Take all the resulting postcodes & calculate distances in loop so does it to all.###
#    for postcode in results:
#        distance(results_lat,results_long ,input_long,input_lat)
#        return postcode
#   
#    
#    ###Order them by closest to furthest####
#    
#    
#    
#    
#    
#    
#    
#    ##All the results returned need to be ordered by closest to the postcode provided##
#    
#     # get longitude and latitude of given postcode
#    test = [i for i in results if i[0].lower().strip() == userInputPostcode.lower().strip()]
#    
#            # select latitude and longitudes of matched postcode
#    coords1 = (test[0][1],test[0][2])
#
#    distances = [distance(test[0][1],test[0][2],i[1], i[2]) for i in results]
#    results = [results[i]+(distances[i],) for i in range(len(distances))]
#    results.sort(key=lambda x: x[-1])




















import sqlite3
from math import sin, cos, sqrt, atan2, radians


##Function that takes results given back and orders by distance to postcode provided by user##

conn = sqlite3.connect('phonebook.db') 
c = conn.cursor()


postcode= 'CT16 1AB'            
postcoderesult = 'CT16 1AJ'
#businesstype= 'Industrial'
#postcoderesults=c.execute('SELECT * FROM business WHERE postcode = ? AND typeBusiness  = ?', (postcode, businesstype))          
            

def distance():
    conn = sqlite3.connect('phonebook.db') 
    c = conn.cursor()
    
    postcode= 'CT16 1AB'            
    postcoderesult = 'CT16 1AJ'


##Get lang and longs for resulting postcodes##
    c.execute("SELECT latitude FROM coordinates WHERE postcode = ?", (postcoderesult,))
    results_lat1=c.fetchall()
    results_lat2=str(results_lat1)
    results_lat= results_lat2.strip("[](),")
    print(results_lat)
    
    c.execute("SELECT longitude FROM coordinates WHERE postcode = ?", (postcoderesult,))
    results_long1=c.fetchall()
    results_long2=str(results_long1)
    results_long= results_long2.strip("[](),")
    print(results_long)
    
    c.execute("SELECT longitude FROM coordinates WHERE postcode = ?", (postcode,))
    input_long1=c.fetchall()
    input_long2=str(input_long1)
    input_long= input_long2.strip("[](),")
    print(input_long)
    
    
    c.execute("SELECT latitude FROM coordinates WHERE postcode = ?", (postcode,))
    input_lat1=c.fetchall()
    input_lat2=str(input_lat1)
    input_lat= input_lat2.strip("[](),")
    print(input_lat)

    print(results_long)
    radians(results_long)
    print(radians)
    print(results_long)

  
    R = 6373.0 # approximate radius of earth in km

    dlon, dlat = radians(results_long) - radians(input_long), radians(results_lat) - radians(input_lat)
    a = sin(dlat / 2) ** 2 + cos(results_lat) * cos(input_lat) * sin(dlon / 2) ** 2
    print(a)
    a=abs(a)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    print(c)

    hdist = R * c
    print(hdist)
    return hdist

distance()



    
    
    
#def get_nearest_neighbors():
#    userInputPostcode=get_postcode()
#    postcode=userInputPostcode
#    
#    resultsFinalPc = get_business()
#    postcoderesults=resultsFinalPc
#    
#    test = [i for i in postcoderesults if i[0].lower().strip() == postcode.lower().strip()]
#    print(test, "tests")
#    
#    
#    if len(test) > 0:
#
#        # select latitude and longitudes of matched postcode
#        coords1 = (test[0][1],test[0][2])
#        print(coords1, "coords1")
#
#        distances = [distance(test[0][1],test[0][2],i[1], i[2]) for i in postcoderesults]
#        postcoderesults = [postcoderesults[i]+(distances[i],) for i in range(len(distances))]
#        postcoderesults.sort(key=lambda x: x[-1])
#        print(distances, "distances")
#        #print(results)
#        return postcoderesults
#    else:
#        print("No Postcode Match fOUND")
#
#get_nearest_neighbors()
#    
#    
#
#    
