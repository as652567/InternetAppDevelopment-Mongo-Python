#!/usr/bin/python
#file: add168689.py
#author: Allison Smith

from datetime import datetime
from datetime import timedelta
from pymongo  import MongoClient

import cgi
import cgitb
import sys
cgitb.enable() #troubleshooting
#----------------------------------------------------------------------
def getDM ( db ):
    ''' this function returns the next sequential subject id (USUBJID) '''
    collection = db.DM
    return collection.find( {} ).count()
#----------------------------------------------------------------------

print "Content-type:text/html\r\n\r\n"
print "<head>"
print "<title>Add Subject </title>"
print "</head> <body>"

client = MongoClient( "mongodb://as652567:743241@localhost:27017/as652567" )
db = client["as652567"]


args = cgi.FieldStorage()

birthdate = args.getvalue("birthdate")
sex = args.getvalue("sex")
race = args.getvalue("race")
country = args.getvalue("country")
formSubmitted = args.getvalue("formSubmitted", False)

if not formSubmitted:
    print "<form method='post' action='' class='formContainer'>"
    print "<input type='hidden' name ='formSubmitted' value='true'>"
    print "<h2>Add Subject Information</h2>"
    print "Birthdate:<br/><input type='datetime-local' name='birthdate' required/><br/>"
    print "Sex:<br/><select required name='sex'>"
    print "<option selected disabled hidden value=''>Select</option>"
    print "<option value='Female'>Female</option>"
    print "<option value='male'>Male</option>"
    print "</select><br/>"
    print "Race:<br/><input type='text' name='race' required pattern='^[A-Za-z]+$'/><br/>"
    print "Country:<br/><input type='text' name='country' required pattern='^[A-Za-z]{3}$' placeholder='ISO Format'/><br/>"
    print "<input type='submit' name='submit' value='submit'/>"
    print "<input type='reset' value='reset'/><br/>"
    print "</form>"

    print "<button onclick=location.href='study217698.py'>Return to Study Page</button>"
else:

    #birthdate = args.getvalue("birthdate")
    #sex = args.getvalue("sex")
    #race = args.getvalue("race")
    #country = args.getvalue("country")
    #insert new subject
    usubjid = getDM(db)
    subject = { 'STUDYID': '12700',
                'DOMAIN': 'DM',
                'USUBJID': usubjid,
                'BRTHDTC': birthdate,
                'SEX': sex,
                'RACE': race,
                'COUNTRY': country    }
    _id = db.DM.insert(subject)

    #Create output message
    print "<h3> You have sucessfully entered a new subject! </h3>"
    print "birthdate = {} <br/>".format(birthdate)
    print "race = {} <br/>".format(race)
    print "country = {} <br/>".format(country)
    print "</br></br>"
    print "<form action='study217698.py'><input type='submit' value='Return to Study'/><form/>"

print "</body> </html>"

