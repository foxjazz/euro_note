import os
def sendMail(some):
    sendmail_location = "/usr/sbin/sendmail" # sendmail location
    p = os.popen("%s -t" % sendmail_location, "w")
    p.write("From: %s\n" % "send@foxjazz.net")
    p.write("To: %s\n" % "mail@foxjazz.net")
    p.write("Subject: eur: " + some)
    p.write("\n") # blank line separating headers from body
    p.write("body of the mail")
    status = p.close()
    
    if status != 0:
           print ("Sendmail exit status", status)
           
sendMail("2.2")           
           
           
