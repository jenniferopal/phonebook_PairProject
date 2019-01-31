import unittest 
import sqlite3
import sys

from search_functions import *

#THE USER CAN CHOOSE TO SEARCH BY NAME OR CATEGORY
   
class test_db(unittest.TestCase):
    def db_test(self):
        self.assertTrue(searchBy())
        self.assertIsInstance(searchBy(), str)#Sys expects arguments after the implementation

#    def sys_input(self):
#        self.assertIsInstance(sys.argv[1], int)


#class TestBusinessSearch(unittest.TestCase):
#   def TestNameSearch(self):
#       self.assertEqual(row[0], inputBusiness)
#
#
#   def TestCategorySearch(self):
#       self.assertEqual(row[1], inputBusiness)



















#---ALWAYS AT THE BOTTOM AND ONLY ONCE
if __name__ == "__main__":
   unittest.main()
   
   