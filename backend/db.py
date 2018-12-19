import mysql.connector
import os

#/*
#** Get a connection to the database
#** You need to close this connection when you are done with it
#*/
def getConnection():
    #The user and pass are evn variables. This way we don't publish them on Git!
    cnx = mysql.connector.connect(user=os.getenv('ROW_USER'), password=os.getenv('ROW_PASS'),
                              host='127.0.0.1',#This will have to be your DB at some point
                              database='rowing')
    return(cnx)

def listBoats():
    conn = getConnection()
    curs = conn.cursor()

    curs.execute('SELECT Name,Seats,InUse  FROM boats WHERE Available=1')
    dbres = curs.fetchall()
    res = {}
    res['inhouse'] = []
    res['onriver'] = []
    for boat in dbres:
        b = {'name':boat[0],'seats':boat[1]}
        if boat[2] != 0:
            res['onriver'].append(b)
        else:
            res['inhouse'].append(b)
    conn.close()
    return(res)

def listTables():
    conn = getConnection()
    curs = conn.cursor()

    curs.execute('SHOW Tables')
    dbres = curs.fetchall()
    tables = []
    for t in dbres:
        tables.append(t[0])

    conn.close()
    return(tables)

def checkUser(user,password):
    conn = getConnection()
    curs = conn.cursor()

    query = "SELECT * from users where userName=%s and password=%s"

    curs.execute(query,(user,password))
    dbres = curs.fetchall()
    if len(dbres) == 1:
        return(True)

    return(False)
