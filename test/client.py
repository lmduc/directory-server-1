import socket
import unittest

class Client:
	def __init__(self, host, port, dataSize):
		self.host 		= host
		self.port 		= port
		self.dataSize = dataSize
		self.sock 		= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def sendMessage(self, payload):
		self.sock.send(payload.encode())

	def receiveMessage(self) -> str:
		data = self.sock.recv(self.dataSize)
		return data.decode()

	def request(self, payload):
		response = ""
		try:
			self.sock.connect((self.host, self.port))
			self.sendMessage(payload)

			while True:
				data = self.receiveMessage()
				if not data:
					break
				response += data
		except Exception as e:
			print("Socket error: %s" %str(e))
		finally:
			self.sock.close()
			return response
