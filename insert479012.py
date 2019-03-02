#!/usr/bin/python
#file: insert479012.py
#author: Allison Smith

from datetime import datetime
from datetime import timedelta
from pymongo  import MongoClient
#----------------------------------------------------------------------
def getDM ( db ):
    ''' this function returns the next sequential subject id (USUBJID) '''
    collection = db.DM
    return collection.find( {} ).count()
#----------------------------------------------------------------------
def getCO ( db, usubjid ):
    ''' this function returns the next sequential comment number (COSEQ)
        for a given subject (USUBJID) '''
    collection = db.CO
    return collection.find( {'USUBJID': int(usubjid)} ).count()
#----------------------------------------------------------------------
def getSV ( db, usubjid ):
    ''' this function returns the next sequential visit number (VISITNUM)
        for a given subject (USUBJID) '''
    collection = db.SV
    return collection.find( {'USUBJID': int(usubjid)} ).count()
#----------------------------------------------------------------------
print "Content-type:text/html\r\n\r\n"
print "<head>"
print "<title> Insert All </title>"
print "</head> <body>"

client = MongoClient( "mongodb://as652567:743241@localhost:27017/as652567" )
db = client.as652567

# SUBJECT 1 ----------------------------------
collection = db.DM
usubjid = getDM( db )
brthdtc = datetime( 2001, 5, 29, 5, 30 )
subject = { 'STUDYID': '12700',
            'DOMAIN' : 'DM',
            'USUBJID': usubjid,
            'BRTHDTC': brthdtc.isoformat(),
            'SEX'    : 'm',
            'RACE'   : 'white',
            'COUNTRY': 'usa'    }
_id = collection.insert( subject )

collection = db.CO
coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is my comment for subject1',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is another comment for subject1',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

collection = db.SV
visitnum = getSV( db, usubjid )
#print( "visitnum=" + str(visitnum) );
#we'll set the start time to now, but we need to send the end time as well.
#  we'll set the end time to 2 hours and 15 minutes from now.
svendtc = datetime.now()
svendtc = svendtc + timedelta( hours=2, minutes=15 )
svendtc = svendtc.isoformat()
visit = { 'STUDYID' : '12700',
          'DOMAIN'  : 'SV',
          'USUBJID' : usubjid,
          'VISITNUM': visitnum,
          'VISIT'   : 'visit for mri imaging study',
          'SVSTDTC' : datetime.now().isoformat(),
          'SVENDTC' : svendtc    }
_id = collection.insert( visit )

# SUBJECT 2 ----------------------------------
collection = db.DM
usubjid = getDM( db )
brthdtc = datetime( 1988, 7, 3, 2, 45 )
subject = { 'STUDYID': '12700',
            'DOMAIN' : 'DM',
            'USUBJID': usubjid,
            'BRTHDTC': brthdtc.isoformat(),
            'SEX'    : 'f',
            'RACE'   : 'black',
            'COUNTRY': 'CHN'    }
_id = collection.insert( subject )

collection = db.CO
coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is my comment for subject2',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is another comment for subject2',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

collection = db.SV
visitnum = getSV( db, usubjid )
#print( "visitnum=" + str(visitnum) );
svendtc = datetime.now()
svendtc = svendtc + timedelta( hours=2, minutes=15 )
svendtc = svendtc.isoformat()
visit = { 'STUDYID' : '12700',
          'DOMAIN'  : 'SV',
          'USUBJID' : usubjid,
          'VISITNUM': visitnum,
          'VISIT'   : 'visit for mri imaging study for subject2',
          'SVSTDTC' : datetime.now().isoformat(),
          'SVENDTC' : svendtc    }
_id = collection.insert( visit )

# SUBJECT 3 ----------------------------------
collection = db.DM
usubjid = getDM( db )
brthdtc = datetime( 1999, 10, 11, 12, 30 )
subject = { 'STUDYID': '12700',
            'DOMAIN' : 'DM',
            'USUBJID': usubjid,
            'BRTHDTC': brthdtc.isoformat(),
            'SEX'    : 'm',
            'RACE'   : 'asian',
            'COUNTRY': 'CAN'    }
_id = collection.insert( subject )

collection = db.CO
coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is my comment for subject3',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is another comment for subject3',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

collection = db.SV
visitnum = getSV( db, usubjid )
#print( "visitnum=" + str(visitnum) );
svendtc = datetime.now()
svendtc = svendtc + timedelta( hours=2, minutes=15 )
svendtc = svendtc.isoformat()
visit = { 'STUDYID' : '12700',
          'DOMAIN'  : 'SV',
          'USUBJID' : usubjid,
          'VISITNUM': visitnum,
          'VISIT'   : 'visit for mri imaging study for subject3',
          'SVSTDTC' : datetime.now().isoformat(),
          'SVENDTC' : svendtc    }
_id = collection.insert( visit )

# SUBJECT 4 ----------------------------------
collection = db.DM
usubjid = getDM( db )
brthdtc = datetime( 2005, 2, 8, 11, 25 )
subject = { 'STUDYID': '12700',
            'DOMAIN' : 'DM',
            'USUBJID': usubjid,
            'BRTHDTC': brthdtc.isoformat(),
            'SEX'    : 'f',
            'RACE'   : 'white',
            'COUNTRY': 'MEX'    }
_id = collection.insert( subject )

collection = db.CO
coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is my comment for subject4',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is another comment for subject4',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

collection = db.SV
visitnum = getSV( db, usubjid )
#print( "visitnum=" + str(visitnum) );
svendtc = datetime.now()
svendtc = svendtc + timedelta( hours=2, minutes=15 )
svendtc = svendtc.isoformat()
visit = { 'STUDYID' : '12700',
          'DOMAIN'  : 'SV',
          'USUBJID' : usubjid,
          'VISITNUM': visitnum,
          'VISIT'   : 'visit for mri imaging study for subject4',
          'SVSTDTC' : datetime.now().isoformat(),
          'SVENDTC' : svendtc    }
_id = collection.insert( visit )

# SUBJECT 5 ----------------------------------
collection = db.DM
usubjid = getDM( db )
brthdtc = datetime( 1990, 8, 25, 1, 10 )
subject = { 'STUDYID': '12700',
            'DOMAIN' : 'DM',
            'USUBJID': usubjid,
            'BRTHDTC': brthdtc.isoformat(),
            'SEX'    : 'm',
            'RACE'   : 'black',
            'COUNTRY': 'usa'    }
_id = collection.insert( subject )

collection = db.CO
coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is my comment for subject5',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is another comment for subject5',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

collection = db.SV
visitnum = getSV( db, usubjid )
#print( "visitnum=" + str(visitnum) );
svendtc = datetime.now()
svendtc = svendtc + timedelta( hours=2, minutes=15 )
svendtc = svendtc.isoformat()
visit = { 'STUDYID' : '12700',
          'DOMAIN'  : 'SV',
          'USUBJID' : usubjid,
          'VISITNUM': visitnum,
          'VISIT'   : 'visit for mri imaging study for subject5',
          'SVSTDTC' : datetime.now().isoformat(),
          'SVENDTC' : svendtc    }
_id = collection.insert( visit )

# SUBJECT 6 ----------------------------------
collection = db.DM
usubjid = getDM( db )
brthdtc = datetime( 1992, 3, 28, 8, 50 )
subject = { 'STUDYID': '12700',
            'DOMAIN' : 'DM',
            'USUBJID': usubjid,
            'BRTHDTC': brthdtc.isoformat(),
            'SEX'    : 'f',
            'RACE'   : 'white',
            'COUNTRY': 'per'    }
_id = collection.insert( subject )

collection = db.CO
coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is my comment for subject6',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is another comment for subject6',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

collection = db.SV
visitnum = getSV( db, usubjid )
#print( "visitnum=" + str(visitnum) );
svendtc = datetime.now()
svendtc = svendtc + timedelta( hours=2, minutes=15 )
svendtc = svendtc.isoformat()
visit = { 'STUDYID' : '12700',
          'DOMAIN'  : 'SV',
          'USUBJID' : usubjid,
          'VISITNUM': visitnum,
          'VISIT'   : 'visit for mri imaging study for subject6',
          'SVSTDTC' : datetime.now().isoformat(),
          'SVENDTC' : svendtc    }
_id = collection.insert( visit )

# SUBJECT 7 ----------------------------------
collection = db.DM
usubjid = getDM( db )
brthdtc = datetime( 2004, 6, 27, 3, 30 )
subject = { 'STUDYID': '12700',
            'DOMAIN' : 'DM',
            'USUBJID': usubjid,
            'BRTHDTC': brthdtc.isoformat(),
            'SEX'    : 'm',
            'RACE'   : 'latino',
            'COUNTRY': 'PAN'    }
_id = collection.insert( subject )

collection = db.CO
coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is my comment for subject7',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is another comment for subject7',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

collection = db.SV
visitnum = getSV( db, usubjid )
#print( "visitnum=" + str(visitnum) );
svendtc = datetime.now()
svendtc = svendtc + timedelta( hours=2, minutes=15 )
svendtc = svendtc.isoformat()
visit = { 'STUDYID' : '12700',
          'DOMAIN'  : 'SV',
          'USUBJID' : usubjid,
          'VISITNUM': visitnum,
          'VISIT'   : 'visit for mri imaging study for subject7',
          'SVSTDTC' : datetime.now().isoformat(),
          'SVENDTC' : svendtc    }
_id = collection.insert( visit )

# SUBJECT 8 ----------------------------------
collection = db.DM
usubjid = getDM( db )
brthdtc = datetime( 2006, 12, 30, 8, 30 )
subject = { 'STUDYID': '12700',
            'DOMAIN' : 'DM',
            'USUBJID': usubjid,
            'BRTHDTC': brthdtc.isoformat(),
            'SEX'    : 'f',
            'RACE'   : 'latina',
            'COUNTRY': 'usa'    }
_id = collection.insert( subject )

collection = db.CO
coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is my comment for subject8',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is another comment for subject8',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

collection = db.SV
visitnum = getSV( db, usubjid )
#print( "visitnum=" + str(visitnum) );
svendtc = datetime.now()
svendtc = svendtc + timedelta( hours=2, minutes=15 )
svendtc = svendtc.isoformat()
visit = { 'STUDYID' : '12700',
          'DOMAIN'  : 'SV',
          'USUBJID' : usubjid,
          'VISITNUM': visitnum,
          'VISIT'   : 'visit for mri imaging study for subject8',
          'SVSTDTC' : datetime.now().isoformat(),
          'SVENDTC' : svendtc    }
_id = collection.insert( visit )

# SUBJECT 9 ----------------------------------
collection = db.DM
usubjid = getDM( db )
brthdtc = datetime( 1996, 7, 12, 4, 21 )
subject = { 'STUDYID': '12700',
            'DOMAIN' : 'DM',
            'USUBJID': usubjid,
            'BRTHDTC': brthdtc.isoformat(),
            'SEX'    : 'f',
            'RACE'   : 'white',
            'COUNTRY': 'usa'    }
_id = collection.insert( subject )

collection = db.CO
coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is my comment for subject9',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is another comment for subject9',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

collection = db.SV
visitnum = getSV( db, usubjid )
#print( "visitnum=" + str(visitnum) );
svendtc = datetime.now()
svendtc = svendtc + timedelta( hours=2, minutes=15 )
svendtc = svendtc.isoformat()
visit = { 'STUDYID' : '12700',
          'DOMAIN'  : 'SV',
          'USUBJID' : usubjid,
          'VISITNUM': visitnum,
          'VISIT'   : 'visit for mri imaging study for subject9',
          'SVSTDTC' : datetime.now().isoformat(),
          'SVENDTC' : svendtc    }
_id = collection.insert( visit )

# SUBJECT 10 ----------------------------------
collection = db.DM
usubjid = getDM( db )
brthdtc = datetime( 1994, 10, 17, 12, 10 )
subject = { 'STUDYID': '12700',
            'DOMAIN' : 'DM',
            'USUBJID': usubjid,
            'BRTHDTC': brthdtc.isoformat(),
            'SEX'    : 'f',
            'RACE'   : 'white',
            'COUNTRY': 'usa'    }
_id = collection.insert( subject )

collection = db.CO
coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is my comment for subject10',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is another comment for subject10',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

collection = db.SV
visitnum = getSV( db, usubjid )
#print( "visitnum=" + str(visitnum) );
svendtc = datetime.now()
svendtc = svendtc + timedelta( hours=2, minutes=15 )
svendtc = svendtc.isoformat()
visit = { 'STUDYID' : '12700',
          'DOMAIN'  : 'SV',
          'USUBJID' : usubjid,
          'VISITNUM': visitnum,
          'VISIT'   : 'visit for mri imaging study for subject10',
          'SVSTDTC' : datetime.now().isoformat(),
          'SVENDTC' : svendtc    }
_id = collection.insert( visit )

# SUBJECT 11 ----------------------------------
collection = db.DM
usubjid = getDM( db )
brthdtc = datetime( 1997, 9, 15, 20, 24 )
subject = { 'STUDYID': '12700',
            'DOMAIN' : 'DM',
            'USUBJID': usubjid,
            'BRTHDTC': brthdtc.isoformat(),
            'SEX'    : 'f',
            'RACE'   : 'black',
            'COUNTRY': 'usa'    }
_id = collection.insert( subject )

collection = db.CO
coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is my comment for subject11',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is another comment for subject11',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

collection = db.SV
visitnum = getSV( db, usubjid )
#print( "visitnum=" + str(visitnum) );
svendtc = datetime.now()
svendtc = svendtc + timedelta( hours=2, minutes=15 )
svendtc = svendtc.isoformat()
visit = { 'STUDYID' : '12700',
          'DOMAIN'  : 'SV',
          'USUBJID' : usubjid,
          'VISITNUM': visitnum,
          'VISIT'   : 'visit for mri imaging study for subject11',
          'SVSTDTC' : datetime.now().isoformat(),
          'SVENDTC' : svendtc    }
_id = collection.insert( visit )

# SUBJECT 12 ----------------------------------
collection = db.DM
usubjid = getDM( db )
brthdtc = datetime( 1990, 11, 2, 21, 35 )
subject = { 'STUDYID': '12700',
            'DOMAIN' : 'DM',
            'USUBJID': usubjid,
            'BRTHDTC': brthdtc.isoformat(),
            'SEX'    : 'f',
            'RACE'   : 'asian',
            'COUNTRY': 'FRA'    }
_id = collection.insert( subject )

collection = db.CO
coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is my comment for subject12',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

coseq = getCO( db, usubjid )
#print( "coseq=" + str(coseq) );
comment = { 'STUDYID': '12700',
            'DOMAIN' : 'CO',
            'USUBJID': usubjid,
            'COSEQ'  : coseq,
            'COVAL'  : 'this is another comment for subject12',
            'CODTC'  : datetime.now().isoformat()   }
_id = collection.insert( comment )

collection = db.SV
visitnum = getSV( db, usubjid )
#print( "visitnum=" + str(visitnum) );
svendtc = datetime.now()
svendtc = svendtc + timedelta( hours=2, minutes=15 )
svendtc = svendtc.isoformat()
visit = { 'STUDYID' : '12700',
          'DOMAIN'  : 'SV',
          'USUBJID' : usubjid,
          'VISITNUM': visitnum,
          'VISIT'   : 'visit for mri imaging study for subject12',
          'SVSTDTC' : datetime.now().isoformat(),
          'SVENDTC' : svendtc    }
_id = collection.insert( visit )


print "<h2>Insert All Sucessfully Completed</h2><br/><br/>"
print "<form action='study217698.py'><input type='submit' value='Return to Study Page'/></form>"
print "</body> </html>"

