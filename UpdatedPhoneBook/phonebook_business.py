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

def create_table_business():
    c.execute('CREATE TABLE IF NOT EXISTS business(businessId REAL, nameBusiness TEXT, typeBusiness TEXT, addressLine1 VARCHAR(255), city TEXT, country TEXT, postcode VARCHAR(10), phoneNumber REAL)')
    
create_table_business()  

def populate_table_business():
    with open('data_business.json') as f:
        dataBusiness = json.load(f)
        for row in dataBusiness:
            businessId = random.randint(0,100000)
            nameBusiness = row["business name"]
            typeBusiness = row["business_category"]
            addressLine1 = row["address_line_1"]
            city = row["address_line_2"]
            country = row["address_line_3"]
            postcode = row["postcode"]
            phoneNumber = row["telephone_number"]
            c.execute("INSERT INTO business(businessId, nameBusiness, typeBusiness, addressLine1, city, country, postcode, phoneNumber) VALUES(?,?,?,?,?,?,?,?)", (businessId, nameBusiness, typeBusiness, addressLine1, city, country, postcode, phoneNumber))
    conn.commit()  

populate_table_business()  

    

c.close()
conn.close()

