
#import libraries
import datetime as dt


#initalizing variables
balance = float(0.00)
requestmny = 0
x = dt.datetime.now()
todayinp = input("Please enter the current date: ")
today = int(todayinp)
i = 1
#x.strftime("%d")
#Gather user input

#String variables
str_bankmsg = "Your Bank Transfer has iniciated for amount $ "



#if loop to get the amount of user to request money from and the amount to request from them
if today == 31:
    requsramtinp = input("Enter the amount of users you would like to send request to: ")
    requsramt = int(requsramtinp)
    while requsramt >= i:
        usrname = input("Please enter the user name of the user you want to request money from: ")
        reqamt = input("Please enter the amount you would like to request from the user: $ ")
        testamt= float(reqamt)
        str_Rqtmsg = "Your Request for $" + str(reqamt) + " was sent to " + str(usrname)
        print(str_Rqtmsg)
        balance += testamt
        i += 1       
else:
    print("It is currently the incorrect date to request the phone bill: ")