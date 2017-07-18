import smtplib
import time

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from craigslist import CraigslistJobs

# locations = ['columbia', 'charleston', 'florencesc', 'greenville', 'hiltonhead', 'myrtlebeach']
locations = ['charleston', 'florencesc', 'greenville', 'hiltonhead', 'myrtlebeach']

queries = ['web', 'mobile', 'app', 'website', 'development', 'developer', 'software', 'wordpress', 'full stack', 'front end']
categories = ['sof', 'web'] # if the category is sof, then we should search for each query, if it's web, then no queiry is needed

#go through each location
for j in locations:
    time.sleep(5)

    # !-!-!-!-!-!-!-!-!-!-
    # search the 'sof' section
    for i in queries:
        cl_e = CraigslistJobs(site=j, category='sof', filters={'query': i})
        final_string = ""
        for result in cl_e.get_results():
            final_string = final_string + ("\n '"  + result['name'] + "' -> " + result['url']).encode('utf-8') + "\n"

        # send an email
        fromaddr = "dml1002313@gmail.com"
        toaddr = "konstantinrubin@engineer.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "CRAIGSTLIST " + j + " JOBS 'SOF': '" + i + "'" + " craigslist search results"
        body = final_string
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "SteveNash70!SteveNash70!")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()



    # !-!-!-!-!-!-!-!-!-!-
    # search the 'web' section
    final_string = ""
    cl_e = CraigslistJobs(site=j, category='web')
    for result in cl_e.get_results():
        final_string = final_string + ("\n '"  + result['name'] + "' -> " + result['url']).encode('utf-8') + "\n"

    # send an email
    fromaddr = "dml1002313@gmail.com"
    toaddr = "konstantinrubin@engineer.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "CRAIGSTLIST " + j + " JOBS 'WEB': '" + "'" + " craigslist search results"
    body = final_string
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "SteveNash70!SteveNash70!")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

