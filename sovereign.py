#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3



# from time import sleep
# from pathlib import Path
# import os
# import re
# import sys
# import pickle
# import copy
# import errno

import sov_utils
import sov_engines
import sov_storyline



###############
#### UTILS ####
def boot():
	print("███████╗██████╗  ██╗   ██ ███████ ██████╗ ███████ ██╗ ██████╗ ███╗   ██╗")
	print("██╔════ ██╔═══██ ██║   ██ ██╔════ ██╔══██ ██╔════ ██ ██╔════╝ ████╗  ██║")
	print("███████ ██║   ██ ██║   ██ █████╗  ██████╔ █████╗  ██ ██║  ███ ██╔██╗ ██║")
	print("╚════██ ██║   ██╚██╗ ██╔  ██╔══╝  ██╔══██ ██╔══╝  ██ ██║   ██ ██║╚██╗██║")
	print("███████╚██████╔╝╚████╔╝   ███████ ██║  ██ ███████ ██ ╚ ██████ ██║ ╚████║")
	print("╚══════╝╚═════╝  ╚═══╝    ╚══════ ╚═╝  ╚═ ╚══════ ╚═╝ ╚═════╝ ╚═╝  ╚═══╝")
	print("BUILD 1.0.0")
def welcome():
	welcomeMsg = "\nWelcome to the VOID"
	sov_engines.discourseEngine(3, 0, welcomeMsg)
	print("\n")


####################
#### MECHANISMS ####
def momento():	# DATA PERSISTENCE
	ref = {
		"c0" : 0,
		"c1" : 0,
		"c2" : 0,
		"c3" : 0,
		"c4" : 0,
		"c5" : 0,
		"c6" : 0,
		"c7" : 0,
		"c8" : 0,
		"c9" : 0,
		"c10" : 0,
		"c11" : 0,
		"c12" : 0,
		"c13" : 0,
		"c14" : 0,
		"c15" : 0
	}
	return ref
#def cogito():	# DATA PROGRESSION 
def persist():
	if not sov_utils.load_obj("momento"):	  # Load save file (if exists)
		moment = {}  
		print("Setting up save data")
		return momento()
	else: 
		return sov_utils.load_obj("momento")
		# print(moment)


##############
#### MAIN ####
def section_0():
	
	##########################
	######## PREAMBLE ########
	resume = 0
	moment = {}

	##########################
	##### INITIALIZATION #####
	boot()				# INIT RUN
	moment = persist()	# SETUP DATA PERSISTENCE 
	welcome()			# SETUP INTERFACE
	

	##########################
	######## EXECUTION #######

	# DECISION FORK I 
	if not moment["c0"] == 1:
		sov_storyline.branch1(moment)
	else:
		resume = 1

	# DECISION FORK II 
	if not moment["c1"] == 1:
		if resume == 1: 
			sov_storyline.branch2_resume()
		sov_utils.load(3)
		sov_storyline.branch2(moment)
	else:
		resume = 1

	# DECISION FORK III 
	if not moment["c2"] == 1:
		if resume == 1: 
			sov_storyline.branch3_resume()
		sov_utils.load(4)
		sov_storyline.branch3(moment)	
	else:
		resume = 1

	# DECISION FORK IV 
	if not moment["c3"] == 1:
		if resume == 1: 
			sov_storyline.branch4_resume()
		sov_utils.load(4)
		sov_storyline.branch4(moment)
	else:
		resume = 1






#################################################
################### EXECUTE #####################
#################################################

if __name__ == '__main__':
    section_0()



