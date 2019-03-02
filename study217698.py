#!/usr/bin/python
#file: study217698.PY
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
print "<title> Study </title>"
print "</head> <body>"
print "<h1> List of study participants </h1>"
print "<form action ='add168689.py'> <input type ='submit' value ='Add Subject'/> </form>"
print "<form action='insert479012.py'> <input type='submit' value='Insert All'/> </form>"
print "<form action='delete090909.py'> <input type='submit' value='Delete All'/> </form><br/>"

client = MongoClient( "mongodb://as652567:743241@localhost:27017/as652567" )
db = client["as652567"]

args = cgi.FieldStorage()
start = args.getvalue("start", 10)
data = db.DM

# NEXT BUTTON ----------------------------------------------------------  
if not (int(start) == 10):
    #increment start field to indicate next 10 subjects to display
    for x in data.find({"USUBJID": {"$gt": int(start)-11,"$lt": int(start)+1}},{"_id": 0, "USUBJID": 1 }):
                print "id: <a href ='subject555888.py?usubjid=" + str(x['USUBJID']) + "' style='text-decoration:none'>" + str(x['USUBJID'])+"</a> <br/>"
    start=int(start)+10
    print "<form method='post' action=''><input type='hidden' name='start' value='start'><br/><br/>"
    print "<input type='button' onclick=location.href='study217698.py?start="+str(start)+"' value='Next'></button></form>"

# INITIAL STUDY PAGE ----------------------------------------------------  
else:
    for x in data.find({"USUBJID": {"$lt": int(start)}},{"_id": 0, "USUBJID": 1 }):
        print "id: <a href ='subject555888.py?usubjid=" + str(x['USUBJID']) + "' style='text-decoration:none'>" + str(x['USUBJID']) + "</a> <br/>"

    #link to view next 10 subjects
    start=int(start)+10
    print "<form method='post' action=''><input type='hidden' name='start' value='start'><br/><br/>"
    print "<input type='button' onclick=location.href='study217698.py?start="+str(start)+"' value='Next'></button></form>"
    

print "</body> </html>"
