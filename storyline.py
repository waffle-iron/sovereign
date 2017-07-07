
from time import sleep
from pathlib import Path
import os
import re
import sys
import pickle
import copy
import errno
import storyline
import random



###############
#### UTILS ####
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
def load(itr):
	l=0
	while l<itr:
		print(".")
		l+=1
		sleep(0.5)
def typewriter(line):
	for x in line:
		print(x, end='')
		sys.stdout.flush()
		sleep(0.05)


#################
#### ENGINES ####
def responseEngine(level, packets, input):
	# Make a regex that matches if any of our regexes match.
	combined = "(" + ")|(".join(packets) + ")"
	if re.match(combined, input):
		return True
def discourseEngine(load_time, sleep_time, copy):
	if load_time != 0: load(load_time)
	if sleep_time != 0: sleep(sleep_time)
	if copy != "": typewriter(copy)


##################
#### BRANCHES ####



def branch4(moment):
	choice_3 = input("How do you respond? > ")
	respSeed_3 = ['.*find.*','.*answer.*','.*need.*','.*know.*','.*aquire.*','.*get.*']
	recSeed_3 = ["A useless endeavor... ", "You just don't get it do you?", "Good try, but not quite."]
	discSeed_3 = ["'Is that so?' ", "'Quite presumtious indeed. No matter, that naivete will be dispelled in due time.'", "so you, '"+choice_3+"', correct?", "Well, I'll give you a chioce comrade."]

	if responseEngine(3, respSeed_3, choice_3):
		moment["c3"] = 1
		save_obj(moment, "momento")
		discourseEngine(4, 0, discSeed_3[0])
		discourseEngine(0, 1, discSeed_3[1])
		discourseEngine(3, 0, discSeed_3[2])
		discourseEngine(3, 0, discSeed_3[3])
		discourseEngine(3, 0, random.choice(recSeed_3))
	else:
		discourseEngine(2, 0, )
		branch4(moment)
def branch4_resume():
	load(4)
	typewriter("[D4] Welcome back comrade...\n")
	load(2)
	typewriter("'Ah.' ")
	sleep(1)
	typewriter("'Finally you speak!', you hear a voice exclaim.")
	load(3)
	typewriter("'Why are you here?', the voice says curtly.")

def branch3(moment):
	choice_2 = input("What do you do? > ")
	respSeed_2 = ['.*say.*','.*speak.*','.*shout.*']
	discSeed_2 = ["'Ah.' ", "'Finally he speaks!', you hear a voice exclaim.", "'Why are you here?', the voice says curtly."]

	if responseEngine(2, respSeed_2, choice_2):
		moment["c2"] = 1
		save_obj(moment, "momento")
		discourseEngine(4, 0, discSeed_2[0])
		discourseEngine(0, 1, discSeed_2[1])
		discourseEngine(3, 0, discSeed_2[2])
	else:
		load(2)
		typewriter("A useless endeavor... ")
		branch3(moment)
def branch3_resume():
	load(4)
	typewriter("[D3] Welcome back comrade...\n")
	load(2)
	typewriter("The white door opens onto a grey room")
	load(3)
	typewriter("Within this room there is but one object: ")
	sleep(1)
	typewriter("a tall, white, leather chair.")
	sleep(1)
	typewriter(" It faces away from you and you realize you cannot move")

def branch2(moment):
	choice_1 = input("What do you do? > ")
	respSeed_1 = ['.*go.*','.*enter.*','.*open.*']
	discSeed_1 = ["The white door opens onto a grey room", "within this room there is but one object: ", "a tall, white, leather chair.", " It faces away from you and you realize you cannot move"]

	if responseEngine(1, respSeed_1, choice_1):
		moment["c1"] = 1
		save_obj(moment, "momento")
		discourseEngine(2, 0, discSeed_1[0])
		discourseEngine(3, 0, discSeed_1[1])
		discourseEngine(0, 1, discSeed_1[2])
		discourseEngine(0, 1, discSeed_1[3])
	else:
		load(2)
		typewriter("Makeing no choice is the same as choosing nothingness. C'est la vie. Dasvidaniya comrade.")
		exit(0)
def branch2_resume():
	load(4)
	typewriter("[D2] Welcome back comrade...\n")
	load(2)
	typewriter("Beyond the vast nothingness stands before you but one object.")
	sleep(2)
	typewriter(" A white door")

def branch1(moment):
	choice_0 = input("Enter? > ")
	respSeed_0 = ['.*yes.*','.*will.*','.*sure.*','.*course.*']
	discSeed_0 = ["Beyond the vast nothingness stands before you but one object.", " A white door"]

	if responseEngine(0, respSeed_0, choice_0):
		moment["c0"] = 1
		save_obj(moment, "momento")
		discourseEngine(2, 0, discSeed_0[0])
		discourseEngine(0, 2, discSeed_0[1])
	else:
		load(2)
		typewriter("Makeing no choice is the same as choosing nothingness. C'est la vie. Dasvidaniya comrade.")
		exit(0)


