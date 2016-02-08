import clients
import socket
import os

class peers(object):
	def __init__(self,resp_port=23456):
		self.host = "127.0.0.1"
		self.resp_port = resp_port
		self.s = socket.socket()
		self.address = socket.gethostbyname(socket.gethostname())

	def get_file_address(self,name):
		return os.getcwd() + '/' + name  # from db

	def send_file(self,name):
		self.s.bind((self.host,self.resp_port))
		self.s.listen(5)
		while True:
			connection, addr = self.s.accept()
			print 'Got Connection @send_file'
			self.transfer_file(connection,addr,name)
			

	def transfer_file(self,connection,addr,name):
		assert type(connection) is not None
		print connection.recv(1024)
		try:
			file_addr = self.get_file_address(file_name)
			file_ptr = open(file_addr,"rb")
			while(True):
				print "sending ..."
				data = file_ptr.read(1024)
				if not data:
					break
				connection.send(data)

			print('FINISEHD')
			connection.send('FINISHED')
		except:
			print "file unavailable"

		finally:
			file_ptr.close()


if __name__== "__main__":
	p = peers()
	p.send_file('a.png')