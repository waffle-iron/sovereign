
############################################################################
######################### SOVEREIGN ENGINES ################################
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
import random
import sov_utils

#################
#### ENGINES ####
def responseEngine(level, packets, input):
	# Combine regexes of matches
	combined = "(" + ")|(".join(packets) + ")"
	if re.match(combined, input, re.IGNORECASE):
		return True
def discourseEngine(load_time, sleep_time, copy):
	if load_time != 0: sov_utils.load(load_time)
	if sleep_time != 0: sleep(sleep_time)
	if copy != "": sov_utils.typewriter(copy)