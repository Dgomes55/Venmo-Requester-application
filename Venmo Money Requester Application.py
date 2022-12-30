#Venmo Money Requester Application by Dylan Gomes

# Venmo API Documentation link (https://github.com/mmohades/Venmo)

#import libraries
import datetime as dt
import venmo_api
from venmo_api import Client

#ask for user input of username and password
venmo_usrname = input("Please input your user name: ")
venmo_psword = input("Please input your password: ")

#Authentication for venmo client (to access your venmo account)
access_token = Client.get_access_token(username= venmo_usrname, password= venmo_psword)
#Print access token so you know what to impup later
print("My token:", access_token)
#initalizing variables

balance = float(0.00)
requestmny = 0
x = dt.datetime.now()
todayinp = input("Please enter the current date: ")
today = int(todayinp)
i = 1


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