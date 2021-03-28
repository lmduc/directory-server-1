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

	def testUnregisterPersistence(self):
		register(1, "sid-1")
		register(2, "sid-1")
		register(3, "sid-1")
		unregister("sid-1", "name-2")
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 2)
		exitServer()
		time.sleep(0.5)
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 2)

	def testResetPersistence(self):
		register(1, "sid-1")
		register(2, "sid-2")
		resetSid("sid-1")
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 0)
		resp = query("sid-2")
		self.assertEqual(len(resp["data"]), 1)
		exitServer()
		time.sleep(0.5)
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 0)
		resp = query("sid-2")
		self.assertEqual(len(resp["data"]), 1)

	def testExitTwice(self):
		register(1, "sid-1")
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 1)
		exitServer()
		time.sleep(0.5)
		exitServer()
		time.sleep(0.5)
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 1)

	def testRegisterAndQuery(self):
		register(1, "sid-1")
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 1)
		exitServer()
		time.sleep(0.5)
		resp = query("sid-1")
		self.assertEqual(resp["data"], { "name-1": "value-1" })

if __name__ == '__main__':
	unittest.main()
