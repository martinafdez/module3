# testing git / iza

import sqlite3
import requests
import json
import pprint
from math import sin, cos, sqrt, atan2, radians

conn = sqlite3.connect('phonebook.db') 
c = conn.cursor()
 
#ask the user how they wish to search
def defineSearch():
    userChoice = (input("Type 1 if you would like to serach by biz name or 2 if you would like tp serach by biz type and location "))
    
    if userChoice ==  "1":
        getBizName()
    elif userChoice ==  "2":
        getPostcode()
    else:
        print("Try again. Please type either 1 or 2")
        defineSearch()
        
####--------SEARCH 1: BIZ NAME
####--------returns results only if the business exists in the database

def getBizName():
    userInputBizName = (input("Type name of the company: ")).title()
    print(userInputBizName)
    c.execute('SELECT * FROM business WHERE nameBusiness = ?', (userInputBizName,))
    
    resultsBizName = c.fetchall()
    if len(resultsBizName) == 0:
        print("Sorry, nothing! Try again.")
    else:
        print(resultsBizName)


####-------------------SEARCH 2: BIZ TYPE AND POSTOCODE

# def getPostcode() take postcode input from the user and gets geo coorindates from API. These are saved as varibales long1 and lat1 used later in def distance 
    
def getPostcode():
    endpoint="https://api.postcodes.io/postcodes/"
    postcodeStart = input("What's the postcode?")
    postcodeValidation(postcodeStart)
    
    postcodeStart = postcodeStart.replace(' ', '')
    postcodeStart_response = requests.get(endpoint + postcodeStart)
    data_postcodeStart = postcodeStart_response.json()
    if postcodeStart_response.status_code == 200:  
        long1 = data_postcodeStart['result']['longitude']
        lat1 = data_postcodeStart['result']['latitude']
#        print (long1, lat1)
        
    getResults(long1, lat1)
    return(long1, lat1)

def getResults(long1, lat1):
    endpoint="https://api.postcodes.io/postcodes/"
    options() #caling options() so see what types of businesses are available 
    finalResults = {} #this is a dictionary that will store our results sorted by distance. 
    
    userInputBizType = input("Type in type of business: ").title()
    c.execute('SELECT * FROM business WHERE typeBusiness = ?', (userInputBizType,) )
    resultsBizType =  c.fetchall() #getting results form the database that match userInputBizType


# looping through resultsBizType, taking postcode, finding out coordinates, storing latitude as long2 and lat2
#calling distance function to figure out diatnce from postcodeStart to the company
# {distance: row} make up a dictionary record in finalresults
    for row in resultsBizType: #looping through resultsBizType
        postcode = row[6]
        postcode = str(postcode).replace(' ', '')
        postcode_response = requests.get(endpoint + postcode)
        data_postcode = postcode_response.json()
        if postcode_response.status_code == 200:  
            long2 = data_postcode['result']['longitude']
            lat2 = data_postcode['result']['latitude']
            
            key = round(distance(lat1, long1, lat2, long2), 2)
            finalResults [key] = row
    sortByDistance(finalResults)


#sorts finalResults, which is a dictionary, by it's key which is distance from the poscodeStart
def sortByDistance(finalResults):
    finalResultsByDistance = sorted(finalResults.items(), key=lambda kv: kv[0])
    print()
    print("FINAL RESULTS BY DISTANCE")
    pprint.pprint (finalResultsByDistance)
    print()
    print("VOILA!!!")


#calculates distance between two points based on geo coordinates
def distance(lat1, long1, lat2, long2):
    R = 6373.0 # approximate radius of earth in km
    dlon, dlat = radians(long2) - radians(long1), radians(lat2) - radians(lat1)
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    a=abs(a)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    hdist = R * c
#    print("distance is:" + str(round(hdist,2)) + " miles")
    return hdist

# validates postcode input - if too short or too long, it will call getPostcode() again
    

    
def options():
    print("Here are business type options we support. Pick one:")
    options =[]
    c.execute('SELECT* FROM business')
    for row in c.fetchall():
        if row[2] not in options:
            options.append(row[2])
    print(options)
    return(options)



def postcodeValidation(postcodeStart):
    while len(postcodeStart) < 6 or len(postcodeStart) > 8:
            try:
                print("Please enter full postcode. Please enter postcode only.")
                getPostcode()
                
            except len(postcodeStart) == 3 or len(postcodeStart) ==2:
                print("Please enter both parts of the postcode")
                getPostcode()

defineSearch()

c.close()
conn.close()