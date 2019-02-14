# testing git / iza

import sqlite3
import requests
import json
import pprint
from math import sin, cos, sqrt, atan2, radians


#conn = sqlite3.connect('phonebook.db') 
#c = conn.cursor()


#--------------Pick biz or ppl--------------------------------------------

def helloJoke():
    #ask the user if they wish to search for people or businesses
    print("WELCOME TO THE BOOK OF PHONE!")
    print("Thanks for stopping by. Bet you have not seen a phonebook done in Python in a while. Here we go! \n") 
    print("Fancy looking for poeple or for businesses? \n Type 1 for people \n Type 2 if you would like to serach by business name \n Type 3 if you would like to serach by business type and location.\n Type Q to quite our phonebook")
    answersUserChoice = ["1","2","3","Q","q"]
    userChoice = "x"
    
    while userChoice not in answersUserChoice: 
        userChoice= input("Type 1, 2, 3 or Q.")
        if userChoice == "1":
            peopleMaster()
            break
        elif userChoice == "2":
            print("Great choice. Looking up starngers online is a bit creepy!\n")
            getBizName()
            break
        elif userChoice == "3":
            print("Great choice. Looking up starngers online is a bit creepy!\n")
            bizMaster()
            break
        elif  userChoice ==  "Q" or userChoice == "q":
            print("You just made a developer cry. Goodbye.")
            return
        else:
            print("Try again. Please type either 1, 2 or Q")

    

def goAgain():
    goAgainOptions = ["Yes","No"]
    goAgainInput = "x"
    while goAgainInput not in goAgainOptions:
        goAgainInput = input("Want to play again? Type Yes or No.").title()
        if goAgainInput == "Yes":
            helloJoke()
            break
        elif goAgainInput == "No":
            print("You just made a developer cry. Goodbye.")
            break
        else:
            print("Try again. Please type either Yes or No.")

#-------------------CONTROL CENTRE PPL ---------------------------------------
        
def peopleMaster():
    optionsS = surnameOptions()
    userInputSurname = typeSurname(optionsS)
    typePostcodeOrCity(userInputSurname)

def surnameOptions():
    conn = sqlite3.connect('phonebook.db') 
    c = conn.cursor()
    optionsS = []
    c = conn.cursor()
    c.execute('SELECT* FROM people')
    for row in c.fetchall():
        if row[2] not in optionsS:
            optionsS.append(row[2])
    return(optionsS)
    c.close()
    conn.close()


def typeSurname(optionsS):
    conn = sqlite3.connect('phonebook.db') 
    c = conn.cursor()
    validSurname = surnameOptions()     
    userInputSurname = input("Type surname of the person you are looking for: ").title()

    while userInputSurname not in validSurname:
        print("Sorry, not in our phonebook! Try Hann ;) Next hint - Carlton")
        userInputSurname = input("Type surname of the person you are looking for: ").title()
    return userInputSurname
    c.close()
    conn.close()


def typePostcodeOrCity(userInputSurname):
    conn = sqlite3.connect('phonebook.db') 
    c = conn.cursor()
    userInputPostcodeOrCity = input("Type in city or postcode: ")

    if userInputPostcodeOrCity.isalpha():
    #CITY
        userInputPostcodeOrCity = userInputPostcodeOrCity.title()

    else:
        userInputPostcodeOrCity = userInputPostcodeOrCity.upper()
        while len(userInputPostcodeOrCity) < 6 or len(userInputPostcodeOrCityP)>8:
            try:
                print("Please enter full postcode or name of a city")
                userInputPostcodeOrCity = input("Type in the postcode: ").upper()
            except  len(userInputPostcodeOrCity) == 3 or len(userInputPostcodeOrCityP) == 2:
                print("Please enter both parts of the postcode")
                userInputPostcodeOrCity = input("Type in the postcode: ").upper()
    
    c.execute('SELECT * FROM people WHERE postcode = ? OR city = ? AND surname = ?', (userInputPostcodeOrCity, userInputPostcodeOrCity, userInputSurname) )
    resultsFinalPeople =  c.fetchall()
    if len(resultsFinalPeople) == 0:
       goAgain()
    else:
        print(resultsFinalPeople)
        goAgain()
    c.close()
    conn.close()
####--------SEARCH 1: BIZ NAME---------------------------------------------


def getBizName():
    #returns results only if the business exists in the database
    conn = sqlite3.connect('phonebook.db') 
    c = conn.cursor()
    userInputBizName = (input("Type name of the company: ")).title()
    print(userInputBizName)
    c.execute('SELECT * FROM business WHERE nameBusiness = ?', (userInputBizName,))
    
    resultsBizName = c.fetchall()
    if len(resultsBizName) == 0:
        print("Sorry, nothing! Try again.")
    else:
        print(resultsBizName)
    c.close()
    conn.close()
    goAgain()

#-------------------CONTROL CENTRE BIZ TYPE AND LOCATION  -----------------

def bizMaster():
    long1, lat1 = getPostcodeCoordinates()
    finalResults = getResults(long1, lat1)
    sortByDistance(finalResults)
    goAgain()
    return
    

####-------------------SEARCH 2: BIZ TYPE AND POSTOCODE

def getPostcodeCoordinates():
    # gets geo coorindates from API for poscodeStart and saves as long1 and lat1 used later in distance() 
    endpoint="https://api.postcodes.io/postcodes/"
    postcodeStart=input("What's the postcode?")
    postcodeStart = postcodeStart.replace(' ', '')
    postcodeStart_response = requests.get(endpoint + postcodeStart)
    data_postcodeStart = postcodeStart_response.json()
    
    while postcodeStart_response.status_code != 200: 
        print("Doesn't seem like we have this postcode. Are you sure you typed an existing one? Pleasy type postcode only. Please type in full postcode.")
        postcodeStart=input("What's the postcode?")
        postcodeStart = postcodeStart.replace(' ', '')
        postcodeStart_response = requests.get(endpoint + postcodeStart)
        data_postcodeStart = postcodeStart_response.json()
        
    if postcodeStart_response.status_code == 200:  
        long1 = data_postcodeStart['result']['longitude']
        lat1 = data_postcodeStart['result']['latitude']
        return(long1, lat1)
        
        
def getResults(long1, lat1):
    # prints all avilable biz types by calling caling bizTypeOptions()and asks user to pick one
    # creates empty dictionary that will store final results 
    # gets all results that match  userInputBizType from the databse
    # runs a for loop that for each row of data 
        # to get geocoordinates from API   
        # calcualte the distance from postcodeStart 
        # create a dictionary entry with distance being the key and the row being the value  {distance: row}
    # sorts the dictionary by keys and prints the results 
            
    conn = sqlite3.connect('phonebook.db') 
    c = conn.cursor()
    endpoint="https://api.postcodes.io/postcodes/"
    valid = bizTypeOptions() 
    finalResults = {}
    userInputBizType = input("Type in type of business: ").title()
    while userInputBizType not in valid:
            print("This clearly did not work. Have another look and type one of the options we support. ")
            userInputBizType = input("Type in type of business: ").title()
    
    c.execute('SELECT * FROM business WHERE typeBusiness = ?', (userInputBizType,) )
    resultsBizType =  c.fetchall() 

    for row in resultsBizType: 
        postcode = row[6]
        postcode = str(postcode).replace(' ', '')
        postcode_response = requests.get(endpoint + postcode)
        data_postcode = postcode_response.json()
        if postcode_response.status_code == 200:  
            long2 = data_postcode['result']['longitude']
            lat2 = data_postcode['result']['latitude']
            
            key = round(distance(lat1, long1, lat2, long2), 2)
            finalResults [(key, "miles away")] = row
    return finalResults
    c.close()
    conn.close()

def sortByDistance(finalResults):
    #sorts finalResults dictionary by key (distance from postcodestart)
    finalResultsByDistance = sorted(finalResults.items(), key=lambda kv: kv[0][0])
    print()
    print("FINAL RESULTS BY DISTANCE")
    pprint.pprint (finalResultsByDistance)
    print()
    print("VOILA!!!")
    return


def distance(lat1, long1, lat2, long2):
    #calculates distance between two points based on geo coordinates
    R = 6373.0 # approximate radius of earth in km
    dlon, dlat = radians(long2) - radians(long1), radians(lat2) - radians(lat1)
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    a=abs(a)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    hdist = R * c
    return hdist

def bizTypeOptions():
    # prints biz type options from phonebook/db/buziness
    conn = sqlite3.connect('phonebook.db') 
    c = conn.cursor()
    print("Here are business type options we support. Pick one:")
    options =[]
    c.execute('SELECT* FROM business')
    for row in c.fetchall():
        if row[2] not in options:
            options.append(row[2])
    print(options)
    c.close()
    conn.close()
    return(options)
    