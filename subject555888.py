#!/usr/bin/python
#file: subject555888.py
#author: Allison Smith

from datetime import datetime
from datetime import timedelta
from pymongo  import MongoClient

import cgi
import cgitb
cgitb.enable()
#----------------------------------------------------------------------
print "Content-type:text/html\r\n\r\n"
print "<head>"
print "<title>Subject Demographics</title>"
print "</head> <body>"

client = MongoClient( "mongodb://as652567:743241@localhost:27017/as652567" )
db = client["as652567"]

args = cgi.FieldStorage()
caseDelete = args.getvalue("caseDelete", False)
caseUpdate = args.getvalue("caseUpdate", False)
formSubmittedUpdate = args.getvalue("formSubmittedUpdate", False)
usubjid = args.getvalue("usubjid")

print "<h2> Demographic Information for Subject " + usubjid + "</h2>"
collection =  db.DM

# DELETE SUBJECT BUTTON ------------------------------------------------
if caseDelete:
    print "Subject " + str(usubjid)+ " Sucessfully Deleted</br>"

    #cascading delete: remove subject and all associated comments and visits
    collection.remove({"USUBJID": int(usubjid)})
    db.CO.remove({"USUBJID": int(usubjid)})
    db.SV.remove({"USUBJID": int(usubjid)})
    
    print "<br/><br/><form action ='study217698.py'> <input type ='submit' value ='Return to Study Page'/> </form>"

# UPDATE SUBJECT BUTTON ------------------------------------------------   
elif caseUpdate:
    print "<form method='post' action='' class='formContainer'>"
    print "<input type='hidden' name='formSubmittedUpdate' value='true'/>"
    print "<h2>Update Subject Information</h2>"
    print "Birthdate:<br/><input type='datetime-local' name='birthdate' /><br/>"
    print "Sex:<br/><select name='sex'>"
    print "<option selected disabled hidden value=''>Select</option>"
    print "<option value='Female'>Female</option>"
    print "<option value='male'>Male</option>"
    print "</select><br/>"
    print "Race:<br/><input type='text' name='race' pattern='^[A-Za-z]+$'/><br/>"
    print "Country:<br/><input type='text' name='country' pattern='^[A-Za-z]{3}$' placeholder='ISO Format'/><br/>"
    print "<input type='submit' name='submit' value='submit'/>"
    print "<input type='reset' value='reset'/>"
    print "</form>"
    print "<form action ='study217698.py'> <input type ='submit' value ='Return to Study Page'/> </form>"

# UPDATE SUBJECT SUBMITTED ------------------------------------------------   
elif formSubmittedUpdate:
    birthdate = args.getvalue("birthdate")
    sex = args.getvalue("sex")
    country = args.getvalue("country")
    race = args.getvalue("race")

    #check if input fields were changed or left blank
    if not (str(sex) == "None"):
        collection.update({"USUBJID": int(usubjid)}, {"$set": {"SEX": sex}})
    if not (str(birthdate) == "None"):
        collection.update({"USUBJID": int(usubjid)}, {"$set": {"BRTHDTC": birthdate}})
    if not (str(country) == "None"):
        collection.update({"USUBJID": int(usubjid)}, {"$set": {"COUNTRY": country}})
    if not (str(race) == "None"):
        collection.update({"USUBJID": int(usubjid)}, {"$set": {"RACE": race}})
        
    print "SUBJECT UPDATED"
    for x in collection.find({"USUBJID": int(usubjid)}, {"USUBJID":1, "STUDYID":1, "COUNTRY":1, "BRTHDTC":1, "SEX":1, "RACE":1}):
        print "<p>USUBJID: " + usubjid + "</br>"
        print "STUDYID: " + str(x["STUDYID"]) + "</br>"
        print "BIRTHDATE: " + str(x["BRTHDTC"])  + "</br>"
        print "SEX: " + str(x["SEX"]) + "</br>"
        print "RACE: " + str(x["RACE"]) + "</br>"
        print "COUNTRY: " + str(x["COUNTRY"]) + "<p/></br>"
        
    print "<button onclick=location.href='subject555888.py?usubjid="+str(x['USUBJID'])+"'>Subject Page</button></br></br>"    
    print "<button onclick=location.href='comment129000.py?usubjid="+str(x['USUBJID'])+"'>Subject Comments</button></br></br>"
    print "<button onclick=location.href='visit212121.py?usubjid="+str(x['USUBJID'])+"'>Subject Visits</button>"
    print "<form action ='study217698.py'> <input type ='submit' value ='Return to Study Page'/> </form>"

# INITIAL SUBJECT PAGE ------------------------------------------------------   
else: 
    print '''<form method='post' action=''> 
    <input type='hidden' name='caseUpdate' value='true'/>
    <input type ='submit' value ='Update Subject'/> </form>'''
    print '''<form method='post' action=''> 
    <input type='hidden' name='caseDelete' value='true'/>
    <input type ='submit' value ='Delete Subject' name=''/> </form></br>'''

    for x in collection.find({"USUBJID": int(usubjid)}, {"USUBJID":1, "COUNTRY":1, "STUDYID":1, "BRTHDTC":1, "SEX":1, "RACE":1}):
        print "<p>USUBJID: " + usubjid + "</br>"
        print "STUDYID: " + str(x["STUDYID"]) + "</br>"
        print "BIRTHDATE: " + str(x["BRTHDTC"])  + "</br>"
        print "SEX: " + str(x["SEX"]) + "</br>"
        print "RACE: " + str(x["RACE"]) + "</br>"
        print "COUNTRY: " + str(x["COUNTRY"]) + "<p/></br>"

        print "<button onclick=location.href='comment129000.py?usubjid="+str(x['USUBJID'])+"'>Subject Comments</button></br></br>"
        print "<button onclick=location.href='visit212121.py?usubjid="+str(x['USUBJID'])+"'>Subject Visits</button>"
        print "<form action ='study217698.py'> <input type ='submit' value ='Return to Study Page'/> </form>"

print "</body> </html>"



