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
        


#---ALWAYS AT THE BOTTOM AND ONLY ONCE
if __name__ == "__main__":
   startTest = test_Project()
   startTest.tests_returns()
   
   
   
   
   
   
   
   
   