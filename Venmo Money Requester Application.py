#Venmo Money Requester Application by Dylan Gomes (This is my first python personal project)
#This application is made to help automate the monthly request of the phone bill from my family, we all share a plan
#so instead of having to request money one by one each month this application will make the task much more simple by allowing
#the process to be automated

# Venmo API Documentation link (https://github.com/mmohades/Venmo)

#import libraries
import configparser
import datetime as dt
import venmo_api
from venmo_api import Client

#Grab Api key from config file
def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['venmo_api']['api']

API_PRIV_KEY = get_api_key()

#Initalize the venmo api
client_test = Client(API_PRIV_KEY = API_PRIV_KEY)

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
        #This is when the api sends the request per the specifications provided by the user
        Client.payment.request_money(reqamt, "Test", "0000000000000000000")
        str_Rqtmsg = "Your Request for $" + str(reqamt) + " was sent to " + str(usrname)
        print(str_Rqtmsg)
        balance += testamt
        i += 1       
else:
    print("It is currently the incorrect date to request the phone bill: ")