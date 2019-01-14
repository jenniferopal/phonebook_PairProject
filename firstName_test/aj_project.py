 
import sqlite3
import json
from pprint import pprint


conn = sqlite3.connect('firstname_Test.db')

c = conn.cursor()
  
def create_people():
    c.execute('CREATE TABLE IF NOT EXISTS nameData(f_Name TEXT, l_Name TEXT')

    
mock_data_people = open('data_people.json').read()

data = json.loads(mock_data_people)
    
    
for row in data:
    f_Name = row["first_name"]
    
    print(f_Name)


with open('data_people.json') as a:
    data_file = json.load('last_name')

pprint(data)
    
#----Taking data for People
    
#def data_entry_People():
#    c.execute("INSERT INTO peopleData VALUES('Melisa', 'Ozyurt', '99 Zoo Lane', 'Taunton', 'Somerset', 'TA41AY', 0800567890, 234.90)")
#    conn.commit()
#    c.close() #----Used to close the table
#    conn.close() #----Used to close the database
#

#------------------FILTER FUNCTION FOR PEOPLE DB----------------------------------
#def read_from_peopleData():
#    c.execute("SELECT * FROM peopleData WHERE value= 'Hairdresser' ")
#    for row in c.fetchall():#-----FETCHALL() function is 
#        print(row)
#        
#        