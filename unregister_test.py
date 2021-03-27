import unittest
import json
from testhelper import payloadFor, cli, resetSid, register, unregister, query

class TestUnregister(unittest.TestCase):
	def setUp(self):
		resetSid("sid-1")

	def testUnregisterSuccessfulResponse(self):
		register(1, "sid-1")
		resp = unregister("sid-1", "name-1")
		self.assertEqual(resp["success"], "true")

	def testUnregisterSuccessfulDatabase(self):
		register(1, "sid-1")
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 1)
		unregister("sid-1", "name-1")
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 0)

	def testUnregisterUnsuccessfulResponse(self):
		resp = unregister("sid-14123", "name-1")
		self.assertEqual(resp["success"], "false")

if __name__ == '__main__':
	unittest.main()
