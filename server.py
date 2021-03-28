import socket
import json
import database
from controller import OperationController

HOST      = '127.0.0.1'
PORT      = 11111
DATA_SIZE = 4096
BACKLOG   = 1

class Server:
	def __init__(self, host, port, dataSize, backlog):
		self.host     = host
		self.port     = port
		self.dataSize = dataSize
		self.backlog  = backlog
		self.sock     = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def listen(self):
		while True:
			print("[API] Waiting to receive message")
			client, address = self.sock.accept()
			data = client.recv(self.dataSize)
			if data:
				print("[API] Receive data: %s" % data)
				response = OperationController(data).call()
				client.send(json.dumps(response).encode())
				print("[API] Response: %s" % json.dumps(response).encode())
			client.close()

	def run(self):
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind((self.host, self.port))
		print("[API] Server is running on %s:%s" % (self.host, self.port))
		self.sock.listen(self.backlog)
		self.listen()

if __name__ == '__main__':
	database.load()
	server = Server(HOST, PORT, DATA_SIZE, BACKLOG)
	server.run()
