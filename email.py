import os.path
import time
import platform
import subprocess
os_name = platform.system()
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
        command = 'ssmtp joe@foxjazz.net < mail.txt'
        try:
            # Run the command and capture the output
            output = subprocess.check_output(command, shell=True, text=True)
            
            # Print the output
            print("Command Output:")
            print(output)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the command: {e}")
            
sendMail(".005")            

