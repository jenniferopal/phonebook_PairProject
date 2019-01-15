# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 09:44:54 2019

@author: milly
"""
import json
import sqlite3
conn = sqlite3.connect('phonebook_project.db')
c = conn.cursor()

###########################
#PEOPLE TABLE
###########################
        
def create_phonebook_people():
    c.execute('CREATE TABLE IF NOT EXISTS phonebook_people(first_name TEXT, last_name TEXT, address_line_1 TEXT, address_line_2 TEXT, address_line_3 TEXT, postcode REAL, country TEXT, telephone_number REAL)')

file = open('mock_data_people.json')
data = json.load(file)


def data_entry_people():
    for i in range(len(data)):
        people_info = data[i]
        first_name = people_info['first_name']
        last_name = people_info['last_name']
        address_line_1 = people_info['address_line_1']
        address_line_2 = people_info['address_line_2']
        address_line_3 = people_info['address_line_3']
        postcode = people_info['postcode']
        country = people_info['country']
        telephone_number = people_info['telephone_number']
        
        c.execute('INSERT INTO phonebook_people(first_name, last_name, address_line_1, address_line_2, address_line_3, postcode, country, telephone_number) VALUES (?, ?, ?, ? , ? , ? , ?, ?)', (first_name, last_name, address_line_1, address_line_2, address_line_3, postcode, country, telephone_number))
        conn.commit()
        
        
create_phonebook_people()
data_entry_people()
c.close()
conn.close()
    
