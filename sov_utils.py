
############################################################################
########################## SOVEREIGN UTILS #################################
############################################################################

# Copyright 2017 ALEXANDER REID

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

############################################################################


from time import sleep
from pathlib import Path
import os
import re
import sys
import pickle
import copy
import errno


###############
#### UTILS ####

## Animation ##
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

## Data Persisistence ##
def save_obj(obj, name):
	filename = 'save/momento.pkl'
	if not os.path.exists(os.path.dirname(filename)):
		try:
			os.makedirs(os.path.dirname(filename))
		except OSError as exc: # Guard against race condition
			if exc.errno != errno.EEXIST:
				raise
	with open(filename, "w") as f:
	    f.write("")
	    return True

	with open('save/'+ name + '.pkl', 'wb') as f:
		pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
def load_obj(name):
	filename = 'save/momento.pkl'
	if os.path.isfile(filename):
		with open('save/' + name + '.pkl', 'rb') as f:
			return pickle.load(f)
	else:
			return False


