#vivliothikes pou xriazontai
import urllib2
import re
#isagogi url istoselidas apo ton xristi
ur=raw_input ('Eisagete url:')
#anigma istoselidas
kodikas=urllib2.urlopen(ur)
#diavazei ton kodika html tis istoselidas kai ton apothikevi stin metavliti url_kod
url_kod=kodikas.read()
#elegxos an iparoun allages grammis ston kodika tis istoselidas me </p>
p=len(re.findall("</p>",url_kod))
#elegxos an iparoun allages grammis ston kodika tis istoselidas me <br>
br=len(re.findall("<br>",url_kod))
#elegos an iparoun exoterikoi sindesmoi ston kodika tis selidas 
ahr=len(re.findall("<a href",url_kod))
print ("arithmos allagon grammis pou iparoun stin istoselida me </p>")
print(p)
print ("arithmos allagon grammis pou iparoun stin istoselida me <br>")
print(br)
print ("arithmos sindesmon pou iparoun stin istoselida <a href")
print (ahr)


