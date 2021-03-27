import client
import unittest
import json
from testhelper import payloadFor, cli, resetSid, register, unregister, query

class TestReset(unittest.TestCase):
	def setUp(self):
		resetSid("sid-1")

	def testResetExistSidResponse(self):
		register(1, "sid-1")
		resp = resetSid("sid-1")
		self.assertEqual(resp["success"], "true")

	def testResetNotEmptySid(self):
		register(1, "sid-1")
		register(2, "sid-1")
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 2)
		resetSid("sid-1")
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 0)

	def testResetNotExistSid(self):
		resp = resetSid("sid-1234")
		self.assertEqual(resp["success"], "true")

if __name__ == '__main__':
	unittest.main()
