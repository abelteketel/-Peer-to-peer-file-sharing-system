#bootstrap_servers = {0:"serv0",1:"serv1",2:"serv2",3:"serv3"}

import socket
import random
import peer

class client(object):
	def __init__(self,port=12345):
		self.bootstrap_servers = {0:"127.0.0.1",1:"127.0.0.1",2:"127.0.0.1",3:"127.0.0.1",4:"127.0.0.1"}
		self.port = 12345;


	def choose_rand(self):
		assert (len(self.bootstrap_servers)) > 0
		return self.bootstrap_servers[random.randint(1,len(self.bootstrap_servers))-1];

	
	def request_peer_address(self,peer_req_handler,name):
		s = self.connect_to(address=peer_req_handler)
		assert s is not None
		try:
			s.send('peer_request')
			print s.recv(1024), 'peer_request'
			s.send(name)
			final_peer = s.recv(1024)

		except:
			import logging
			logging.basicConfig(filename='fragment_request.log',level=logging.DEBUG)
			logging.info('Error')
		finally:
			s.close()

		p = peer.peers()
		p.request_file(name,final_peer)



	def request_fragment_handler_address(self,name):
		s=self.connect_to()
		assert s is not None
		try:
			s.send('fragment_owner_server')
			print s.recv(1024)
			s.send(name)
			peer_req_handler_server=s.recv(1024)
		except:
			import logging
			logging.basicConfig(filename='fragment_request.log',level=logging.DEBUG)
			logging.info('Error')
		finally:
			s.close()
		self.request_peer_address(peer_req_handler_server,name)


	def connect_to(self,address=None,port=None):
		s = socket.socket()
		if port is None:
			port = self.port
		if address is None:
			address =  self.choose_rand()

		try:
			s.connect((address,port))
			return s

		except:
			import logging
			logging.basicConfig(filename='errors.log',level=logging.DEBUG)
			logging.info('Error')
		finally:
			s.close


if __name__=="__main__":
	c = client()
	c.request_fragment_handler_address(raw_input("ENTER FILE NAME: "))
