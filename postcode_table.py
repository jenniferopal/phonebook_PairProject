###########################
#POSTCODE TABLE
###########################

import sqlite3
import requests
conn = sqlite3.connect('phonebook_project.db')
c = conn.cursor()

def create_postcode_table():
    c.execute('CREATE TABLE IF NOT EXISTS postcode_table(postcode TEXT, longitude REAL, latitude REAL)')


def insert_business_into_postcode():
        
    c.execute('SELECT postcode FROM phonebook_business')
    for row in c.fetchall():
        current =row[0]#--This turns the postcodes into individual items rather than one whole list
        c.execute('SELECT * FROM postcode_table WHERE postcode =?', (current, ))
        results = c.fetchall()
        
        if len(results) == 0:
            
            postcode_no_spaces = current.replace(" ","")
            endpoint = 'https://api.postcodes.io/postcodes/'
            response = requests.get(endpoint + postcode_no_spaces)
            data = response.json()
            
            if response.status_code == 200:
                print('ok')
                latitude = data['result']['latitude']
                longitude = data['result']['longitude']   
                #    print(latitude)
                #    print(longitude)
                c.execute('INSERT INTO postcode_table(postcode, longitude, latitude) VALUES (?,?, ?)', (current, longitude,latitude))
                conn.commit()
            else:
                 print('no')   



create_postcode_table()
insert_business_into_postcode()
c.close()
conn.close()
