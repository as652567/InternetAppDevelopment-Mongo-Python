#!/usr/bin/python
#file: comment129000.py
#author: Allison Smith

from datetime import datetime
from datetime import timedelta
from pymongo  import MongoClient

import cgi
import cgitb
cgitb.enable()

#----------------------------------------------------------------------
def getCO ( db, usubjid ):
    ''' this function returns the next sequential comment number (COSEQ)
        for a given subject (USUBJID) '''
    collection = db.CO
    return collection.find( {'USUBJID': int(usubjid)} ).count()
#----------------------------------------------------------------------

print "Content-type:text/html\r\n\r\n"
print "<head>"
print "<title>Subject Comments</title>"
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
    print "<h2> Submit New Comment for Subject " + str(usubjid) + "</h2>"
    print'''<form method='post' action=''>
    <input type='hidden' name='addSubmitted' value='true'/>
    <input type='text' name='comment' placeholder='Insert comment here' required style='width:300px'/><br/><br/>
    <input type='reset' value='reset'/><br/><br/>
    <input type='submit' value='Submit Comment'></form><br/>'''
    print "<button onclick=location.href='comment129000.py?usubjid="+str(usubjid)+"' value='Return'>Return</button>"

# NEW COMMENT SUBMITTED -------------------------------------------------
elif addSubmitted:
    comment = args.getvalue("comment")
    #print "{}".format(comment)
    coseq = getCO( db, usubjid )
    comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': int(usubjid),
            'COSEQ'  : coseq,
            'COVAL'  : str(comment),
            'CODTC'  : datetime.now().isoformat()   }
    _id = db.CO.insert( comment )

    print "<h1>New Comment Submitted for Subject " + str(usubjid) + "</h2><br/>"
    for x in db.CO.find({"USUBJID": int(usubjid), "COSEQ": int(coseq)}, {"USUBJID":1, "STUDYID":1, "COVAL":1, "CODTC":1, "COSEQ":1}):
        print "<p>COSEQ: " + str(x["COSEQ"]) + "</br>"
        print "USUBJID: " + str(usubjid) + "</br>"
        print "STUDYID: " + str(x["STUDYID"]) + "</br>"
        print "COVAL: " + str(x["COVAL"])  + "</br>"
        print "CODTC: " + str(x["CODTC"]) + "<p/></br>"

    print "<button onclick=location.href='comment129000.py?usubjid="+str(usubjid)+"'>Return</button>"

# NEXT BUTTON PRESSED --------------------------------------------------
elif not (int(start) == 5):
    print "<h2> Comments for Subject " + str(usubjid) + "</h2>"
    print '''<form method='post' action=''> 
    <input type='hidden' name='caseAdd' value='true'/>
    <input type ='submit' value ='Add Comment'/> </form>'''

    for x in db.CO.find({"COSEQ": {"$gt": int(start)-6, "$lt": int(start)+1}, "USUBJID": int(usubjid)}, {"STUDYID":1, "COVAL":1, "CODTC":1, "COSEQ":1}):
        print "<p>COSEQ: " + str(x["COSEQ"]) + "</br>"
        print "USUBJID: " + str(usubjid) + "</br>"
        print "STUDYID: " + str(x["STUDYID"]) + "</br>"
        print "COVAL: " + str(x["COVAL"])  + "</br>"
        print "CODTC: " + str(x["CODTC"]) + "<p/></br>"

    # NEXT BUTTON ---------------------------------------
    start=int(start)+5
    print "<form method='post' action=''>" 
    print "<input type='hidden' name='start' value='start'/>"
    print "<input type ='button' onclick=location.href='comment129000.py?usubjid="+str(usubjid)+"&start="+str(start)+"' value ='Next'/> </form>"

    print "<button onclick=location.href='subject555888.py?usubjid="+str(usubjid)+"' value='Subject Page'>Subject Page</button><br/><br/>"
    print "<button onclick=location.href='visit212121.py?usubjid="+str(usubjid)+"' value='Visit Page'>Visit Page</button><br/><br/>"
    print "<button onclick=location.href='study217698.py' value='Study Page'>Return to Study Page</button>"

# ORIGINAL COMMENT PAGE ------------------------------------------------
else:
    print "<h2> Comments for Subject " + str(usubjid) + "</h2>"
    print '''<form method='post' action=''> 
    <input type='hidden' name='caseAdd' value='true'/>
    <input type ='submit' value ='Add Comment'/> </form>'''

    for x in db.CO.find({"COSEQ": {"$lt": int(start)}, "USUBJID": int(usubjid)}, {"STUDYID":1, "COVAL":1, "CODTC":1, "COSEQ":1}):
        print "<p>COSEQ: " + str(x["COSEQ"]) + "</br>"
        print "USUBJID: " + str(usubjid) + "</br>"
        print "STUDYID: " + str(x["STUDYID"]) + "</br>"
        print "COVAL: " + str(x["COVAL"])  + "</br>"
        print "CODTC: " + str(x["CODTC"]) + "<p/>"

   # NEXT BUTTON ---------------------------------------
    start=int(start)+5
    print "<form method='post' action=''>" 
    print "<input type='hidden' name='start' value='start'/>"
    print "<input type ='button' onclick=location.href='comment129000.py?usubjid="+str(usubjid)+"&start="+str(start)+"' value ='Next'/> </form>"

    print "<button onclick=location.href='subject555888.py?usubjid="+str(usubjid)+"'>Subject Page</button><br/><br/>"
    print "<button onclick=location.href='visit212121.py?usubjid="+str(usubjid)+"' value='Visit Page'>Visit Page</button><br/><br/>"
    print "<button onclick=location.href='study217698.py' value='Study Page'>Study Page</button><br/>"

print "</body> </html>"



