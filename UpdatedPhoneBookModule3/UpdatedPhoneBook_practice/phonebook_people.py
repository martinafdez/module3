#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 11:35:13 2019

@author: Fabiana
"""

import sqlite3 
import json
import random

conn = sqlite3.connect('phonebook.db') 

c = conn.cursor()

def create_table_people():
    c.execute('CREATE TABLE IF NOT EXISTS people(personId REAL, name TEXT, surname TEXT, addressLine1 VARCHAR(255), city TEXT, country TEXT, postcode VARCHAR(10), phoneNumber REAL)')
    
create_table_people()  

def populate_table_people():
    with open('data_people.json') as p:
        dataPeople = json.load(p)
        for row in dataPeople:
            personId = random.randint(0,100000)
            name = row["first_name"]
            surname = row["last_name"]
            addressLine1 = row["address_line_1"]
            city = row["address_line_2"]
            country = row["address_line_3"]
            postcode = row["postcode"]
            phoneNumber = row["telephone_number"]
            c.execute("INSERT INTO people(personId, name, surname, addressLine1, city, country, postcode, phoneNumber) VALUES(?,?,?,?,?,?,?,?)", (personId, name, surname, addressLine1, city, country, postcode, phoneNumber))
    conn.commit()  

populate_table_people()  
        

c.close()
conn.close()

