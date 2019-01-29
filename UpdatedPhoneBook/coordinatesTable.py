# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:35:50 2019

@author: mluci
"""
import sqlite3
import requests
import json


conn = sqlite3.connect('phonebook.db') 

c = conn.cursor()

endpoint="https://api.postcodes.io/postcodes/"

def create_table_coordinates():
    c.execute('CREATE TABLE IF NOT EXISTS coordinates(postcode VARCHAR(10), latitude DECIMAL(10,8), longitude DECIMAL (11,8) ) ')
    
create_table_coordinates() 

def populate_table_coordinates_people():
     c.execute('SELECT postcode FROM people')
     for row in c.fetchall():
        currentpostcode = row[0]
        
        c.execute('SELECT * FROM coordinates WHERE postcode = ?', (currentpostcode,))
        results = c.fetchall()
        if len(results) == 0: 
            postcode = str(currentpostcode).replace(' ', '')
            postcode = postcode.strip("'(),'")    
            print("NOT DUPLICATE")
            postcode_response = requests.get(endpoint + postcode)
    
            data_postcode = postcode_response.json()
            if data_postcode['status'] == 200:
                longitude = data_postcode['result']['longitude']
                latitude = data_postcode['result']['latitude']
                print(longitude)
                print(latitude)
                
                c.execute("INSERT INTO coordinates(postcode, latitude, longitude) VALUES(?,?,?)", (currentpostcode, latitude, longitude))
        else:         
              print("DUPLICATE") 
        conn.commit()
     
populate_table_coordinates_people()

def read_from_db_all():
    input_postcode=input("Please enter a postcode: ")
    c.execute('SELECT * FROM coordinates WHERE postcode=?', (input_postcode, ))
    for row in c.fetchall():
        print(row)
read_from_db_all()
print('read from db all')



c.close()
conn.close()
            
            