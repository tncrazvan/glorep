# -*- coding: utf-8 -*-
'''
Created on 18/feb/2016

@author: Fabio Mazzacrelli - Enrico Brensacchi Based on interface of Emanuele Camerieri
'''

import webbrowser
from utility import *
#import threading, moduleThreading
import urllib2, time
#from create_torrent import *

class sharedSpace(object):
    def __init__(self):
        self.cond=threading.Condition()
        self.arrayOfQuery=[]

class sharedEx(Exception):
    def __init__(self):
        Exception.__init__(self)

def check_shared_database(dbString):
	if(dbString==""):
		write_log("dbString empty error")
		return False
    	else:
	    try:
		write_log("check_shared_database try")
		sharedDb=get_shared_database_array_access(dbString)
		dbconn=connect(host=sharedDb['host'], user=sharedDb['user'], passwd=sharedDb['password'], db=sharedDb['database'])
		dbcursor = dbconn.cursor(cursors.DictCursor)
		dbcursor.close()
		dbconn.close()
		write_log("connection ok")
		return True
            except:
		write_log("connection ko")
		return False

def bootstrap_shared_setup(myName, myUrl, myUser, myPass, locdb):
    """This function creates the required tables in shared database and inform drupal if it can start the bootstrap or not
    """
    try:
	#federationSituation="new_federation"
	#queryToExecute=[]
        #if(federationSituation=="new_federation"):
        #	queryToExecute.append("""CREATE TABLE IF NOT EXISTS collabrep_federation (\
#server_id VARCHAR(20) NOT NULL COMMENT 'The unique server name',\
#server_address VARCHAR(250) NOT NULL COMMENT 'The server address', \
#login_username VARCHAR(50) COMMENT 'The server access username', \
#login_password VARCHAR(50) COMMENT 'The server access password', \
#is_active TINYINT(1) NOT NULL DEFAULT 0 COMMENT 'True if the remote repository has successfully completed the initial join procedure', \
#PRIMARY KEY (server_id, server_address), \
#INDEX fuid_index (server_id), \
#UNIQUE sid_key (server_id), \
#UNIQUE serveraddr_key (server_address)\
#)""")
		#access=get_shared_database_array_access(locdb)
		#write_log("query_to_shared CREATE TABLE collabrep_federation "+str(access))
		#creation=query_to_shared(queryToExecute, access)
		#if(creation==True):
		#	return True
		#elif(not creation):
		#	return "Error in one or more creation tables in shared db: look at the log file!"
		#else:
		#	return "Error"
#            queryToExecute.append("""CREATE TABLE IF NOT EXISTS collabrep_todo (\
#time SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT 'Needed to perform actions chronologically', \
#recipient_id VARCHAR(20) NOT NULL COMMENT 'The unique server ID', \
#event VARCHAR(50) NOT NULL COMMENT 'The action to notify', \
#data TEXT COMMENT 'Subject of the action', \
#INDEX time_index (time)\
#)""")
# the category fields are not nullable so a value MUST be inserted in those fields:
#            queryToExecute.append("""CREATE TABLE IF NOT EXISTS collabrep_vocabulary (\
#global_id VARCHAR (255) NOT NULL, \
#name VARCHAR(255) NOT NULL, \
#description TEXT, \
#help VARCHAR(255) NOT NULL, \
#tags SMALLINT(3) NOT NULL, \
#multiple SMALLINT(3) NOT NULL, \
#required SMALLINT(3) NOT NULL, \
#weight SMALLINT(4) NOT NULL, \
#hierarchy SMALLINT(3) NOT NULL, \
#relations SMALLINT(3) NOT NULL, \
#PRIMARY KEY (global_id)\
#)""")
            
#            queryToExecute.append("""CREATE TABLE IF NOT EXISTS collabrep_term (\
#global_id VARCHAR(255) NOT NULL,\
#name VARCHAR(255) NOT NULL, \
#description TEXT, \
#parent SMALLINT(3) NOT NULL, \
#global_parent VARCHAR (255) NOT NULL, \
#weight SMALLINT(4) NOT NULL, \
#global_vid VARCHAR(255) NOT NULL, \
#PRIMARY KEY (global_id), \
#FOREIGN KEY (global_vid) REFERENCES collabrep_vocabulary(global_id) ON DELETE CASCADE\
#)""")

#            queryToExecute.append("""CREATE TABLE IF NOT EXISTS collabrep_synonyms (\
#synonym_id INTEGER AUTO_INCREMENT, \
#global_tid VARCHAR(255) NOT NULL, \
#synonym VARCHAR(255), \
#PRIMARY KEY (synonym_id), \
#FOREIGN KEY (global_tid) REFERENCES collabrep_term(global_id) ON DELETE CASCADE\
#)""")

    # in all cases
	
#        queryToExecute.append("""CREATE TABLE IF NOT EXISTS """+myName+""" (\
#title VARCHAR(255) NOT NULL COMMENT 'Node title', \
#body TEXT COMMENT 'Node body', \
#fuid VARCHAR(255) NOT NULL COMMENT 'A federation-unique ID', \
#is_software TINYINT(1) NOT NULL DEFAULT 0 COMMENT 'Marks this node as a software, so that other Learning Objects can depend on it', \
#depends_on TEXT NOT NULL COMMENT 'A list of Learning Object the node depends on', \
#file_list TEXT COMMENT 'List of files attached to this Linkable Object', \
#term_list TEXT COMMENT 'List of terms that categorize this Linkable Object', \
#torrent MEDIUMBLOB COMMENT 'Contains the torrent file', \
#lom_entity VARCHAR(1000), \
#lom_keyword VARCHAR(1000), \
#global_id TINYTEXT NOT NULL, \
#lom_aggregation TINYINT(4), \
#lom_learning_resource_type VARCHAR(200), \
#lom_intended_end_user_role VARCHAR(200), \
#lom_context VARCHAR(200), \
#lom_difficulty VARCHAR(200), \
#lom_copyright VARCHAR(5) NOT NULL, \
#INDEX fuid_index (fuid), \
#UNIQUE federuid (fuid))""")
	access=get_shared_database_array_access("",locdb)
        creation=query_to_shared("INSERT INTO LO_Federation VALUES ('"+myName+"','"+myUrl+"','"+myUser+"','"+myPass+"',1,0,0)", access)
        if(creation==True):
            return True
        elif(not creation):
            return "Error in one or more creation/insert query: look at the log file!"
        else:
            return "Error"
    except Error, err:
        return "Errore di connessione al database! Error "+err.args[1]

def update_local_fuids(myRep,locdb):
    """
    arg: the local repository name
    the function is usually called during the botstrap execution;
    it update the fuids of the local LO with the new federation name
    """
    query="SELECT Id_Fd , Id_Lo FROM LO_General ORDER BY Id_Lo ASC"
    access=get_shared_database_array_access(locdb)
    nodeList=query_to_shared(query,access)
    if(type(nodeList)<>type(tuple())):
        return False
    elif(not nodeList): # no local nodes
        return True
    else:
        federation=get_my_drupal_var("collabrep_federation_name", locdb)
        for node in nodeList:      
            splitted=node["Id_Fd"].split(" ") #down here we are updateing fuids to match the federation and repository name
            arQuery=[]
            arQuery.append("UPDATE LO_General SET Id_Fd='"+federation+" "+myRep+" "+splitted[2]+"' WHERE Id_Fd='"+node["Id_Fd"]+"'")
            arQuery.append("UPDATE LO_Contribute SET Id_Fd='"+federation+" "+myRep+" "+splitted[2]+"' WHERE Id_Fd='"+node["Id_Fd"]+"'")
            arQuery.append("UPDATE LO_Educational SET Id_Fd='"+federation+" "+myRep+" "+splitted[2]+"' WHERE Id_Fd='"+node["Id_Fd"]+"'")
            #arQuery.append("UPDATE LO_LifeCycle SET Id_Fd='"+federation+" "+myRep+" "+splitted[2]+"' WHERE Id_Fd='"+node["Id_Fd"]+"'")
            arQuery.append("UPDATE LO_Metadata SET Id_Fd='"+federation+" "+myRep+" "+splitted[2]+"' WHERE Id_Fd='"+node["Id_Fd"]+"'")
            arQuery.append("UPDATE LO_File SET Id_Fd='"+federation+" "+myRep+" "+splitted[2]+"' WHERE Id_Fd='"+node["Id_Fd"]+"'")
	    arQuery.append("UPDATE LO_Identifier SET Id_Fd='"+federation+" "+myRep+" "+splitted[2]+"' WHERE Id_Fd='"+node["Id_Fd"]+"'")
            arQuery.append("UPDATE LO_Requirement SET Id_Fd='"+federation+" "+myRep+" "+splitted[2]+"' WHERE Id_Fd='"+node["Id_Fd"]+"'")
            arQuery.append("UPDATE LO_Rights SET Id_Fd='"+federation+" "+myRep+" "+splitted[2]+"' WHERE Id_Fd='"+node["Id_Fd"]+"'")
            arQuery.append("UPDATE LO_Technical SET Id_Fd='"+federation+" "+myRep+" "+splitted[2]+"' WHERE Id_Fd='"+node["Id_Fd"]+"'")
	    #these queries could also all be executed at the same moment
            ret=query_my_drupal_tables_multiple(arQuery,access)
            if(not ret): #something WRONG
                #stop this procedure
                return False
        return True

def import_local_federation(locdb):
    query="SELECT ServerName , ServerAddress , N_Lo , TimeUpd FROM LO_Federation"
    access=get_shared_database_array_access("",locdb)
    nodeList=query_to_shared(query,access)
    access=get_shared_database_array_access(locdb)
    if(type(nodeList)<>type(tuple())):
        return False
    elif(not nodeList): # no local nodes
        return True
    else:
        for node in nodeList:  
           creation=query_to_shared("INSERT INTO LO_Federation VALUES ('"+node["ServerName"]+"','"+node["ServerAddress"]+"','"+str(node["N_Lo"])+"',0)", access)
	    #these queries could also all be executed at the same moment
        if(creation==True):
           return True
       	elif(not creation):
           return "Error in one or more query: look at the log file!"
        else:
           return "Error"
           
           
def exec_remote_cron(locdb):
	write_log("exec_remote_cron:---------------------------"+str(locdb))
	accesslocal=get_shared_database_array_access(locdb)
	nameFd=get_my_drupal_var("collabrep_my_name", locdb)
	query="SELECT * FROM LO_Federation WHERE ServerName !='"+nameFd+"'"
	accessremote=get_shared_database_array_access("",locdb)
	serverList=query_to_shared(query,accessremote)  # get the serverlist from shared db
	if(type(serverList)<>type(tuple())):
		return False
    	elif(not serverList): # no server to syncronize
		return True
    	else:
		for nodesl in serverList:
			write_log("exec_remore_cron - "+str(nodesl['ServerName'])+" - "+str(nodesl['TimeUpd']))
			query="SELECT ServerName, TimeUpd FROM LO_Federation WHERE ServerName !='"+str(nodesl['ServerName'])+"'"
			serverLocal=query_to_shared(query,accesslocal)
			if (str(serverLocal[0]["TimeUpd"])=="0"): #insert the new federated and his LO in local db
				creation=query_to_shared("INSERT INTO LO_Federation VALUES ('"+nodesl["ServerName"]+"','"+nodesl["ServerAddress"]+"',"+str(nodesl["N_Lo"])+",0)", accesslocal)
				write_log("Insert new federated in local db")
				query="SELECT * FROM LO_General JOIN LO_File ON (LO_General.Id_Fd=LO_File.id_Fd) JOIN LO_Educational ON (LO_Educational.Id_Fd=LO_General.Id_Fd) JOIN LO_Rights ON (LO_Rights.Id_Fd=LO_General.Id_Fd) JOIN LO_Metadata ON (LO_Metadata.Id_Fd=LO_General.Id_Fd) WHERE (LO_General.Id_Fd LIKE '%"+str(nodesl['ServerName'])+"%')"
				#JOIN LO_LifeCycle ON (LO_LifeCycle.Id_Fd=LO_General
				nodeListRemote=query_to_shared(query,accessremote) # get the server's nodelist from shared db
				write_log("if ((str(serverLocal[0][... 1")
			    	if(type(nodeListRemote)<>type(tuple())):
					return False
			    	elif(not nodeListRemote): # no remote nodes
					return True
			    	else:
					for node in nodeListRemote:
						presents=query_to_shared("SELECT COUNT(*) FROM LO_General WHERE Id_Fd ='"+node["Id_Fd"]+"'", accesslocal)
						if(presents[0]["COUNT(*)"]==0):# insert the node into local db if it doesn't exists
							write_log("Insert LO of New federated in local db")
							creation=query_to_shared("INSERT INTO node (type,language,title,created,comment,promote) VALUES ('linkableobject','"+node["Language"]+"','"+node["Title"]+"','"+str(node["TimeUpd"])+"','2','1')", accesslocal)
							nid=query_to_shared("SELECT nid FROM node WHERE title='"+node["Title"]+"'", accesslocal)
							creation=query_to_shared("INSERT INTO node_access (nid,realm,grant_view) VALUES ('"+str(nid[0]["nid"])+"','all','1')", accesslocal)
							creation=query_to_shared("UPDATE node SET vid='"+str(nid[0]["nid"])+"' WHERE nid='"+str(nid[0]["nid"])+"'", accesslocal)
							creation=query_to_shared("INSERT INTO node_revision (nid,vid,title,promote) VALUES ('"+str(nid[0]["nid"])+"','"+str(nid[0]["nid"])+"','"+node["Title"]+"','1')", accesslocal)
							creation=query_to_shared("INSERT INTO node_comment_statistics (nid) VALUES ('"+str(nid[0]["nid"])+"')", accesslocal)
							
							creation=query_to_shared("INSERT INTO file_managed (filename,uri,filemime,filesize,status,timestamp) VALUES ('"+node["filename"]+"','"+node["url"]+"','"+node["filemime"]+"','"+node["filesize"]+"','1','"+str(node["TimeUpd"])+"')",accesslocal)
							fid=query_to_shared("SELECT fid FROM file_managed WHERE uri='"+node["url"]+"'", accesslocal)
							creation=query_to_shared("INSERT INTO file_usage VALUES ('"+str(fid[0]["fid"])+"','file','node','"+str(nid[0]["nid"])+"','1')",accesslocal)
							## insert General
							creation=query_to_shared("INSERT INTO LO_General VALUES ('"+str(nid[0]["nid"])+"','"+node["Id_Fd"]+"','"+node["Title"]+"','"+node["Language"]+"','"+node["Description"]+"','"+node["Keyword"]+"','"+node["Coverage"]+"','"+node["Structure"]+"','"+str(node["Aggregation_Level"])+"','"+str(node["Deleted"])+"','"+str(node["TimeUpd"])+"')", accesslocal)
							if(creation!=True):
					   			return "Error in LO_General insert: look at the log file!"
					   		## insert File
							creation=query_to_shared("INSERT INTO LO_File VALUES ('"+node["Id_Fd"]+"','"+node["url"]+"','"+node["filename"]+"','"+node["filesize"]+"','"+node["filemime"]+"')", accesslocal)
							if(creation!=True):
								return "Error"
							## insert Educational
							creation=query_to_shared("INSERT INTO LO_Educational VALUES (1,'"+node["Id_Fd"]+"','"+str(node["InteractivityType"])+"','"+str(node["LearningResourceType"])+"','"+str(node["InteractivityLevel"])+"','"+str(node["SemanticDensity"])+"','"+str(node["IntendedEndUserRole"])+"','"+str(node["Context"])+"','"+str(node["TypicalAgeRange"])+"','"+str(node["Difficulty"])+"','"+str(node["TypicalLearningTime"])+"','"+str(node["LO_Educational.Description"])+"','"+str(node["LO_Educational.Language"])+"')", accesslocal)
							if(creation!=True):
					   			return "Error in LO_Educational Insert: look at the log file!"
							## insert Rights
							creation=query_to_shared("INSERT INTO LO_Rights VALUES (1,'"+node["Id_Fd"]+"','"+str(node["Cost"])+"','"+str(node["Copyright"])+"','"+str(node["LO_Rights.Description"])+"')", accesslocal)
							if(creation!=True):
					   			return "Error in LO_Rights insert: look at the log file!"
							## insert Metadata
							creation=query_to_shared("INSERT INTO LO_Metadata VALUES (1,'"+node["Id_Fd"]+"','"+str(node["MetadataSchema"])+"','"+str(node["LO_Metadata.Language"])+"')", accesslocal)
							if(creation!=True):
					   			return "Error in LO_Metadata insert: look at the log file!"
							## insert LifeCycle
							#creation=query_to_shared("INSERT INTO LO_LifeCycle VALUES (1,'"+node["Id_Fd"]+"','"+str(node["Version"])+"','"+str(node["Status"])+"')", accesslocal)
							#if(creation!=True):
					   		#	return "Error in LO_LifeCycle insert: look at the log file!"
							## insert Contribute
							ContribList=query_to_shared("SELECT * FROM LO_Contribute WHERE Id_Fd='"+node["Id_Fd"]+"'", accesslocal)				
							write_log("ContribList: "+str(ContribList))	
							if(type(ContribList)<>type(tuple())):
								return False
			    				elif(not ContribList): # no local nodes
								return True
			    				else:
								for Cont in ContribList:  
									creation=query_to_shared("INSERT INTO LO_Contribute VALUES (DEFAULT,'"+node["Id_Fd"]+"','"+str(Cont["Role"])+"','"+str(Cont["Entity"])+"','"+str(Cont["Date"])+"')", accessremote)
									if(creation!=True):
					   					return "Error in LO_Contribute creator insert: look at the log file!"
							## Updating LO_File And Technical
							if(node["Structure"]=='1'):
								write_log("Atomic")
			else:
				if ((str(serverLocal[0]["TimeUpd"]))<>(str(nodesl["TimeUpd"]))):
					query="SELECT * FROM LO_General JOIN LO_File ON (LO_General.Id_Fd=LO_File.Id_Fd) JOIN LO_Educational ON (LO_Educational.Id_Fd=LO_General.Id_Fd) JOIN LO_Rights ON (LO_Rights.Id_Fd=LO_General.Id_Fd) JOIN LO_Metadata ON (LO_Metadata.Id_Fd=LO_General.Id_Fd) WHERE (LO_General.Id_Fd LIKE '%"+str(nodesl['ServerName'])+"%' AND LO_General.TimeUpd >'"+str(serverLocal[0]["TimeUpd"])+"')"
					# JOIN LO_LifeCycle ON (LO_LifeCycle.Id_Fd=LO_General.Id_Fd) 
					nodeListRemote=query_to_shared(query,accessremote) # get the server's nodelist from shared db
				    	if(type(nodeListRemote)<>type(tuple())):
						return False
				    	elif(not nodeListRemote): # no remote nodes
						return True
				    	else:
						for node in nodeListRemote:
							presents=query_to_shared("SELECT COUNT(*) FROM LO_General WHERE Id_Fd ='"+node["Id_Fd"]+"'", accesslocal)
							if(presents[0]["COUNT(*)"]==0):# insert the node into local db if it doesn't exists
								creation=query_to_shared("INSERT INTO node (type,language,title,created,comment,promote) VALUES ('linkableobject','"+node["Language"]+"','"+node["Title"]+"','"+str(node["TimeUpd"])+"','2','1')", accesslocal)
								nid=query_to_shared("SELECT nid FROM node WHERE title='"+node["Title"]+"'", accesslocal)
								creation=query_to_shared("INSERT INTO node_access (nid,realm,grant_view) VALUES ('"+str(nid[0]["nid"])+"','all','1')", accesslocal)
								creation=query_to_shared("UPDATE node SET vid='"+str(nid[0]["nid"])+"' WHERE nid='"+str(nid[0]["nid"])+"'", accesslocal)
								creation=query_to_shared("INSERT INTO node_revision (nid,vid,title,promote) VALUES ('"+str(nid[0]["nid"])+"','"+str(nid[0]["nid"])+"','"+node["Title"]+"','1')", accesslocal)
								creation=query_to_shared("INSERT INTO node_comment_statistics (nid) VALUES ('"+str(nid[0]["nid"])+"')", accesslocal)
							
								creation=query_to_shared("INSERT INTO file_managed (filename,uri,filemime,filesize,status,timestamp) VALUES ('"+node["filename"]+"','"+node["url"]+"','"+node["filemime"]+"','"+node["filesize"]+"','1','"+str(node["TimeUpd"])+"')",accesslocal)
								fid=query_to_shared("SELECT fid FROM file_managed WHERE uri='"+node["url"]+"'", accesslocal)
								creation=query_to_shared("INSERT INTO file_usage VALUES ('"+str(fid[0]["fid"])+"','file','node','"+str(nid[0]["nid"])+"','1')",accesslocal)				
								## insert General
								creation=query_to_shared("INSERT INTO LO_General VALUES (DEFAULT,'"+node["Id_Fd"]+"','"+node["Title"]+"','"+node["Language"]+"','"+node["Description"]+"','"+node["Keyword"]+"','"+node["Coverage"]+"','"+node["Structure"]+"','"+str(node["Aggregation_Level"])+"','"+str(node["Deleted"])+"','"+str(node["TimeUpd"])+"')", accesslocal)
								if(creation!=True):
						   			return "Error in LO_General insert: look at the log file!"
						   		## insert File
								creation=query_to_shared("INSERT INTO LO_File VALUES ('"+node["Id_Fd"]+"','"+node["url"]+"','"+node["filename"]+"','"+node["filesize"]+"','"+node["filemime"]+"')", accesslocal)
								if(creation!=True):
									return "Error"
								## insert Educational
								creation=query_to_shared("INSERT INTO LO_Educational VALUES (1,'"+node["Id_Fd"]+"','"+str(node["InteractivityType"])+"','"+str(node["LearningResourceType"])+"','"+str(node["InteractivityLevel"])+"','"+str(node["SemanticDensity"])+"','"+str(node["IntendedEndUserRole"])+"','"+str(node["Context"])+"','"+str(node["TypicalAgeRange"])+"','"+str(node["Difficulty"])+"','"+str(node["TypicalLearningTime"])+"','"+str(node["LO_Educational.Description"])+"','"+str(node["LO_Educational.Language"])+"')", accesslocal)
								if(creation!=True):
						   			return "Error in LO_Educational Insert: look at the log file!"
								## insert Rights
								creation=query_to_shared("INSERT INTO LO_Rights VALUES (1,'"+node["Id_Fd"]+"','"+str(node["Cost"])+"','"+str(node["Copyright"])+"','"+str(node["LO_Rights.Description"])+"')", accesslocal)
								if(creation!=True):
						   			return "Error in LO_Rights insert: look at the log file!"
								## insert Metadata
								creation=query_to_shared("INSERT INTO LO_Metadata VALUES (1,'"+node["Id_Fd"]+"','"+str(node["MetadataSchema"])+"','"+str(node["LO_Metadata.Language"])+"')", accesslocal)
								if(creation!=True):
						   			return "Error in LO_Metadata insert: look at the log file!"
								## insert LifeCycle
								##creation=query_to_shared("INSERT INTO LO_LifeCycle VALUES (1,'"+node["Id_Fd"]+"','"+str(node["Version"])+"','"+str(node["Status"])+"')", accesslocal)
								##if(creation!=True):
						   		##	return "Error in LO_LifeCycle insert: look at the log file!"
								## insert Contribute
								ContribList=query_to_shared("SELECT * FROM LO_Contribute WHERE Id_Fd='"+node["Id_Fd"]+"'", accesslocal)				
								write_log("ContribList: "+str(ContribList))	
								if(type(ContribList)<>type(tuple())):
									return False
				    				elif(not ContribList): # no local nodes
									return True
				    				else:
									for Cont in ContribList:  
										creation=query_to_shared("INSERT INTO LO_Contribute VALUES (DEFAULT,'"+node["Id_Fd"]+"','"+str(Cont["Role"])+"','"+str(Cont["Entity"])+"','"+str(Cont["Date"])+"')", accesslocal)
										if(creation!=True):
						   					return "Error in LO_Contribute creator insert: look at the log file!"
								## Updating LO_File And Technical
								if(node["Structure"]=='1'):
									write_log("Atomic")
								## Updating LO_Requirement
								## Updating LO_OrComposite

								## Updating LO_Identifier
								## Updating LO_Relation
								## Updating LO_Annotation
								#-----------------------------
							else:
								write_log("else for nodelist - "+str(node['TimeUpd']))
								## update General
				       				creation=query_to_shared("UPDATE LO_General SET Id_Fd='"+node["Id_Fd"]+"', Title='"+node["Title"]+"', Language='"+node["Language"]+"', Description='"+node["Description"]+"', Keyword='"+node["Keyword"]+"', Coverage='"+node["Coverage"]+"', Structure='"+node["Structure"]+"', Aggregation_Level='"+str(node["Aggregation_Level"])+"',Deleted='"+str(node["Deleted"])+"', TimeUpd='"+str(node["TimeUpd"])+"' WHERE Id_Fd='"+node["Id_Fd"]+"'", accesslocal)
								if(creation==False):
						   			return "Error in LO_General Updating: look at the log file!"
								## update Educational
								creation=query_to_shared("UPDATE LO_Educational SET Id_Fd='"+node["Id_Fd"]+"', InteractivityType='"+str(node["InteractivityType"])+"', LearningResourceType='"+str(node["LearningResourceType"])+"',InteractivityLevel='"+str(node["InteractivityLevel"])+"', SemanticDensity='"+str(node["SemanticDensity"])+"', IntendedEndUserRole='"+str(node["IntendedEndUserRole"])+"', Context='"+str(node["Context"])+"', TypicalAgeRange='"+str(node["TypicalAgeRange"])+"', Difficulty='"+str(node["Difficulty"])+"', TypicalLearningTime='"+str(node["TypicalLearningTime"])+"', Description='"+str(node["edu.Description"])+"', Language='"+str(node["edu.Language"])+"' WHERE Id_Fd='"+node["Id_Fd"]+"'", accesslocal)
								if(creation==False):
						   			return "Error in LO_Educational Updating: look at the log file!"
								## update Rights
				       				creation=query_to_shared("UPDATE LO_Rights SET Id_Fd='"+node["Id_Fd"]+"', Cost='"+str(node["Cost"])+"', Copyright='"+str(node["Copyright"])+"', Description='"+str(node["LO_Rights.Description"])+"' WHERE Id_Fd='"+node["Id_Fd"]+"'", accesslocal)
								if(creation==False):
						   			return "Error in LO_Rights Updating: look at the log file!"
								## update Metadata
				       				creation=query_to_shared("UPDATE LO_Metadata SET Id_Fd='"+node["Id_Fd"]+"', MetadataSchema='"+str(node["MetadataSchema"])+"', Language='"+str(node["LO_Metadata.Language"])+"' WHERE Id_Fd='"+node["Id_Fd"]+"'", accesslocal)
								if(creation==False):
						   			return "Error in LO_Metadata Updating: look at the log file!"
						   		## update File	
								creation=query_to_shared("UPDATE LO_File SET Id_Fd='"+node["Id_Fd"]+"', url='"+node["url"]+"', filename='"+node["filename"]+"', filesize='"+node["filesize"]+"',filemime='"+node["filemime"]+"' WHERE Id_Fd='"+node["Id_Fd"]+"'", accesslocal)
						   			
								## update LifeCycle
				       				##creation=query_to_shared("UPDATE LO_LifeCycle SET Id_Fd='"+node["Id_Fd"]+"', Version='"+str(node["Version"])+"', Status='"+str(node["Status"])+"'", accesslocal)
								##if(creation==False):
						   		##	return "Error in LO_LifeCycle Updating: look at the log file!"
								## insert Contribute

								## Updating LO_Identifier
								## Updating LO_Relation
								## Updating LO_Annotation

								## Updating LO_File
								## Updating LO_Technical
								## Updating LO_Requirement
								## Updating LO_OrComposite
								## DA CONTROLLARE------------------------------------
								upd=query_to_shared("UPDATE LO_Federation SET TimeUpd='"+str(node["TimeUpd"])+"' WHERE (ServerName LIKE '%"+str(node['Id_Fd'])+"%')", accesslocal)## update TimeUpd in LO_Federation
								if(upd==False):
						   			return "Error updating TimeUpd in LO_Federation"
        return True

def exec_local_cron(locdb):	
	accesslocal=get_shared_database_array_access(locdb)
	nameFd=get_my_drupal_var("collabrep_my_name", locdb)
	query="SELECT ServerName,TimeUpd FROM LO_Federation WHERE ServerName='"+nameFd+"'"
	TimeUpdServer=query_to_shared(query,accesslocal)
	accesslocal=get_shared_database_array_access(locdb)
	
	## Updating LO_Identifier
	## Updating LO_Relation
	## Updating LO_Annotation

	## Updating LO_File
	## Updating LO_Technical
	## Updating LO_Requirement
	## Updating LO_OrComposite
	query="SELECT * FROM LO_General JOIN LO_File ON (LO_General.Id_Fd=LO_File.Id_Fd) JOIN LO_Educational ON (LO_Educational.Id_Lo=LO_General.Id_Lo AND LO_Educational.Id_Fd=LO_General.Id_Fd) JOIN LO_Rights ON (LO_Rights.Id_Lo=LO_General.Id_Lo AND LO_Rights.Id_Fd=LO_General.Id_Fd) JOIN LO_Metadata ON (LO_Metadata.Id_Lo=LO_General.Id_Lo AND LO_Metadata.Id_Fd=LO_General.Id_Fd) WHERE (LO_General.Id_Fd LIKE '%"+str(nameFd)+"%' AND LO_General.TimeUpd > '"+str(TimeUpdServer[0]["TimeUpd"])+"')" 	
	# JOIN LO_LifeCycle ON (LO_LifeCycle.Id_Lo=LO_General.Id_Lo AND LO_LifeCycle.Id_Fd=LO_General.Id_Fd) 
	nodeList=query_to_shared(query,accesslocal)	
	write_log("RESULT: "+str(nodeList[0]))	
	accessremote=get_shared_database_array_access("",locdb)
    	if(type(nodeList)<>type(tuple())):
        	return False
    	elif(not nodeList): # no local nodes
        	return True
    	else:
        	for node in nodeList:  
			presents=query_to_shared("SELECT COUNT(*) FROM LO_General WHERE Id_Fd ='"+node["Id_Fd"]+"'", accessremote)
			if(presents[0]["COUNT(*)"]==0): 
				## insert General
				creation=query_to_shared("INSERT INTO LO_General VALUES ('"+node["Id_Fd"]+"','"+node["Title"]+"','"+node["Language"]+"','"+node["Description"]+"','"+node["Keyword"]+"','"+node["Coverage"]+"','"+node["Structure"]+"','"+str(node["Aggregation_Level"])+"','"+str(node["Deleted"])+"','"+str(node["TimeUpd"])+"')", accessremote)
				if(creation!=True):
	           			return "Error in LO_General insert: look at the log file!"
	           	## insert File
				creation=query_to_shared("INSERT INTO LO_File VALUES ('"+node["Id_Fd"]+"','"+node["url"]+"','"+node["filename"]+"','"+node["filesize"]+"','"+node["filemime"]+"')", accessremote)
				if(creation!=True):
					return "Error"
				## insert Educational
				creation=query_to_shared("INSERT INTO LO_Educational VALUES ('"+node["Id_Fd"]+"','"+str(node["InteractivityType"])+"','"+str(node["LearningResourceType"])+"','"+str(node["InteractivityLevel"])+"','"+str(node["SemanticDensity"])+"','"+str(node["IntendedEndUserRole"])+"','"+str(node["Context"])+"','"+str(node["TypicalAgeRange"])+"','"+str(node["Difficulty"])+"','"+str(node["TypicalLearningTime"])+"','"+str(node["edu_Description"])+"','"+str(node["edu_Language"])+"')", accessremote)
				if(creation!=True):
	           			return "Error in LO_Educational Insert: look at the log file!"
				## insert Rights
				creation=query_to_shared("INSERT INTO LO_Rights VALUES ('"+node["Id_Fd"]+"','"+str(node["Cost"])+"','"+str(node["Copyright"])+"','"+str(node["rights_Description"])+"')", accessremote)
				if(creation!=True):
	           			return "Error in LO_Rights insert: look at the log file!"
				## insert Metadata
				creation=query_to_shared("INSERT INTO LO_Metadata VALUES ('"+node["Id_Fd"]+"','"+str(node["MetadataSchema"])+"','"+str(node["LO_Metadata.Language"])+"')", accessremote)
				if(creation!=True):
	           			return "Error in LO_Metadata insert: look at the log file!"
	          
				## insert LifeCycle
				##creation=query_to_shared("INSERT INTO LO_LifeCycle VALUES ('"+node["Id_Fd"]+"','"+str(node["Version"])+"','"+str(node["Status"])+"')", accessremote)
				##if(creation!=True):
	           		##	return "Error in LO_LifeCycle insert: look at the log file!"
				## insert Contribute
				ContribList=query_to_shared("SELECT * FROM LO_Contribute WHERE Id_Fd='"+node["Id_Fd"]+"'", accesslocal)				
				write_log("CIAO: "+str(ContribList))	
				if(type(ContribList)<>type(tuple())):
        				return False
    				elif(not ContribList): # no local nodes
        				return True
    				else:
        				for Cont in ContribList:  
						creation=query_to_shared("INSERT INTO LO_Contribute VALUES (DEFAULT,'"+node["Id_Fd"]+"','"+str(Cont["Role"])+"','"+str(Cont["Entity"])+"','"+str(Cont["Date"])+"')", accessremote)
						if(creation!=True):
	           					return "Error in LO_Contribute creator insert: look at the log file!"
				## Updating LO_File And Technical
				if(node["Structure"]=='1'):
					write_log("Atomic")
				## Updating LO_Requirement
				## Updating LO_OrComposite

				## Updating LO_Identifier
				## Updating LO_Relation
				## Updating LO_Annotation
				
			else:
				## update General
				write_log("sono sull'elseeee")
				creation=query_to_shared("UPDATE LO_General SET Id_Fd='"+node["Id_Fd"]+"', Title='"+node["Title"]+"', Language='"+node["Language"]+"', Description='"+node["Description"]+"', Keyword='"+node["Keyword"]+"', Coverage='"+node["Coverage"]+"', Structure='"+node["Structure"]+"', Aggregation_Level='"+str(node["Aggregation_Level"])+"',Deleted='"+str(node["Deleted"])+"', TimeUpd='"+str(node["TimeUpd"])+"' WHERE Id_Fd='"+node["Id_Fd"]+"'", accessremote)
				if(creation==False):
	           			return "Error in LO_General Updating: look at the log file!"
				## update Educational
				creation=query_to_shared("UPDATE LO_Educational SET Id_Fd='"+node["Id_Fd"]+"', InteractivityType='"+str(node["InteractivityType"])+"', LearningResourceType='"+str(node["LearningResourceType"])+"',InteractivityLevel='"+str(node["InteractivityLevel"])+"', SemanticDensity='"+str(node["SemanticDensity"])+"', IntendedEndUserRole='"+str(node["IntendedEndUserRole"])+"', Context='"+str(node["Context"])+"', TypicalAgeRange='"+str(node["TypicalAgeRange"])+"', Difficulty='"+str(node["Difficulty"])+"', TypicalLearningTime='"+str(node["TypicalLearningTime"])+"', Description='"+str(node["edu_Description"])+"', Language='"+str(node["edu_Language"])+"' WHERE Id_Fd='"+node["Id_Fd"]+"'", accessremote)
	        		if(creation==False):
	           			return "Error in LO_Educational Updating: look at the log file!"
				## update Rights
       				creation=query_to_shared("UPDATE LO_Rights SET Id_Fd='"+node["Id_Fd"]+"', Cost='"+str(node["Cost"])+"', Copyright='"+str(node["Copyright"])+"', rights_Description='"+str(node["rights_Description"])+"' WHERE Id_Fd='"+node["Id_Fd"]+"'", accessremote)
				if(creation==False):
	           			return "Error in LO_Rights Updating: look at the log file!"
				## update Metadata
       				creation=query_to_shared("UPDATE LO_Metadata SET Id_Fd='"+node["Id_Fd"]+"', MetadataSchema='"+str(node["MetadataSchema"])+"', Language='"+str(node["LO_Metadata.Language"])+"' WHERE Id_Fd='"+node["Id_Fd"]+"'", accessremote)
				if(creation==False):
	           			return "Error in LO_Metadata Updating: look at the log file!"
				## update File
				write_log("file")
				creation=query_to_shared("UPDATE LO_File SET Id_Fd='"+node["Id_Fd"]+"', url='"+node["url"]+"', filename='"+node["filename"]+"', filesize='"+node["filesize"]+"',filemime='"+node["filemime"]+"' WHERE Id_Fd='"+node["Id_Fd"]+"'", accessremote)
	           			
				## update LifeCycle
       				##creation=query_to_shared("UPDATE LO_LifeCycle SET Id_Fd='"+node["Id_Fd"]+"', Version='"+str(node["Version"])+"', Status='"+str(node["Status"])+"'", accessremote)
				##if(creation==False):
	           		##	return "Error in LO_LifeCycle Updating: look at the log file!"
				## insert Contribute

				## Updating LO_Identifier
				## Updating LO_Relation
				## Updating LO_Annotation

				## Updating LO_File
				## Updating LO_Technical
				## Updating LO_Requirement
				## Updating LO_OrComposite
		#set TimeUpd of the federated TEMPORANEO
		Ok=query_to_shared("UPDATE LO_Federation SET TimeUpd='"+str(node["TimeUpd"])+"' WHERE ServerName='"+nameFd+"'",accessremote)
		#Ok=query_to_shared("UPDATE LO_Federation SET TimeUpd='"+str(node["TimeUpd"])+"' WHERE ServerName='"+nameFd+"'",accesslocal)
	return True


def leave_federation(myVar, locdb):
    """This function creates the required tables in shared database and inform drupal if it can start the bootstrap or not
    """
    try:
	access=get_shared_database_array_access(locdb)
	qresult=query_to_shared("DELETE FROM LO_Federation", access)
	access=get_shared_database_array_access("", locdb)
    	qresult=query_to_shared("DELETE FROM LO_Federation WHERE ServerName='"+myVar+"'", access)
	if(qresult==False): return "Error: the shared database is unreachable."
	elif(qresult==None): return "Wrong execution of the query in shared database."
	elif(qresult==True): return True
	else: return "An error has occurred while executing the query."
    except Error, err:
        return "Errore di connessione al database! Error "+err.args[1]

def main():
	print "Incorrect use for this script."
	time.sleep(5)

if __name__ == "__main__":
	sys.exit(main())
