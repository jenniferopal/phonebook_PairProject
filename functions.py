###########################
#FUNCTION FILE- CHAPTER 4
###########################
import sqlite3
from os.path import exists

db_path = 'db/phonebook_project.db'
conn = sqlite3.connect('db/phonebook_project.db')
c = conn.cursor()

#CHECK THE DATABASE EXISTS
def check_db():
    if exists(db_path):
        return True
    else:
        return False


#CONNECT THE DATABASE       
def connect_db():
    try:
        conn = sqlite3.connect('db/phonebook_project.db')
        c = conn.cursor()
        return (conn, c)
    except:
        return None


def searchBy():
    print(" Would you like to: \n\n Search by Business (1) \n Search by Person (2) ")  
    user_input = 0
    while True:
        try:
            while user_input < 1 or user_input > 2:
                user_input = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Please enter a number!")
    
    if user_input == 1:
        searchByBusiness()        
    elif user_input == 2:
        ask_searchPerson()


###############################
#BUSINESS PHONEBOOK SEARCH
###############################


#THE USER CAN CHOOSE TO SEARCH BY NAME OR CATEGORY
def searchByBusiness():
    print(" Would you like to: \n\n Search by Business Name (1) \n Search by Business Category (2) ")  
    user_input = 0
    while True:
        try:
            while user_input < 1 or user_input > 2:
                user_input = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Please enter a number!")
    
    if user_input == 1:
        ask_searchBusinessName()        
    elif user_input == 2:
        ask_searchBusinessCat()


#FIND A BUSINESS BY NAME
def ask_searchBusinessName():
    inputBusinessName = ""
    inputBusinessLocation = ""
    while inputBusinessName == "" and inputBusinessLocation == "":  
        try:
            inputBusinessName = input("Enter a business Name: ")
            inputBusinessLocation = input("Enter a location: ")
            
        except ValueError:
            print("Please enter a string!")
    searchBusinessName(inputBusinessName, inputBusinessLocation)
            
def searchBusinessName(inputBusinessName, inputBusinessLocation):
    cur = conn.cursor()
    cur.execute("SELECT business_name,business_category,address_line_1,address_line_2,postcode FROM phonebook_business WHERE business_name =? and address_line_2 =?", (inputBusinessName, inputBusinessLocation))
    rows = cur.fetchall()
    
    if len(rows) == 0:
        print("Sorry there are no businesses matching the name {}".format(inputBusinessName))
        ask_searchBusinessName()
    else:
        for row in rows:         
            print("")
            print("Business Name: ", row[0], "\nAddress: ", row[2],row[3], "\nPostcode: ", row[4])
        
     
    print("Would you like to search again? ")
    print("Type yes or no:")
    another_option()

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

#NEED TO DO
#--- ORDER BY LONGITUDE AND LATITUDE BASED ON THE USER INPUT (ANOTHER C.EXECUTE TO RETRIEVE DATA FROM POSTCODE TABLE)
    
    rows = cur.fetchall()
    
    if len(rows) == 0:
        print("Sorry the category:{}".format(inputBusinessCat), " is not recognised")
        ask_searchBusinessCat()
    else:
        for row in rows:         
            print("Business Name: ", row[0], "\nBusiness Category: ", row[1], "\nAddress: ", row[2],row[3], "\nPostcode: ", row[4])
            print("\n")

    
    print("Would you like to search again? ")
    print("Type yes or no:")
    another_option()


###############################
#PEOPLE PHONEBOOK SEARCH
###############################
            
#FIND A BUSINESS BY NAME
def ask_searchPerson():
    inputSurname = ""
    while inputSurname == "":  
        try:
            inputSurname = input("Enter a Surname: ")
            
        except ValueError:
            print("Please enter a string!")
    searchSurname(inputSurname)
            
def searchSurname(inputSurname):
    cur = conn.cursor()
    cur.execute("SELECT first_name,last_name,address_line_1,address_line_2,postcode,telephone_number FROM phonebook_people WHERE last_name =?", (inputSurname, ))
    rows = cur.fetchall()
    
    if len(rows) == 0:
        print("Sorry there are no results matchin: {}".format(inputSurname))
        ask_searchPerson()
    else:
        for row in rows:         
            print("")
            print("First name: ", row[0], "\nLast name: ", row[1], "\nAddress: ", row[2],row[3], "\nPostcode: ", row[4], "\nTelephone Num: ", row[5])
            print("")
        
    print("")
    print("Would you like to search again? ")
    print("Type yes or no:")
#    another_option()     


#ANOTHER OPTION
def another_option():
    more = ""
    while more != "yes" or more != "no":
        try:
            more = input("Please enter your choice: ")
            if more == "yes":
                searchBy()
            elif more == "no":
                print("Okay, bye.")
                break
            else:
                print("Please try again.")
#                another_option()
            
        except ValueError():
            print("Please enter yes or no")      
            
searchBy()