""""
A library to interact with Shiny's api.
""""

import requests

def Pay(customerName, customerKey, reciever, amount, appId):
 res = requests.post('https://shinies.space/pay-with-key?user='+customerName+'&key='+customerKey+'&receiver='+reciever+'&amount='+amount+'appid='+appId)
 return res.text

def Request(customerName, customerKey, toRequestFrom,   amount,appId):
 res = requests.post('https://shinies.space/request-with-key?user='+customerName+'&key='+customerKey+'&torequest='+toRequestFrom+'&amount='+amount+'appid='+appId)
 return res.text

def CheckUser(username):
 res = requests.get('https://shinies.space/user-info/'+username)
 return res.text

def ValidateKey(username, key):
 res = requests.get('https://shinies.space/validate-key?user='+username+'&key='+key)
 return res.text
