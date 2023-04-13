""""
A library to interact with Shiny's api.
""""

import requests
v = GetVersion() # Gets the latest version

def GetVersion():
    res = requests.get('https://shinies.space/version')
    return res.text

def UserInfo(username):
    if v == '1':
        res = requests.get('https://shinies.space/user-info/'+username)
    elif v == '2':
        res = requests.get('https://shinies.space/api/users/'+username)
    return res.text

def UserHistory(username):
    res = requests.get('https://shinies.space/api/history/'+username)
    return res.text

def AppInfo(key):
    res = requests.get('https://shinies.space/api/app/'+key)
    return res.text

def Pay(customerName, customerkey, receiver, amount):
    if v == '2':
        res = requests.post('https://shinies.space/api/pay', data={'key': customerkey,'receiver': receiver, 'amount': amount}) 
    elif v == '1':
        res = requests.post(f'https://shinies.space/pay-with-key?user={customerName}&key={customerkey}&receiver={receiver}&amount={amount}&appid={app}')
    return res.text

def AppPay(customerName, key, app,receiver,amount):
    if v == '2':
        res = requests.post('https://shinies.space/api/pay', data={'key': key,'app': app, 'amount': amount}) 
    elif v == '1':
        return "App-pay is a v2 feature"

def Request(customerName, customerKey, toRequestFrom, amount, appId):
    if v == '1':
        res = requests.post(f'https://shinies.space/request-with-key?user={customerName}&key={customerKey}&torequest={toRequestFrom}&amount={amount}appid={appId}')
        return res.text
    elif v == '2':
        return "Requests are not anymore a feature in v2"
