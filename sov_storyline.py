
from time import sleep
# from pathlib import Path
# import os
# import re
# import sys
# import pickle
# import copy
# import errno
import random
import sov_utils
import sov_engines


###################
#### DATABANKS ####
discSeed_0 = ["Beyond the vast nothingness stands before you but one object.", " A white door"]
recSeed_0 = "Making no choice is the same as choosing nothingness. C'est la vie. Dasvidaniya comrade."
respSeed_0 = ['.*yes.*','.*will.*','.*sure.*','.*course.*']

discSeed_1 = ["The white door opens onto a grey room", "within this room there is but one object: ", "a tall, white, leather chair.", " It faces away from you and you realize you cannot move"]
recSeed_1 = "Making no choice is the same as choosing nothingness. C'est la vie. Dasvidaniya comrade."
respSeed_1 = ['.*go.*','.*enter.*','.*open.*']
resumeSeed_1 = ["[D3] Welcome back comrade...\n", "The white door opens onto a grey room", "Beyond the vast nothingness stands before you but one object.", " A white door"]

discSeed_2 = ["'Ah.' ", "'Finally he speaks!', you hear a voice exclaim.", "'Why are you here?', the voice says curtly."]
respSeed_2 = ['.*say.*','.*speak.*','.*shout.*']
recSeed_2 = ["A useless endeavor... ", "You just don't get it do you? ", "Good try, but not quite. "]
resumeSeed_2 = ["[D3] Welcome back comrade...\n", "The white door opens onto a grey room", "within this room there is but one object: ", "a tall, white, leather chair.", " It faces away from you and you realize you cannot move"]

discSeed_3 = ["'Is that so?' ", "'Quite presumtious indeed. No matter, that naivete will be dispelled in due time.'", "so you, correct?", "Well, I'll give you a chioce comrade."]
respSeed_3 = ['.*find.*','.*answer.*','.*need.*','.*know.*','.*aquire.*','.*get.*']
recSeed_3 = ["A useless endeavor... ", "You just don't get it do you?", "Good try, but not quite."]
resumeSeed_3 = ["[D3] Welcome back comrade...\n", "'Ah.' ", "'Finally he speaks!', you hear a voice exclaim.", "'Why are you here?', the voice says curtly."]



##################
#### BRANCHES ####

def branch4(moment):
	choice_3 = input("How do you respond? > ")
	if sov_engines.responseEngine(3, respSeed_3, choice_3):
		moment["c3"] = 1
		sov_utils.save_obj(moment, "momento")
		sov_engines.discourseEngine(4, 0, discSeed_3[0])
		sov_engines.discourseEngine(0, 1, discSeed_3[1])
		sov_engines.discourseEngine(3, 0, discSeed_3[2])
		sov_engines.discourseEngine(3, 0, discSeed_3[3])
	else:
		sov_engines.discourseEngine(2, 0, random.choice(recSeed_3))
		branch4(moment)
def branch4_resume():
	sov_engines.discourseEngine(4, 0, resumeSeed_3[0])
	sov_engines.discourseEngine(2, 0, resumeSeed_3[1])
	sov_engines.discourseEngine(0, 1, resumeSeed_3[2])
	sov_engines.discourseEngine(3, 0, resumeSeed_3[3])

def branch3(moment):
	choice_2 = input("What do you do next? > ")
	if sov_engines.responseEngine(2, respSeed_2, choice_2):
		moment["c2"] = 1
		sov_utils.save_obj(moment, "momento")
		sov_engines.discourseEngine(4, 0, discSeed_2[0])
		sov_engines.discourseEngine(0, 1, discSeed_2[1])
		sov_engines.discourseEngine(3, 0, discSeed_2[2])
	else:
		sov_engines.discourseEngine(2, 0, random.choice(recSeed_2))
		branch3(moment)
def branch3_resume():
	sov_engines.discourseEngine(4, 0, resumeSeed_2[0])
	sov_engines.discourseEngine(2, 0, resumeSeed_2[1])
	sov_engines.discourseEngine(3, 0, resumeSeed_2[2])
	sov_engines.discourseEngine(0, 1, resumeSeed_2[3])
	sov_engines.discourseEngine(0, 1, resumeSeed_2[4])

def branch2(moment):
	choice_1 = input("What do you do? > ")
	if sov_engines.responseEngine(1, respSeed_1, choice_1):
		moment["c1"] = 1
		sov_utils.save_obj(moment, "momento")
		sov_engines.discourseEngine(2, 0, discSeed_1[0])
		sov_engines.discourseEngine(3, 0, discSeed_1[1])
		sov_engines.discourseEngine(0, 1, discSeed_1[2])
		sov_engines.discourseEngine(0, 1, discSeed_1[3])
	else:
		sov_engines.discourseEngine(2, 0, recSeed_1)
		exit(0)
def branch2_resume():
	sov_engines.discourseEngine(4, 0, resumeSeed_2[0])
	sov_engines.discourseEngine(2, 0, resumeSeed_2[1])
	sov_engines.discourseEngine(0, 2, resumeSeed_2[2])

def branch1(moment):
	choice_0 = input("Enter? > ")
	if sov_engines.responseEngine(0, respSeed_0, choice_0):
		moment["c0"] = 1
		sov_utils.save_obj(moment, "momento")
		sov_engines.discourseEngine(2, 0, discSeed_0[0])
		sov_engines.discourseEngine(0, 2, discSeed_0[1])
	else:
		sov_engines.discourseEngine(2, 0, recSeed_0)
		exit(0)


