import unittest
import json
from test.testhelper import payloadFor, cli, resetSid, register, unregister, query

class TestQuery(unittest.TestCase):
	def setUp(self):
		resetSid("sid-1")

	def testQueryEmptySid(self):
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 0)

	def testNotEmptySid(self):
		register(1, "sid-1")
		register(2, "sid-1")
		resp = query("sid-1")
		self.assertEqual(len(resp["data"]), 2)

	def testQueryNotExistSid(self):
		resp = query("sid-13030708")
		self.assertEqual(len(resp["data"]), 0)

if __name__ == '__main__':
	unittest.main()
