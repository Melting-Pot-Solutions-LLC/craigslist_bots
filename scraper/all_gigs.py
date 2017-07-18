import smtplib
import time

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from craigslist import CraigslistGigs

# locations = ['columbia', 'charleston', 'florencesc', 'greenville', 'hiltonhead', 'myrtlebeach']
locations = ['charleston', 'florencesc', 'greenville', 'hiltonhead', 'myrtlebeach']

queries = ['website', 'development', 'developer', 'software', 'wordpress']


#go through each location
for j in locations:
    #go through each keyword 
    for i in queries:
        cl_e = CraigslistGigs(site=j, filters={'query': i})
        final_string = ""
        for result in cl_e.get_results():
            #print  " '"  + result['name'] + "' -> " + result['url']
            final_string = final_string + ("\n '"  + result['name'] + "' -> " + result['url']).encode('utf-8') + "\n"

        # send an email
        fromaddr = "dml1002313@gmail.com"
        toaddr = "konstantinrubin@engineer.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = j + ": '" + i + "'" + " craigslist search results"
        body = final_string
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "SteveNash70!SteveNash70!")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

        #pause
        time.sleep(5)