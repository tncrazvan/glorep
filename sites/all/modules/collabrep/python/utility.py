# -*- coding: utf-8 -*-
'''
Created on 18/feb/2016

@author: Fabio Mazzacrelli - Enrico Brensacchi Based on interface of Emanuele Camerieri
'''

from MySQLdb import *
import sys, hashlib, base64, time, urllib2, urllib, httplib, re
from datetime import datetime
import ntpath, posixpath
#from IPy import IP
import pickle

class StringError(Exception):
    def _init_(self, value):
        self.value = value
    def _str_(self):
        return repr(self.value)

if(sys.platform.startswith("win")):
	version="win"
elif(sys.platform.startswith("linux")):
	version="linux"

def get_shared_database_array_access(dbString="",locdb=""):
    if(dbString==""):
        dbString=get_my_drupal_var("collabrep_db_url", locdb)# this is a sample form: mysql://myuser:mypass@127.0.0.1/shared_collabrep_db
    try:
        if(dbString.count(":")==2):
            a=dbString.split("@")
            b=a[0].split(":")
            c=a[1].split("/")
            dbArray={'user': b[1].strip("/"), 'password': b[2], 'host': c[0], 'database': c[1]}
	    write_log("dbArray if "+dbArray['user']+" "+dbArray['host']+" "+dbArray['database'])
            return dbArray
        else:
            a=dbString.split("@")
            b=a[0].split(":")
            c=a[1].split("/")
            dbArray={'user': b[1].strip("/"), 'host': c[0], 'database': c[1], 'password': ""}
	    write_log("dbArray else")
            return dbArray
    except:
	write_log("Errore get_shared_database_array_access")	
	return False

def query_to_shared(query=False,access=""):
    """
    Function that takes a string as a parameter that contains a SQL query.
    SELECT statement: the function returns a correct result set, or a "None" value if there is no result.
    OTHER statements: the function returns the number of the modified rows, or a "None" value if no rows where modified.
    In ALL CASE of database error or if the query is incorrect, the function will return False!!!
    """
    if(query):
	#access=get_shared_database_array_access("",locdb)
	if(type(access)<>type(dict())):
		write_log("Unable to get the data access for the Shared Database")
		return False
        try:
		write_log("querytoshared:"+access['host']+" "+access['user']+" "+access['password']+" "+access['database'])
		dbconn=connect(host=access['host'], user=access['user'], passwd=access['password'], db=access['database'])
		dbcursor = dbconn.cursor(cursors.DictCursor)
		if(query[:3]=="SEL" or query[:3]=="sel"):
			dbcursor.execute(query)
			result_set=dbcursor.fetchall()
			dbcursor.close()
			dbconn.commit()
			dbconn.close()
			return result_set   
		else: # update, insert, delete
			dbcursor.execute(query)
			if(dbcursor.rowcount==0): # number of rows inserted, modified or deleted
				good=None
			elif(dbcursor.rowcount>0):
				good=True
			else: good=False
			dbcursor.close()
                	dbconn.commit()
                	dbconn.close()
                	return good
	except Error, err:
		write_log("Errore di connessione al database! Error %d: %s" % (err.args[0],err.args[1]))
		return False
    else:
	return False

def get_my_drupal_var(variable=None, locdb=""):
    """
    The function returns the value of a variable of Drupal given as a string. It returns the default value if an error occurred.
    The variable type MUST be boolean, string, or integer.
    """
    if(variable<>""):
        access=get_shared_database_array_access(locdb)
        if(type(access)<>type(dict())):
            write_log("Unable to get the data access for the local Drupal Database")
            return False
        try:
            dbconn=connect(host=access['host'], user=access['user'], passwd=access['password'], db=access['database'])
            dbcursor = dbconn.cursor(cursors.DictCursor)
            query="SELECT value FROM variable WHERE name='"+variable+"'"
            dbcursor.execute(query)
            ris=dbcursor.fetchone() # only one result
            dbcursor.close()
            dbconn.commit()
            dbconn.close()     
            value=ris['value']
            if(value[0:2]=="b:"): # booleans
                if (value[2]=="1"):
                    return True
                else:
                    return False
            elif(value[0:2]=="s:"): # strings
                number=value.split(":")[1]
                return value[4+len(str(number)):-2]
            elif(value[0:2]=="i:"): # integers
                return value.split(":")[1][:-1] 
        except:
            return default
    else:
        return default	

def write_log(string):
	if(string!=""):
		try:
			if(version=="win"):
				#logpath=ntpath.dirname(__file__)
				logpath="log\log.txt"
			elif(version=="linux"):
				logpath=posixpath.dirname(__file__)
				logpath+="/log/log.txt"
			f = open(logpath, "a") # open file in appending
			timestampIta=datetime.today().strftime("%a %d/%m/%y, %H:%M:%S")
			f.write("[%s] - " % (timestampIta))
			f.write(string+"\n")
			f.close()
        	except Error, e:
            		print "Error while opening or writing in the file log!"
            		return False

########## DA RIVEDERE ###########
def query_my_drupal_tables_multiple(queryArray,access=""):
    """
    Function that takes an array of string SQL querys as parameter. (probably only insert statements)
    The function returns a True value if the database responds. If some query doesn't work, look at log file.
    The function returns a False value in case of "database connection error".
    """ 
    if(type(access)<>type(dict())):
        write_log("Unable to get the data access for the Local Drupal Database")
        return False
    try:
        #dbconn=connect(host='localhost', user='root', db='dbcondiviso')
        dbconn=connect(host=access['host'], user=access['user'], passwd=access['password'], db=access['database'])
        dbcursor = dbconn.cursor(cursors.DictCursor)
        #end=True
        for query in queryArray:
            if(query):
                try:
                    dbcursor.execute(query)
                    dbconn.commit()
                except:
                    write_log("Error executing query in to the local database: "+query)
                    # to_do locale...
                    #end=False
        dbcursor.close()
        dbconn.close()
        return True
    except:
        write_log("Error connecting to shared database! (function: query_my_drupal_tables_multiple())")
        return False

def decode_glorep(string):
	pass
    
def main():
	print "This is not the correct use!"
	time.sleep(5)
    
if __name__ == "__main__":
	sys.exit(main())
