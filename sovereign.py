#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3



from time import sleep
from pathlib import Path
import os
import re
import sys
import pickle
import copy
import errno

import sov_utils
import sov_engines
import sov_storyline




###############
#### UTILS ####
# def save_obj(obj, name ):
# 	filename = 'save/momento.pkl'
# 	if not os.path.exists(os.path.dirname(filename)):
# 		try:
# 			os.makedirs(os.path.dirname(filename))
# 		except OSError as exc: # Guard against race condition
# 			if exc.errno != errno.EEXIST:
# 				raise
# 	with open(filename, "w") as f:
# 	    f.write("")

# 	with open('save/'+ name + '.pkl', 'wb') as f:
# 		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
# def load_obj(name ):
# 	filename = 'save/momento.pkl'
# 	if os.path.isfile(filename):
# 		with open('save/' + name + '.pkl', 'rb') as f:
# 			return pickle.load(f)
# 	else:
# 			return False

def boot():
	print("███████╗██████╗  ██╗   ██ ███████ ██████╗ ███████ ██╗ ██████╗ ███╗   ██╗")
	print("██╔════ ██╔═══██ ██║   ██ ██╔════ ██╔══██ ██╔════ ██ ██╔════╝ ████╗  ██║")
	print("███████ ██║   ██ ██║   ██ █████╗  ██████╔ █████╗  ██ ██║  ███ ██╔██╗ ██║")
	print("╚════██ ██║   ██╚██╗ ██╔  ██╔══╝  ██╔══██ ██╔══╝  ██ ██║   ██ ██║╚██╗██║")
	print("███████╚██████╔╝╚████╔╝   ███████ ██║  ██ ███████ ██ ╚ ██████ ██║ ╚████║")
	print("╚══════╝╚═════╝  ╚═══╝    ╚══════ ╚═╝  ╚═ ╚══════ ╚═╝ ╚═════╝ ╚═╝  ╚═══╝")

# def load(itr):
# 	l=0
# 	while l<itr:
# 		print(".")
# 		l+=1
# 		sleep(0.5)

def welcome():
	welcomeMsg = "\nWelcome to the VOID"
	sov_engines.discourseEngine(3, 0, welcomeMsg)

# def typewriter(line):
# 	for x in line:
# 		print(x, end='')
# 		sys.stdout.flush()
# 		sleep(0.05)




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




##############
#### MAIN ####
def section_0():
	
	##########################
	######## PREAMBLE ########
	resume = 0
	moment = {}


	##########################
	#### DATA PERSISTENCE ####
	if not sov_utils.load_obj("momento"):	  # Load save file (if exists)
		moment = {}  
		print("Setting up save data")
		moment = momento()
	else: 
		moment = sov_utils.load_obj("momento")
		# print(moment)


	##########################
	##### INITIALIZATION #####
	boot()
	welcome()


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



