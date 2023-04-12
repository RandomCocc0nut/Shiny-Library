# Shiny-Library
Shinies, or, respectively, a Shiny, is a currency for Scratch. 
Use this library to interact with Shiny's api.
 >Note: a shinies admin will have to generate you an app ID, and the app ID automatically determines what it is called and who the receiver is.
 
## GetUser(username)
Example of response:
>Note: This example of response is just for 2.0 api.
```
{"balance":0,
"history":[{"type":"paid","user":"__evelyn","amount":10,"date":0}, {"type":"received","user":"__evelyn","amount":10,"date":0}],
"pins":["__evelyn","__evelyn","__evelyn"],
"admin":true,
"exists":true}
```
or  ```{"exists":false}``` if the user does not exist or hasn't registered their account

## GetVersion()
Gets the latest version

## UserHistory(username)
Example of response:
>Note: This example of response is just for 2.0 api.
```
{"exists":true,
"html":"<br /><a href=\"/u/__evelyn\">__evelyn</a> paid you 10 shinies 57 years ago<br />You paid <a href=\"/u/__evelyn\">__evelyn</a> 10 shinies 57 years ago"}
```
or  ```{"exists":false}``` if the user does not exist or hasn't registered their account

## AppInfo(key)
Gets info about an application
```JSON Keys: exists (boolean), name (string), receiver (string)```

## Pay(customerName, customerkey, receiver, amount) & AppPay(customerName, key, app,receiver,amount)
 Transfers money from one account to another
 
##Request(customerName, customerKey, toRequestFrom, amount, appId)
>Note: This feature will work just for 1.0 api.
 Requets from an account the specified amount of money
