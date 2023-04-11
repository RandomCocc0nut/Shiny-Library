# Shiny-Library
Shinies, or, respectively, a Shiny, is a currency for Scratch. 
Use this library to interact with Shiny's api.


### UserInfo() Fuction
```python
UserInfo(username)
```
Response Example:
```json
{"exists":true,
"balance":0,
"isAdmin":false}
```

### Pay() and Request() Fuction
```python
Pay(customerName, customerKey, reciever, amount, appId)
Request(customerName, customerKey, toRequestFrom, amount, appId)
```
Status Codes:
```
200 - Request succeeded
400 - Bad Request
404 - Resource Not Found
500 - Internal Server Error
503 - Indicates that the service could be down for maintenance, has crashed, or is temporarily unable to handle the user request.
```

### ValidateKey() Fuction
```python
ValidateKey(username, key)
```
Response Example:
```
Key: Correct
```
