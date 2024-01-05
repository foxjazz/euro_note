import http.client
import json
def getEURUSD():
    conn = http.client.HTTPSConnection("alpha-vantage.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "80d2e87f11msh0f7dee9d529814cp1d1301jsndf3b182ae5bc",
        'X-RapidAPI-Host': "alpha-vantage.p.rapidapi.com"
    }

    conn.request("GET", "/query?to_currency=EUR&function=CURRENCY_EXCHANGE_RATE&from_currency=USD", headers=headers)

    res = conn.getresponse()
    data = res.read()
    dc = data.decode("utf-8")
   
    return json.loads(dc)
    
    

import time
quote = 1.1
file_path = 'last_quote.json'
with open(file_path, 'r') as file:
    data = json.load(file)
    quote = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

while True:
    # Code to be executed every 5 minutes
    data = getEURUSD()
   
    with open("last_quote.json", "w") as file:
        json.dump(data,file)
    newquote = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    print("quote: ", quote)
    if (float(newquote) - .05 > float(quote)):
        print("newquote" + newquote)
    #exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    
    #print ("ER: ", exchange_rate)
    # Delay for 5 minutes (300 seconds)
    time.sleep(300)
