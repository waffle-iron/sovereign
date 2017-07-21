#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import sov_engines
import sov_storyline
import unittest

class SovEnginesTests(unittest.TestCase):
 
	def setUp(self):
		pass
 
 	# def test_dataManagement(self):
 	# 	self.assertEqual( save(), )
 	# 	self.assertEqual( save(), )

	def test_responseEngine_s0_1(self):
		self.assertEqual( sov_engines.responseEngine(0, sov_storyline.respSeed_0, "yes"), True )
	def test_responseEngine_s0_2(self):
		self.assertEqual( sov_engines.responseEngine(0, sov_storyline.respSeed_0, "will"), True )
	def test_responseEngine_s0_3(self):
		self.assertEqual( sov_engines.responseEngine(0, sov_storyline.respSeed_0, "sure"), True )
	def test_responseEngine_s0_4(self):
		self.assertEqual( sov_engines.responseEngine(0, sov_storyline.respSeed_0, "course"), True )

	def test_responseEngine_s1_1(self):
		self.assertEqual( sov_engines.responseEngine(1, sov_storyline.respSeed_1, "go"), True )
	def test_responseEngine_s1_2(self):
		self.assertEqual( sov_engines.responseEngine(1, sov_storyline.respSeed_1, "enter"), True )
	def test_responseEngine_s1_3(self):
		self.assertEqual( sov_engines.responseEngine(1, sov_storyline.respSeed_1, "open"), True )

	def test_responseEngine_s2_1(self):
		self.assertEqual( sov_engines.responseEngine(2, sov_storyline.respSeed_2, "say"), True )
	def test_responseEngine_s2_2(self):
		self.assertEqual( sov_engines.responseEngine(2, sov_storyline.respSeed_2, "speak"), True )
	def test_responseEngine_s2_3(self):
		self.assertEqual( sov_engines.responseEngine(2, sov_storyline.respSeed_2, "shout"), True )

	def test_responseEngine_s3_1(self):
		self.assertEqual( sov_engines.responseEngine(3, sov_storyline.respSeed_3, "find"), True )
	def test_responseEngine_s3_2(self):
		self.assertEqual( sov_engines.responseEngine(3, sov_storyline.respSeed_3, "answer"), True )
	def test_responseEngine_s3_3(self):
		self.assertEqual( sov_engines.responseEngine(3, sov_storyline.respSeed_3, "need"), True )
	def test_responseEngine_s3_4(self):
		self.assertEqual( sov_engines.responseEngine(3, sov_storyline.respSeed_3, "know"), True )
	def test_responseEngine_s3_5(self):
		self.assertEqual( sov_engines.responseEngine(3, sov_storyline.respSeed_3, "aquire"), True )
	def test_responseEngine_s3_6(self):
		self.assertEqual( sov_engines.responseEngine(3, sov_storyline.respSeed_3, "get"), True )


	# def test_responseEngine(self):
	# 	self.assertEqual( sov_engines.responseEngine(3, ['.*find.*','.*answer.*','.*need.*','.*know.*','.*aquire.*','.*get.*'], "get"), True)
 
 
if __name__ == '__main__':
	print("\nSOVERIGN TEST SUITE")
	print("----------------------------------------------------------------------\n")
	unittest.main(verbosity=2)