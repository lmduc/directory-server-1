import unittest
import json
import time
from test.testhelper import resetSid, register, unregister, query, exitServer

class TestPersistence(unittest.TestCase):
	def setUp(self):
		resetSid("sid-1")

	def testRegisterPersistence(self):
		register(1, "sid-1")
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 1)
		exitServer()
		time.sleep(0.5)
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 1)

if __name__ == '__main__':
	unittest.main()
