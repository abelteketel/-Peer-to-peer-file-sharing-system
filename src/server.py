import socket
import multiprocessing

class server(object):
	def __init__(self,port=12345):
		self.host = "127.0.0.1"
		self.port = port
		self.serv_name=0
		self.s = socket.socket()
		self.range_to_handle = {0:[['a','b','c','d','e'],['f','g','h','i','j']],1:[['f','g','h','i','j']],2:[['k','l','m','n','o']],3:[['p','q','r','s','t'],['a','b','c','d','e']],4:[['u','v','w','x','y','z']]}
		self.bootstrap_servers = {0:"127.0.0.1",1:"127.0.0.1",2:"127.0.0.1",3:"127.0.0.1",4:"127.0.0.1"}

	
	def find_handler(self, name):
		if(name[0] in self.range_to_handle[self.serv_name]):
			return self.serv_name
		else:
			for a in self.range_to_handle.keys():
				for b in self.range_to_handle[a]:
					if(name[0] in b):
						return a
		return -1

	def get_peer(self,connection,addr,file_name):
		connection.send(127.0.0.1)
		connection.close()
		

	#find the correct fragment handler server	
	def process_request_ser(self,connection,addr,file_name):
		try:
			# type(file_name)
			handler_server=self.find_handler(file_name)
			print file_name,handler_server
			connection.send(self.bootstrap_servers[handler_server])
		except:
			import logging
			logging.basicConfig(filename='server_errors.log',level=logging.DEBUG)
			logging.info('Error')	
		finally:
			connection.close()


	def process_request(self,connection,addr):
		print 'Got connection from', addr
		req_kind=connection.recv(1024) #peer request or fragment owner server request
		# print req_kind
		connection.send('confirm')
		file_name=connection.recv(1024)
		# print file_name

		if(req_kind=='fragment_owner_server'):
			self.process_request_ser(connection,addr,file_name)
		else:
			self.get_peer(connection,addr,file_name)
		


	def start(self):
		self.s.bind((self.host,self.port))
		self.s.listen(5)

		while True:
			c, addr = self.s.accept()
			self.process_request(c,addr)




if __name__== "__main__":
	s = server()
	s.start()