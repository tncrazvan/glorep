# -*- coding: utf-8 -*-
'''
Created on 18/feb/2016

@author: Fabio Mazzacrelli - Enrico Brensacchi Based on interface of Emanuele Camerieri
'''

import webbrowser
import os, sys
import clientFunctions
import hashlib, base64, string, time
from utility import *
import ntpath

def main(argv=sys.argv):
    if(len(argv)==1):
	print "This is not the correct use for this script!"
	return True
    try:
	if(argv[1].startswith('-')):
		option = argv[1][1:]
		if(option=="check_shared_database"):
			result=clientFunctions.check_shared_database(argv[2])
			write_log("ok "+str(result))
               		return clientFunctions.check_shared_database(argv[2]) # returns a True value if the authentication was correct, a False value
		elif(option=="bootstrap_shared_setup"):
			result=False
			result=clientFunctions.bootstrap_shared_setup(argv[2], argv[3], argv[4], argv[5], argv[6])
			if(type(result)==type(bool()) and result==True): # the shared database responded, so the bootstrap can continue!
                    		write_log("ok bootstrap_shared_setup")
                    		return True
                	elif(type(result)==type(str())):
                    		write_log(str(result)+"bootstrap_shared_setup")
                    		return False
                	else:
                    		write_log("Error bootstrap_shared_setup")
                    		return False
		elif(option=="import_local_federation"):
			result=False
			result=clientFunctions.import_local_federation(argv[2])
			if(type(result)==type(bool()) and result==True): # the shared database responded, so the bootstrap can continue!
                    		write_log("ok import_local_federation")
                    		return True
                	elif(type(result)==type(str())):
                    		write_log(str(result)+"import_local_federation")
                    		return False
                	else:
                    		write_log("Error import_local_federation")
                    		return False
		elif(option=="update_local_fuids"):
			result=False
			result=clientFunctions.update_local_fuids(argv[2], argv[3])
			if(type(result)==type(bool()) and result==True): # the Id_Fd was updating!
                    		write_log("ok update_local_fuids")
                    		return True
                	elif(type(result)==type(str())):
                    		write_log(str(result)+"update_local_fuids")
                    		return False
                	else:
                    		write_log("Error update_local_fuids")
                    		return False
		elif(option=="leave_federation"):
			write_log("ok leave_federation 0 "+argv[2]+"-"+argv[3])
			result=clientFunctions.leave_federation(argv[2], argv[3])
			if(type(result)==type(bool()) and result==True): # the shared database responded, so the bootstrap can continue!
                    		write_log("ok leave_federation")
                    		return True
                	elif(type(result)==type(str())):
                    		write_log(str(result)+"leave_federation")
                    		return False
                	else:
                    		write_log("Error leave_federation")
                    		return False
		elif(option=="exec_remote_cron"):
			result=False
			result=clientFunctions.exec_remote_cron(argv[2])
			if(type(result)==type(bool()) and result==True): # the shared database responded, so the bootstrap can continue!
				write_log("ok exec_remote_cron")
				return True
			elif(type(result)==type(str())):
				write_log(str(result)+"exec_remote_cron")
				return False
			else:
				write_log("Error exec_remote_cron")
				return False
		elif(option=="exec_local_cron"):
			result=False
			result=clientFunctions.exec_local_cron(argv[2])
			if(type(result)==type(bool()) and result==True): # the shared database responded, so the bootstrap can continue!
                    		write_log("ok exec_local_cron")
                    		return True
                	elif(type(result)==type(str())):
                    		write_log(str(result)+"exec_local_cron")
                    		return False
                	else:
                    		write_log("Error exec_local_cron")
                    		return False
    except Error, err:
	write_log("Interface Except")
       	print "Error: incorrect parameter in exec call (except): "+str(err.args)
       	return False

if __name__ == "__main__":
	sys.exit(main())
