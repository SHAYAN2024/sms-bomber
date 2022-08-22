import requests
import time

number = input("Enter Your Phone number (without 0) : ")
url_divar = "https://api.divar.ir/v5/auth/authenticate"
json_divar = {"phone":number}

 req = requests.post(url=url_divar,json=json_divar)
 print(req)
