import unittest
import json
from test.testhelper import payloadFor, cli, resetSid, register, unregister, query

class TestRegister(unittest.TestCase):
	def setUp(self):
		resetSid("sid-1")

	def testRegisterSuccessResponse(self):
		resp = register(1, "sid-1")
		self.assertEqual(resp["success"], "true")

	def testRegisterSuccessDatabase(self):
		register(1, "sid-1")
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 1)

	def testRegisterFailedResponse(self):
		resp = register(1, "sid-1")
		self.assertEqual(resp["success"], "true")
		resp = register(1, "sid-1")
		self.assertEqual(resp["success"], "false")

	def testRegisterFailedDatabase(self):
		register(1, "sid-1")
		register(1, "sid-1")
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 1)

if __name__ == '__main__':
	unittest.main()
