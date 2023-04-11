""""
A library to interact with Shiny's api.
""""

import requests

def GetVersion():
 res = requests.get('https://shinies.space/version')
 return res.text

def UserInfo(username):
 res = requests.get('https://shinies.space/api/users/'+username)
 return res.text

def UserHistory(username):
 res = requests.get('https://shinies.space/api/history/'+username)
 return res.text

def AppInfo(key):
 res = requests.get('https://shinies.space/api/app/'+key)
 return res.text

def Pay(key, reciever, amount):
 res = requests.post('https://shinies.space/api/pay', data={'key': key,'reciever': reciever, 'amount': amount}) 
 return res.text

def AppPay(key, app, amount):
 res = requests.post('https://shinies.space/api/pay', data={'key': key,'app': app, 'amount': amount}) 
 return res.text





