#Venmo Money Requester Application by Dylan Gomes (This is my first python personal project)
#This application is made to help automate the monthly request of the phone bill from my family, we all share a plan
#so instead of having to request money one by one each month this application will make the task much more simple by allowing
#the process to be automated

# Venmo API Documentation link (https://github.com/mmohades/Venmo)

#import libraries
import configparser
import datetime as dt
import venmo_api as venmo
from venmo_api import *

#Grab Api key from config file
def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['venmo_api']['api']

API_PRIV_KEY = get_api_key()

#Initalize the venmo api
client = Client(get_api_key())

#Use this to grab user IDS
print(client.user.get_user_by_username("MattGomes9878"))

#initalizing variables
balance = float(0.00)
requestmny = 0
x = dt.datetime.now()
todayinp = input("Please enter the current date: ")
today = int(todayinp)
i = 1

#String variables
str_bankmsg = "Your Bank Transfer has iniciated for amount $ "

#if loop to get the amount of user to request money from and the amount to request from them
if today == 31:
    requsramtinp = input("Enter the amount of users you would like to send request to: ")
    requsramt = int(requsramtinp)
    while requsramt >= i:
        usrname = input("Please enter the user ID of the user you want to request money from: ")
        reqamt = input("Please enter the amount you would like to request from the user: $ ")
        reqnote = input("Please enter the note along with this transaction: ")
        testamt= float(reqamt)
        #This is when the api sends the request per the specifications provided by the user
        client.payment.request_money(amount=testamt, note=reqnote, target_user_id=usrname)
        str_Rqtmsg = "Your Request for $" + str(reqamt) + " was sent to " + str(usrname)
        print(str_Rqtmsg)
        balance += testamt
        print("Your Total Amount Requested is: "+ balance)
        i += 1       
else:
    print("It is currently the incorrect date to request the phone bill: ")
