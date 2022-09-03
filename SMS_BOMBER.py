from pyexpat import model
import requests
import time

number = input("Inter your phone number (without 0) : ")
url_namva = "https://api-react.okala.com/C/CustomerAccount/OTPRegister"
json_namva = {"mobile":"0" + number,"deviceTypeCode":5,"confirmTerms":"true","notRobot":"false"}
req = requests.post(url= url_namva,json= json_namva)
print(req)
