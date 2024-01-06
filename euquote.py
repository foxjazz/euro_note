#!/usr/bin/env python3
import http.client
import json
import os.path
import time
import platform
import subprocess

# Get the operating system name and version
os_name = platform.system()

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
    
def sendMail(some):
    if os_name == "Darwin":
        with open("pw.txt", 'r') as file:
            pw = file.readline()
        msg = MIMEText("EUR went up")
        msg['Subject'] = "EUR went up " + some
        msg['From'] = "joe@foxjazz.net"
        msg['To'] = "mail@foxjazz.net"
        server = smtplib.SMTP('smtp.ionos.com', 587)  # Replace with your email server's details
        server.starttls()
        server.login("send@foxjazz.net", pw)  # Replace with your email credentials
        server.sendmail(msg['From'], msg['To'], msg.as_string())
    else:
        file_path = 'mail.txt'  # Replace with the path to your file

# Open the file in write mode ('w')
        with open(file_path, 'w') as file:
            # Write multiple lines of text
            file.write("From: send@foxjazz.net\n")
            file.write(f"Subject: EUR is {some} up.\n")
            file.write(f"Euro is up by {some}\n")
        command = '"ssmtp joe@foxjazz.net < mail.txt"'
        subprocess.check_output(command, shell=True, text=True)
        command = '"ssmtp ruthdickinson@live.com < mail.txt"'
        subprocess.check_output(command, shell=True, text=True)
            
            # Print the output
        


quote = .7
fe = True
file_path = 'last_quote.json'
if not os.path.exists(file_path):
    fe = False    
else:
    with open(file_path, 'r') as file:
        data = json.load(file)
        quote = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

while True:
    # Code to be executed every 5 minutes
    data = getEURUSD()
    
    with open("last_quote.json", "w") as file:
        json.dump(data,file)
    newquote = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    if (not fe):
        quote = newquote
    print("quote: ", quote)
    if (float(newquote) - .005 > float(quote)):
        sendMail(newquote)
        print("newquote" + newquote)
    #exchange_rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
    
    #print ("ER: ", exchange_rate)
    # Delay for 5 minutes (300 seconds)
    time.sleep(300)
