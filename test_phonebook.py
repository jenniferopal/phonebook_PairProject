####################################
#TEST PHONEBOOK FOR UNIT TESTING
####################################

import unittest 
#import sqlite3
from functions import connect_db

#THE USER CAN CHOOSE TO SEARCH BY NAME OR CATEGORY
   
class Test_DB_Connection(unittest.TestCase):#This function doesn't take any input #Gives us access to different testing capabilities
    def test_connect_db(self):
        self.assertTrue(connect_db("db/phonebook_project.db"))





#---ALWAYS AT THE BOTTOM AND ONLY ONCE
if __name__ == "__main__":
   unittest.main()
   
