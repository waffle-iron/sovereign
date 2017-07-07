#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3



from time import sleep
from pathlib import Path
import os
import re
import sys
import pickle
import copy
import errno
import storyline



def save_obj(obj, name ):
	filename = 'save/momento.pkl'
	if not os.path.exists(os.path.dirname(filename)):
		try:
			os.makedirs(os.path.dirname(filename))
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise
	with open(filename, "w") as f:
	    f.write("")

	with open('save/'+ name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
	filename = 'save/momento.pkl'
	if os.path.isfile(filename):
		with open('save/' + name + '.pkl', 'rb') as f:
			return pickle.load(f)
	else:
			return False

def momento():
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

#def cogito():

def typewriter(line):
	for x in line:
		print(x, end='')
		sys.stdout.flush()
		sleep(0.05)
	# print("\n")

def boot():
    l=0
    while l<4:
        os.system("clear")
        print("\n\nLOADING")
        l+=1
        sleep(1)

def load(itr):
	l=0
	while l<itr:
		print(".")
		l+=1
		sleep(0.5)

def section_0():
	

	##################
	#### PREAMBLE ####

	# INITIALIZE
	# boot()
	resume = 0
	moment = {}



	##########################
	#### DATA PERSISTENCE ####

	# LOAD SAVE FILE (IF EXISTS)
	if not load_obj("momento"):
		moment = {}  
		print("Setting up save data")
		moment = momento()
	else: 
		moment = load_obj("momento")
	# print(moment)




	###################
	#### EXECUTION ####

	typewriter("\nWelcome to the VOID")
	load(3)



	# DECISION FORK I ####
	if not moment["c0"] == 1:
		storyline.branch1(moment)
	else:
		resume = 1


	# DECISION FORK II ####
	if not moment["c1"] == 1:
		if resume == 1: 
			storyline.branch2_resume()
		load(3)
		storyline.branch2(moment)
	else:
		resume = 1


	# DECISION FORK III ####
	if not moment["c2"] == 1:
		if resume == 1: 
			storyline.branch3_resume()
		load(4)
		storyline.branch3(moment)	
	else:
		resume = 1


	# DECISION FORK IV ####
	if not moment["c3"] == 1:
		if resume == 1: 
			storyline.branch4_resume()
		load(4)
		storyline.branch4(moment)
	else:
		resume = 1


if __name__ == '__main__':
    section_0()



