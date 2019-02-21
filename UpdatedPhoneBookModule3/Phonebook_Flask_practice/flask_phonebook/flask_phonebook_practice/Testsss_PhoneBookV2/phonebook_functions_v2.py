# testing git / iza

import sqlite3
import requests

conn = sqlite3.connect('phonebook.db') 
c = conn.cursor()
 

def defineSearch():
    defineSearch = (input("Type 1 if you would like to serach by biz name or 2 if you would like tp serach by biz type and location "))
    if defineSearch ==  "1":
        typeBizName()
    elif defineSearch ==  "2":
        typeBizType()
    else:
        print("Try again")

####--------SEARCH 1: BIZ NAME
####--------returns results only if the business exists in the database

def typeBizName():
    userInputBizName = (input("Type name of the company: ")).title()
    print(userInputBizName)
    c.execute('SELECT * FROM business WHERE nameBusiness = ?', (userInputBizName,))
    
    resultsBizName = c.fetchall()
    if len(resultsBizName) == 0:
        print("Sorry, nothing! Try again.")
    else:
        print(resultsBizName)
    
#typeBizName()


####-------------------SEARCH 2: BIZ TYPE AND POSTOCODE


# ask for user input BIZTYPE
def typeBizType():
    options()
    
    userInputBizType = input("Type in type of business: ").title()

    c.execute('SELECT * FROM business WHERE typeBusiness = ?', (userInputBizType,) )
    resultsBizType =  c.fetchall()
    if len(resultsBizType) != 0:
           for i in resultsBizType:
               print (i)
               print()

    else:
        print("Sorry, nothing. Try again!")

def options():
    print("Here are business type options we support. Pick one:")
    options =[]
    c.execute('SELECT* FROM business')
    for row in c.fetchall():
        if row[2] not in options:
            options.append(row[2])
    print(options)

defineSearch()

#typeBizType()

#def typePostcode():
#    userInputPostcode = (input("Type in postcode: ")).upper()
#
#
#    while len(userInputPostcodeOrCity) < 6 or len(userInputPostcodeOrCity)>8:
#        try:
#            print("Please enter full postcode or name of a city")
#            userInputPostcode = input("Type in the postcode: ").upper()
#    
#        except  len(userInputPostcodeOrCity) == 3 or len(userInputPostcodeOrCity) == 2:
#            print("Please enter both parts of the postcode")
#            userInputPostcode = input("Type in the postcode: ").upper()
#    
#        
#        c.execute('SELECT * FROM business WHERE postcode = ?', (userInputPostcodeOrCity,) )
#    
#        resultsPC = c.fetchall()
#    
#        if len(resultsPC ) == 0:
#            print("Sorry, nothing for this postcode! Try again.")
#            typePostcodeOrCity()
#        else:
#            typeBizTypeOrName(userInputPostcodeOrCity)
#
#

#


c.close()
conn.close()

