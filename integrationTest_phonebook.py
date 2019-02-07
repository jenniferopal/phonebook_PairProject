####################################
#TEST PHONEBOOK FOR INTEGRATION TESTING
####################################
from functions import *
import os
import requests



class test_Project():
    #CHECKS THAT THE USER INPUT MATCHES SOMETHING THAT IS IN THE DB
    def test_inputBusinessCat(self):
        self.businessCat = ask_searchBusinessCat()
        if self.businessCat:
            return True
        else:
            return False
        
    def test_BusinessCatSearch(self):
        if self.businessCat:
            businessCatSearch = searchBusinessCat()
            if businessCatSearch:
                return True
            else:
                print("Couldn't pull the Business Categories")
                return False
        else:
            return "There is no category by that name in the DB"
        
    def tests_returns(self):
        print(self.test_inputBusinessCat())
        print(self.test_BusinessCatSearch())
        
"""

#SEARCH BY BUSINESS CATEGORY
def ask_searchBusinessCat():
    inputBusinessCat = ""
    inputBusinessLocation = ""
    while inputBusinessCat == "" and inputBusinessLocation == "":  
        try:
            inputBusinessCat = input("Enter a business Category: ")
            inputBusinessLocation = input("Enter a location: ")
        except ValueError:
            print("Please enter a string!")
    searchBusinessCat(inputBusinessCat, inputBusinessLocation)
            
def searchBusinessCat(inputBusinessCat, inputBusinessLocation):
    cur = conn.cursor()
    cur.execute("SELECT business_name,business_category,address_line_1,address_line_2,postcode FROM phonebook_business WHERE business_category =? and address_line_2 =? order by business_name", (inputBusinessCat, inputBusinessLocation ))

"""
    


#---ALWAYS AT THE BOTTOM AND ONLY ONCE
if __name__ == "__main__":
   startTest = test_Project()
   startTest.tests_returns()
   
   
   
   
   
   
   
   
   