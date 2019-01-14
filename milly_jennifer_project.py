
import sqlite3
import json

conn = sqlite3.connect('phonebook_Test.db')

c = conn.cursor()

def create_business():
    c.execute('CREATE TABLE IF NOT EXISTS phonebook_business(business_name TEXT, address_line_1 TEXT, address_line_2 TEXT, address_line_3 TEXT, postcode REAL, country TEXT, telephone_number REAL, business_category TEXT)')
#---Taking data for Businesses

file = open('mock_data_business.json')
data = json.load(file)

def data_entry_Business():
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

        c.execute(
            ('INSERT INTO phonebook_business(business_name, address_line_1, address_line_2, address_line_3, postcode, country, telephone_number, business_category) VALUES (?, ?, ?, ? , ? , ? , ?, ?)',
            (business_name, address_line_1, address_line_2, address_line_3, postcode, country, telephone_number,
             business_category))
        conn.commit()

#    conn.commit()
#    c.close() #----Used to close the table
#    conn.close() #----Used to close the database
  
def create_people():
    c.execute('CREATE TABLE IF NOT EXISTS phonebook_people(first_name TEXT, last_name TEXT, address_line_1 TEXT, address_line_2 TEXT, address_line_3 TEXT, postcode REAL, country TEXT, telephone_number REAL)')

#----Taking data for People
def data_entry_People():
    for i in range(len(data)):
        people_info = data[i]
        business_name = people_info['business_name']
        address_line_1 = people_info['address_line_1']
        address_line_2 = people_info['address_line_2']
        address_line_3 = people_info['address_line_3']
        postcode = people_info['postcode']
        country = people_info['country']
        telephone_number = people_info['telephone_number']
        business_category = people_info['business_category']

        c.execute('INSERT INTO phonebook_people(first_name, last_name, address_line_1, address_line_2, address_line_3, postcode, country, telephone_number) VALUES (?, ?, ?, ? , ? , ? , ?)',
            (first_name, second_name, address_line_1, address_line_2, address_line_3, postcode, country, telephone_number))
        conn.commit()
    c.close() #----Used to close the table
    conn.close() #----Used to close the database

#------------------FILTER FUNCTION FOR PEOPLE DB----------------------------------
#def read_from_peopleData():
#    c.execute("SELECT * FROM peopleData WHERE value= 'Hairdresser' ")
#    for row in c.fetchall():#-----FETCHALL() function is
#        print(row)
#---------------------------------------------------------------------------------

create_phonebook_business()
data_entry_business()
c.close()
conn.close()



