# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 14:04:54 2018

@author: 612383263
"""
#--------Module 2: Lesson 8---------
#----"Data Bundle Exercise"----


###Functions###
#####NOTHING TO CHANGE#####
def DataBundlePurchase(truePasscode, balance):
    if passwordCheck(truePasscode) == True:
        transtype=TransactionType()
        if transtype == 1:
                return ('Your balance is {}'.format(balance))
             
        elif transtype == 2:
            return TelNumber(balance) 
    else: 
        return 'Wrong Password'
#####NOTHING TO CHANGE#####

def comparison(truePasscode):
    attempt = passwordCheck(truePasscode)
    if attempt == truePasscode:
        return True
    else:
        return False



def passwordCheck(truePasscode):

    counter= 3
    while counter > 0:
        attempt = input('Please enter your password: ') 
        if attempt == truePasscode:
            return True
        elif len(str(attempt)) > 4:
            print("Password too long. Try again")
                
        elif len(str(attempt)) < 4:
            print("Password too short. Try again")
        try:
            int(attempt)          
        except ValueError:
            print('Your password should be numbers only.')
            
        counter -= 1
        s = ''
        if (counter > 1):
            s = 's'
        
        print('You have {} attempt{} remaining'.format(counter, s))
        
        #comparison(truePasscode)
    print('You ran out of attempts')       
    
    
    
    
    
    
      
#####NOTHING TO CHANGE#####   
def checkBalance(balance):
    if balance > 0:
        return True
    else:
        return False
#####NOTHING TO CHANGE#####
    
    
    
    
    
#def TransactionType():
#    transtype = 0
#    counter = 3
#    while counter > 0:
#        try:
#            transtype = int(input('Please select what you would like to do: \n 1: Request credit balance \n 2: Purchase Data Bundle: '))
#            
#            if transtype < 1 or transtype > 2:
#                print("Please select either 1 or 2")
#            else:
#                return transtype
#        except ValueError:
#            print("Please enter 1 or 2.")             
#        counter -= 1
#        s = ''
#        if (counter > 1):
#            s = 's'
#        print('You have {} attempt{} remaining'.format(counter, s))
#
#    print("You ran out of attempts. Please try again later.")
              
    
#def TelNumb1():
#    counter = 3
#    while counter > 0:
#        try:
#            Numb1 = int(input('Please enter your phone number: '))
#        except ValueError:
#            print("Numbers should be digits only.")
#        counter -= 1
#    
#        s = ''
#        if (counter > 1):
#            s = 's'          
#        print('You have {} attempt{} remaining'.format(counter, s))
#    print('You ran out of attempts')
#    #return Numb1
# 
#    
#def TelNumber(balance):
#    maxtopup = 100
#    Numb1=TelNumb1()
#    counter = 3
#    while counter > 0:
#        try:
#            Numb2 = int(input('Please confirm your phone number: '))
#            if Numb1 == Numb2:
#                amountbuy = int(input('How much data would you like to buy? Please select up to 100GB. '))
#                if amountbuy > maxtopup:
#                    return('Sorry maximum is 100.')
#                elif amountbuy > balance:
#                    return('Sorry, you do not have enough in your account for this purchase.')
#                else:
#                    return multipleFive(amountbuy)          
#            else:
#                return('Sorry, your numbers do not match. Try again')
#        except ValueError:
#            print("Enter a number please")
#            
        






#####NOTHING TO CHANGE#####
def multipleFive(amountbuy):
    if amountbuy %5==0:
        return('Success. Your account has been updated.')
    else:
        return('This amount is unavailable. Try again please.')
#####NOTHING TO CHANGE#####
