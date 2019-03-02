#!/usr/bin/python
#file: visit212121.py
#author: Allison Smith

from datetime import datetime
from datetime import timedelta
from pymongo  import MongoClient

import cgi
import cgitb
cgitb.enable()
#----------------------------------------------------------------------
def getSV ( db, usubjid ):
    ''' this function returns the next sequential visit number (VISITNUM)
        for a given subject (USUBJID) '''
    collection = db.SV
    return collection.find( {'USUBJID': int(usubjid)} ).count()
#----------------------------------------------------------------------
print "Content-type:text/html\r\n\r\n"
print "<head>"
print "<title>Subject Visits</title>"
print "</head> <body>"

client = MongoClient( "mongodb://as652567:743241@localhost:27017/as652567" )
db = client["as652567"]

args = cgi.FieldStorage()
start = args.getvalue("start", 5) 
usubjid = args.getvalue("usubjid")
caseAdd = args.getvalue("caseAdd", False)
addSubmitted = args.getvalue("addSubmitted", False) 

# ADD BUTTON -----------------------------------------------------------
if caseAdd:
    print "<h2> Submit New Visit Instance for Subject " + str(usubjid) + "</h2>"
    print'''<form method='post' action=''>
    <input type='hidden' name='addSubmitted' value='true'/>
    <input type='text'  name='visitText' placeholder='Insert visit information' style='width:300px' required/><br/><br/>
    <input type='reset' value='reset'/><br/><br/>
    <input type='submit' value='Submit Visit Information'></form><br/>'''
    print "<button onclick=location.href='visit212121.py?usubjid="+str(usubjid)+"' value='Return'>Return</button>"

# NEW COMMENT SUBMITTED -------------------------------------------------
elif addSubmitted:
    visitText = args.getvalue("visitText")
    collection = db.SV
    visitnum = getSV( db, usubjid )
    svendtc = datetime.now()
    svendtc = svendtc + timedelta( hours=2, minutes=15 )
    svendtc = svendtc.isoformat()
    visit = { 'STUDYID' : '12700',
              'DOMAIN'  : 'SV',
              'USUBJID' : int(usubjid),
              'VISITNUM': visitnum,
              'VISIT'   : str(visitText),
              'SVSTDTC' : datetime.now().isoformat(),
              'SVENDTC' : svendtc    }
    _id = collection.insert( visit )

    print "<h2> New Visit Instance for Subject " + str(usubjid) + "</h2>"
    for x in db.SV.find({"USUBJID": int(usubjid), "VISITNUM":visitnum}, {"STUDYID":1, "VISITNUM":1, "VISIT":1, "SVSTDTC":1, "SVENDTC": 1}):
        print "<p>USUBJID: " + usubjid + "</br>"
        print "STUDYID: " + str(x["STUDYID"]) + "</br>"
        print "VISITNUM: " + str(x["VISITNUM"])  + "</br>"
        print "VISIT: " + str(x["VISIT"]) + "</br>"
        print "SVSTDTC: " + str(x["SVSTDTC"]) + "</br>"
        print "SVENDTC: " + str(x["SVENDTC"]) + "</p>"

    print "<button onclick=location.href='visit212121.py?usubjid="+str(usubjid)+"' value='Return'>Return</button>"

# NEXT BUTTON PRESSED --------------------------------------------------
elif not (int(start) == 5):
    print "<h2> Visits for Subject " + str(usubjid) + "</h2>"
    print '''<form method='post' action=''> 
    <input type='hidden' name='caseAdd' value='true'/>
    <input type ='submit' value ='Add Visit'/> </form>'''

    for x in db.SV.find({"USUBJID": int(usubjid), "VISITNUM": {"$gt": int(start)-6, "$lt": int(start)+1}}, {"STUDYID":1, "VISITNUM":1, "VISIT":1, "SVSTDTC":1, "SVENDTC": 1}):
        print "<p>USUBJID: " + usubjid + "</br>"
        print "STUDYID: " + str(x["STUDYID"]) + "</br>"
        print "VISITNUM: " + str(x["VISITNUM"])  + "</br>"
        print "VISIT: " + str(x["VISIT"]) + "<br/>"
        print "SVSTDTC: " + str(x["SVSTDTC"]) + "<br/>"
        print "SVENDTC: " + str(x["SVENDTC"]) + "</p>"
   

    # NEXT BUTTON ---------------------------------------
    start=int(start)+5
    print "<form method='post' action=''>" 
    print "<input type='hidden' name='start' value='start'/>"
    print "<input type='button' onclick=location.href='visit212121.py?usubjid="+str(usubjid)+"&start="+str(start)+"' value='Next'></button></form>"

    print "<button onclick=location.href='subject555888.py?usubjid="+str(usubjid)+"' value='Subject Page'>Subject Page</button><br/><br/>"
    print "<button onclick=location.href='comment129000.py?usubjid="+str(usubjid)+"' value='Comment Page'>Comment Page</button><br/><br/>"
    print "<button onclick=location.href='study217698.py' value='Study Page'>Study Page</button>"

# ORIGINAL COMMENT PAGE ------------------------------------------------
else:
    print "<h2> Visits for Subject " + str(usubjid) + "</h2>"
    print '''<form method='post' action=''> 
    <input type='hidden' name='caseAdd' value='true'/>
    <input type ='submit' value ='Add Visit'/> </form>'''

    for x in db.SV.find({"USUBJID": int(usubjid), "VISITNUM": {"$lt": int(start)}}, {"STUDYID":1, "VISITNUM":1, "VISIT":1, "SVSTDTC":1, "SVENDTC": 1}):
        print "<p>USUBJID: " + usubjid + "</br>"
        print "STUDYID: " + str(x["STUDYID"]) + "</br>"
        print "VISITNUM: " + str(x["VISITNUM"])  + "</br>"
        print "VISIT: " + str(x["VISIT"]) + "</br>"
        print "SVSTDTC: " + str(x["SVSTDTC"]) + "</br>"
        print "SVENDTC: " + str(x["SVENDTC"]) + "<p/>"

   # NEXT BUTTON ---------------------------------------
    start=int(start)+5
    print "<form method='post' action=''>" 
    print "<input type='hidden' name='start' value='start'/>"
    print "<input type='button' onclick=location.href='visit212121.py?usubjid="+str(usubjid)+"&start="+str(start)+"' value='Next'></button></form>"

    print "<button onclick=location.href='subject555888.py?usubjid="+str(usubjid)+"'>Subject Page</button><br/><br/>"
    print "<button onclick=location.href='comment129000.py?usubjid="+str(usubjid)+"' value='Comment Page'>Comment Page</button><br/><br/>"
    print "<button onclick=location.href='study217698.py' value='Study Page'>Study Page</button>"

print "</body> </html>"
