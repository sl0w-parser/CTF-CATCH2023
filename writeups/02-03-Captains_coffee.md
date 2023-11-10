# Captain's coffee

## Zadání

Ahoy, deck cadet,
your task is to prepare good coffee for captain. As a cadet, you are prohibited from going to the captain's cabin, so you will have to solve the task remotely. Good news is that the coffee maker in captain's cabin is online and can be managed via API.

May you have fair winds and following seas!

Coffee maker API is available at http://coffee-maker.cns-jv.tcc.

Hint 1: Use VPN to get access to the coffee maker.

Hint 2: API description si available at http://coffee-maker.cns-jv.tcc/docs.

## Řešení

- na URL je jakési API
- v komentáři je odkaz na dokumentaci: http://coffee-maker.cns-jv.tcc/docs
	- zde je info o POST volání `/makeCoffee`, které jako vstup očekává ID
- volání prostého `/coffeeMenu` vrací seznam možných drinků a z něj odhaduji toto jako správné kafe
```
|3||
|drink_name|"Naval Espresso with rum"|
|drink_id|501176144|
```
- dotaz na ChatGPT, jak naformulovat JSON dotaz - vrátilo použitelný Python kód s mou úpravou:
```
import requests

url = "http://coffee-maker.cns-jv.tcc/makeCoffee/"
data = {"drink_id": 501176144}

response = requests.post(url, json=data)

if response.status_code == 200:
     #data = response.json()
     # Process the data here
     print(response.json())
else:
     print(f"Request failed with status code: {response.status_code}")


```
- odpověď serveru: `{'message': 'Your Naval Espresso with rum is ready for pickup', 'validation_code': 'Use this validation code FLAG{ccLH-dsaz-4kFA-P7GC}'}`
- FLAG: `FLAG{ccLH-dsaz-4kFA-P7GC}`