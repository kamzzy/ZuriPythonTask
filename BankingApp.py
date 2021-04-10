# import mysql.connector
# import ast
import datetime
currentDateTime = datetime.datetime.now()
import random
database = {}  
def init():
 
    print ('\n Welcome to ziri bank today is %s \n' % currentDateTime.strftime("%c"))

    haveAccount = int(input('Do you have an account with us: 1(yes) 2(no) \n '))

    if(haveAccount == 1):
            
        login()
    elif(haveAccount == 2):
            
        register()
    else:
        print('You have selected an invalid option')
        init()
    
def login():
    print('******* Login *******')

    accountNumberFromUser = int(input('What is your account number? \n'))
    password = input('What is your password \n')

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
    else:
        print('you have selected an invalid option \n')   
        init()
    

def register():
    print('****** Register ******* \n')
    email = input('What is your email address? \n')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    password = input('Create a secure password \n')

    accountNumber = generatingAccountNumber()

    database[accountNumber] =  [first_name,last_name,email,password]
    
    # saveDatabase = open('database.txt', 'a')
    # saveDatabase.write(str(database))
    # saveDatabase.close()

    print('Your account has been created')
    print('== ==== ====== ===== ==')
    print('Your account number is: %d \n' % accountNumber)
    print('Make sure you keep it safe')
    print('== ==== ====== ===== ==')
    
    login()

def bankOperation(user):
    print('welcome %s %s \n' % (user[0], user[1]))
    
    print('These are the available options \n')
    print('1. Cash Deposit \n')
    print('2. Withdrawal \n')
    print('3. Complaints \n')
    print('4. Change password \n')
    print('5. logout \n')
        
    selectedOption = int(input('Please select an option \n'))

    if(selectedOption == 1):
    
        depositOperation()
    elif(selectedOption == 2):
    
        withdrawalOperation()
    elif(selectedOption == 3):

        complaints()
    elif(selectedOption == 4):

        changePasswordOperation()

    elif(selectedOption == 5):
    
        logout()
    elif(selectedOption <=0 or selectedOption >4):
        print('invalid option selected') 
        login()
    
def withdrawalOperation():

    withdrawalAmount = int(input('How much do you like to withdraw \n'))
    print('withdrawal request is successful \n')
    print('Please take your cash \n')
    print('Your current balance is %d \n' % withdrawalAmount)
    closingRemark()

def depositOperation():
    depositAmount = int(input('How much would you like to deposit \n'))
    print('Your deposit request is successful \n') 
    print('Your current balance is %d \n' % depositAmount)
    closingRemark()

def complaints():
    input('What issue would you like to report? \n')
    print('Thank you for contacting us \n')
    closingRemark()

def closingRemark():
    print('\n == ==== ====== ==== ==')
    print('Thank you for banking with us')
    print('  == ==== ====== ==== == \n')
    init()

def changePasswordOperation():
    input('What is your old password \n')
    input('what is your new password \n')
    print('password change is successful \n')
    closingRemark()

def logout():
    closingRemark()

def generatingAccountNumber():
    return random.randrange(1111111111,9999999999)


init()