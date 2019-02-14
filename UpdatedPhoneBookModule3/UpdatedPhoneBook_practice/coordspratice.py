# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 12:03:05 2019

@author: mluci
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:35:50 2019

@author: mluci
"""
import sqlite3
import requests



conn = sqlite3.connect('phonebook.db') 

c = conn.cursor()

endpoint="https://api.postcodes.io/postcodes/"

def create_table_coordinates():
    c.execute('CREATE TABLE IF NOT EXISTS Coordinates(postcode VARCHAR(10), latitude DECIMAL(10,8), longitude DECIMAL (11,8) )')
    
create_table_coordinates() 

def populate_table_coordinates():
     c.execute('SELECT postcode FROM people')
     for row in c.fetchall():
        postcode = str(row).replace(' ', '')
        postcode = postcode.strip("'(),'")
        c.execute('SELECT postcode FROM people')
#        coords = c.fetchall()
        for postcode in c.fetchall():
            
            if postcode not in c.execute('SELECT postcode FROM people'):
        
                postcode_response = requests.get(endpoint + postcode)
    
                data_postcode = postcode_response.json()
            
    
                       
                if data_postcode['status' ] == 200:
                    longitude = data_postcode['result']['longitude']
                    latitude = data_postcode['result']['latitude']
                    print(longitude)
                    print(latitude)
            
                    c.execute("INSERT INTO Coordinates(postcode, latitude, longitude) VALUES(?,?,?)", (postcode, latitude, longitude))
                    conn.commit()
         
         
populate_table_coordinates()

c.close()
conn.close()
            
            