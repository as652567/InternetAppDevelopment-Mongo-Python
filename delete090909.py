#!/usr/bin/python
#file: delete090909.py
#author: Allison Smith

from pymongo  import MongoClient

#-------------------------------------------------------------------------

print "Content-type:text/html\r\n\r\n"
print "<head>"
print "<title> Delete </title>"
print "</head> <body>"


client = MongoClient( "mongodb://as652567:743241@localhost:27017/as652567" )
db = client.as652567

deleted_DM = db.DM.delete_many({})
deleted_CO = db.CO.delete_many({})
deleted_SV = db.SV.delete_many({})

print "<h3> All entries deleted. </h3>"
print "<button onclick=location.href='study217698.py'>Return to Study Page</button>"
print "</body> </html>"
