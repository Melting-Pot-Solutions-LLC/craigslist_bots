import smtplib
import time
from datetime import date, timedelta

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from craigslist import CraigslistGigs

# locations = ['columbia', 'charleston', 'florencesc', 'greenville', 'hiltonhead', 'myrtlebeach']
# locations = ['charleston', 'florencesc', 'greenville', 'hiltonhead', 'myrtlebeach']

queries = ['website', 'development', 'developer', 'software', 'wordpress', 'freelance']



yesterday_string = (date.today() - timedelta(1)).strftime('20%y-%m-%d')

locations_us =  {
                    'SC': ['columbia', 'charleston', 'florencesc', 'greenville', 'hiltonhead', 'myrtlebeach'],
                    'NC': ['asheville', 'boone', 'charlotte', 'eastnc', 'fayetteville', 'greensboro', 'hickory', 'onslow', 'outerbanks', 'raleigh', 'wilmington', 'winstonsalem'],
                    'GA': ['albanyga', 'athensga', 'atlanta', 'augusta', 'brunswick', 'columbusga', 'macon', 'nwga', 'savannah', 'statesboro', 'valdosta'],
                    'AL': ['auburn', 'bham', 'dothan', 'shoals', 'gadsden', 'huntsville', 'mobile', 'montgomery', 'tuscaloosa'],
                    'TN': ['chattanooga', 'clarksville', 'cookeville', 'jacksontn', 'knoxville', 'memphis', 'nashville', 'tricities'],
                    'FL': ['miami', 'daytona', 'keys', 'fortmyers', 'gainesville', 'cfl', 'jacksonville', 'lakeland', 'lakecity', 'ocala', 'okaloosa', 'orlando', 'panamacity', 'pensacola', 'sarasota', 'spacecoast', 'staugustine', 'tallahassee', 'tampa', 'treasure'],
                    'MS': ['gulfport', 'hattiesburg', 'jackson', 'meridian', 'northmiss', 'natchez'],
                    'LA': ['batonrouge', 'cenla', 'houma', 'lafayette', 'lakecharles', 'monroe', 'neworleans', 'shreveport'],
                    'AR': ['fayar', 'fortsmith', 'jonesboro', 'littlerock', 'texarkana'],
                    'TX': ['abilene', 'amarillo', 'austin', 'beaumont', 'brownsville', 'collegestation', 'corpuschristi', 'dallas', 'nacogdoches', 'delrio', 'elpaso', 'galveston', 'houston', 'killeen', 'laredo', 'lubbock', 'mcallen', 'odessa', 'sanangelo', 'sanantonio', 'sanmarcos', 'bigbend', 'texoma', 'easttexas', 'victoriatx', 'waco', 'wichitafalls'],
                    'NM': ['albuquerque', 'clovis', 'farmington', 'lascruces', 'roswell', 'santafe'],
                    'AR': ['flagstaff', 'mohave', 'phoenix', 'prescott', 'showlow', 'sierravista', 'tucson', 'yuma'],
                    'CA': ['bakersfield', 'chico', 'fresno', 'goldcountry', 'hanford', 'humboldt', 'imperial', 'inlandempire', 'losangeles', 'mendocino', 'merced', 'modesto', 'monterey', 'orangecounty', 'palmsprings', 'redding', 'sacramento', 'sandiego', 'sfbay', 'slo', 'santabarbara', 'santamaria', 'siskiyou', 'stockton', 'susanville', 'ventura', 'visalia', 'yubasutter'],
                    'NV': ['elko', 'lasvegas', 'reno'],
                    'UT': ['logan', 'ogden', 'provo', 'saltlakecity', 'stgeorge'],
                    'CO': ['boulder', 'cosprings', 'denver', 'eastco', 'fortcollins', 'rockies', 'pueblo', 'westslope'],
                    # 'KS': ['lawrence', 'ksu', 'nwks', 'salina', 'seks', 'swks', 'topeka', 'wichita'],
                    # 'KY': ['bgky', 'eastky', 'lexington', 'louisville', 'owensboro', 'westky'],
                    # 'WV': ['charlestonwv', 'martinsburg', 'huntington', 'morgantown', 'wheeling', 'parkersburg', 'swv', 'wv'],
                    # 'VA': ['charlottesville', 'danville', 'fredericksburg', 'norfolk', 'harrisonburg', 'lynchburg', 'blacksburg', 'richmond', 'roanoke', 'swva', 'winchester'],
                    # 'MD': ['annapolis', 'baltimore', 'easternshore', 'baltimore', 'frederick', 'smd', 'westmd'],
                    # 'IL': ['bn', 'chambana', 'chicago', 'decatur', 'lasalle', 'mattoon', 'peoria', 'rockford', 'carbondale', 'springfieldil', 'quincy'],
                    # 'MT': ['billings', 'bozeman', 'butte', 'greatfalls', 'helena', 'kalispell', 'missoula', 'montana'],
                    # 'RI': ['providence'],
                    # 'AK': ['anchorage', 'fairbanks', 'kenai', 'juneau'],
                    # 'IN': ['juneau', 'evansville', 'fortwayne', 'indianapolis', 'kokomo', 'tippecanoe', 'muncie', 'richmondin', 'southbend', 'terrehaute'],
                    # 'NE': ['grandisland', 'lincoln', 'northplatte', 'omaha', 'scottsbluff'],
                    # 'SD': ['nesd', 'csd', 'rapidcity', 'siouxfalls', 'sd'],
                    # 'IA': ['ames', 'cedarrapids', 'desmoines', 'dubuque', 'fortdodge', 'iowacity', 'masoncity', 'quadcities', 'siouxcity', 'ottumwa', 'waterloo'],
                    # 'NH': ['nh'],
                    # 'NJ': ['cnj', 'jerseyshore', 'newjersey', 'southjersey'],
                    # 'NY': ['albany', 'binghamton', 'buffalo', 'catskills', 'chautauqua', 'elmira', 'fingerlakes', 'glensfalls', 'hudsonvalley', 'ithaca', 'longisland', 'newyork', 'oneonta', 'plattsburgh', 'potsdam', 'rochester', 'syracuse', 'potsdam', 'twintiers', 'utica', 'watertown'],
                    # 'CT': ['newlondon', 'hartford', 'newhaven', 'nwct'],
                    # 'MA': ['boston', 'capecod', 'southcoast', 'westernmass', 'worcester'],
                    # 'ND': ['bismarck', 'fargo', 'grandforks', 'nd'],
                    # 'MI': ['annarbor', 'battlecreek', 'centralmich', 'detroit', 'flint', 'grandrapids', 'holland', 'jxn', 'lansing', 'kalamazoo', 'monroemi', 'muskegon', 'nmi', 'porthuron', 'saginaw', 'swmi', 'thumb', 'up'],
                    # 'ME': ['maine'],
                    # 'VT': ['vermont'],
                    # 'OH': ['akroncanton', 'ashtabula', 'athensohio', 'chillicothe', 'cincinnati', 'cleveland', 'columbus', 'dayton', 'limaohio', 'mansfield', 'sandusky', 'toledo', 'tuscarawas', 'youngstown', 'zanesville'],
                    # 'WA': ['bellingham', 'kpr', 'moseslake', 'olympic', 'pullman', 'seattle', 'skagit', 'skagit', 'wenatchee', 'yakima'],
                    # 'MN': ['bemidji', 'brainerd', 'duluth', 'mankato', 'minneapolis', 'rmn', 'marshall', 'stcloud'],
                    # 'OK': ['lawton', 'enid', 'oklahomacity', 'stillwater', 'tulsa'],
                    # 'WI': ['appleton', 'eauclaire', 'greenbay', 'janesville', 'racine', 'lacrosse', 'madison', 'milwaukee', 'northernwi', 'sheboygan', 'wausau'],
                    # 'OR': ['bend', 'corvallis', 'eastoregon', 'eugene', 'klamath', 'medford', 'oregoncoast', 'portland', 'roseburg', 'salem'],
                    # 'PA': ['altoona', 'chambersburg', 'erie', 'harrisburg', 'lancaster' ,'allentown', 'meadville', 'philadelphia', 'pittsburgh', 'poconos' ,'reading' ,'scranton', 'pennstate', 'pennstate', 'york'],
                    # 'MO': ['columbiamo', 'joplin', 'kansascity', 'kirksville', 'loz', 'semo', 'springfield', 'stjoseph', 'stlouis'],
                    # 'WY': ['wyoming'],
                    # 'ID': ['boise', 'eastidaho', 'lewiston', 'twinfalls', 'honolulu'],
                    # 'OTHER': ['micronesia', 'puertorico', 'virgin']
                }


#open file with the ads used before
previous_ads = []
with open('todays_gigs_previous_ads.txt') as file:
    previous_ads = file.readlines()

previous_ads = [x.strip() for x in previous_ads]

k = 0
for query in queries:
    for i in locations_us:
        final_string = ""
        for j in locations_us[i]:
            cl_e = CraigslistGigs(site=j, filters={'query': query})
            for result in cl_e.get_results():
                if ((result['datetime'][:10] == yesterday_string) and (not (result['name'] in previous_ads))):
                    # print result
                    final_string = final_string + ("\n '"  + result['name'] + "' -> " + result['url']).encode('utf-8') + "\n"
                    previous_ads.append(result['name'])


        # send an email if the string is not empty
        if (final_string != ""):
            fromaddr = "dml1002313@gmail.com"
            toaddr = "konstantinrubin@engineer.com"
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = i + " '" + query + "': craigslist search results"
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
    k = k + 1
    print k + " out of 6 is done"


f = open('todays_gigs_previous_ads.txt', 'w')
for i in previous_ads:
    f.write(i + "\n")
