# Shiny-Library
Shinies, or, respectively, a Shiny, is a currency for Scratch. 
Use this library to interact with Shiny's api.
 >Note: a shinies admin will have to generate you an app ID, and the app ID automatically determines what it is called and who the receiver is.
 
## GetUser(username)
Example of response:
>Note: This example of response is just for 2.0 api.
```json
{"balance":0,
"history":[{"type":"paid","user":"__evelyn","amount":10,"date":0}, {"type":"received","user":"__evelyn","amount":10,"date":0}],
"pins":["__evelyn","__evelyn","__evelyn"],
"admin":true,
"exists":true}
```
or 
```json
{"exists":false}
``` 
if the user does not exist or hasn't registered their account

## GetVersion()
Gets the latest version

## UserHistory(username)
Example of response:
>Note: This example of response is just for 2.0 api.
```json
{"exists":true,
"html":"<br /><a href=\"/u/__evelyn\">__evelyn</a> paid you 10 shinies 57 years ago<br />You paid <a href=\"/u/__evelyn\">__evelyn</a> 10 shinies 57 years ago"}
```
or 
```json
{"exists":false}
``` 
if the user does not exist or hasn't registered their account

## AppInfo(key)
Gets info about an application
```JSON Keys: exists (boolean), name (string), receiver (string)```

## Pay(customerName, customerkey, receiver, amount) & AppPay(customerName, key, app,receiver,amount)
> AppPay it's just a v2.0 feature

 Transfers money from one account to another
| Argument | Description | v1.0 | 2.0
| --- | --- | --- | --- | 
| `customerName` | The user who get transfered the money from |:white_check_mark:|:x:
| `customerKey` | The user's key who get transfered the money from |:white_check_mark:|:white_check_mark:
| `receiver` | The user who receive the money |:white_check_mark:|:white_check_mark:
| `amount` | The amount of money who gets the reciever |:white_check_mark:|:white_check_mark:
| `appId` | The id of the application that will transfer the money |:white_check_mark:|:x:
 
## Request(customerName, customerKey, toRequestFrom, amount, appId)
>Note: This feature will work just for 1.0 api.

Requests from an account the specified amount of money
