import socket, json, database, threading
from controller import OperationController

HOST      = '127.0.0.1'
PORT      = 11111
DATA_SIZE = 8192
BACKLOG   = 5
PARALLEL  = 5

def handleRequest(client, dataSize, semaphore):
	data = client.recv(dataSize).decode()
	try:
		if data:
			print("[API] Receive data: %s" % data)
			response = OperationController(data).call()
			client.send(json.dumps(response).encode())
			print("[API] Response: %s" % json.dumps(response).encode())
	finally:
		semaphore.release()
	client.close()

class Server:
	def __init__(self, host, port, dataSize, parallel, backlog):
		self.host      = host
		self.port      = port
		self.dataSize  = dataSize
		self.parallel  = parallel
		self.backlog   = backlog
		self.sock      = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.semaphore = threading.Semaphore(parallel)

	def listen(self):
		while True:
			print("[API] Waiting to receive message")
			self.semaphore.acquire()
			client, address = self.sock.accept()
			threading.Thread(target=handleRequest, name=str(address), args=(client, self.dataSize, self.semaphore)).start()

	def run(self):
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind((self.host, self.port))
		print("[API] Server is running on %s:%s" % (self.host, self.port))
		self.sock.listen(self.backlog)
		self.listen()

if __name__ == '__main__':
	database.load()
	server = Server(HOST, PORT, DATA_SIZE, PARALLEL, BACKLOG)
	server.run()
