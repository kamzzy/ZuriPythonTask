
#  Use functions
# Include register, and login
#  Generate Account Number
#  Any other improvement you can think of (extra point)
 
import datetime
currentDateTime = datetime.datetime.now()
name =input("What is your name? ")
allowedUsers = ['presh','beli', 'seyi', 'kelvin']
allowedPassword = ['pass','passy','para','ment']

if (name in allowedUsers):
    password = input('Your Password ')
    userId = allowedUsers.index(name)

    if (password == allowedPassword[userId]):

        print ('Welcome %s today is %s' % (name,currentDateTime.strftime("%c")))

        print('\n These are the available options')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('\n Please select an option: '))

        if(selectedOption == 1):
            int(input('\n How much would you like to withdraw: '))
            print('\n Please take your cash')
            
        elif(selectedOption == 2):
            deposit = int(input('\n How much would you like to deposit? '))
            print('\n Your current balance is %d' % deposit)
        elif(selectedOption == 3):
            input('\n What issue will you like to report? ')
            print('\n Thank you for contacting us')
        else:
            print('\n invalid option selected')
    else:
        print('Password is incorrect, please try again')
            
else:
    print('Name not found, please try again')