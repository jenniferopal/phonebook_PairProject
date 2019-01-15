# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 09:44:54 2019

@author: milly
"""

###########################
#BUSINESS TABLE
###########################

import json
import sqlite3
conn = sqlite3.connect('phonebook_project.db')
c = conn.cursor()

def create_phonebook_business():
    c.execute('CREATE TABLE IF NOT EXISTS phonebook_business(business_name TEXT, address_line_1 TEXT, address_line_2 TEXT, address_line_3 TEXT, postcode REAL, country TEXT, telephone_number REAL, business_category TEXT)')

file = open('mock_data_business.json')
data = json.load(file)


def data_entry_business():
    for i in range(len(data)):
        business_info = data[i]
        business_name = business_info['business_name']
        address_line_1 = business_info['address_line_1']
        address_line_2 = business_info['address_line_2']
        address_line_3 = business_info['address_line_3']
        postcode = business_info['postcode']
        country = business_info['country']
        telephone_number = business_info['telephone_number']
        business_category = business_info['business_category']
        
        c.execute('INSERT INTO phonebook_business(business_name, address_line_1, address_line_2, address_line_3, postcode, country, telephone_number, business_category) VALUES (?, ?, ?, ? , ? , ? , ?, ?)', (business_name, address_line_1, address_line_2, address_line_3, postcode, country, telephone_number, business_category))
        conn.commit()
        

create_phonebook_business()
data_entry_business()
c.close()
conn.close()


