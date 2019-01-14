import sqlite3
from milly_jennifer_project import *


conn = sqlite3.connect('phonebook.db')

c = conn.cursor()

#---Add dynamic entry later on
#--------------CALLS THE DEFINED FUNCTIONS ABOVE
    
create_business()
data_entry_Business()
create_people()
data_entry_People()