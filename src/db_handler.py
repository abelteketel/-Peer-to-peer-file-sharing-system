import MySQLdb

db = MySQLdb.connect('localhost','root','root','peer2peer')
cursor = db.cursor()
peer_list = []

def get_file_info(file_name):
	sql = "SELECT * FROM file_info where file_name = '%s'" %(file_name)
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			f_id = row[0]
			f_name = row[1]
			f_size = row[2]
			f_type = row[3]
			print f_id,f_name,f_size,f_type
			return f_id

	except:
		print 'ERROR'


def get_owner_peer(id):
	sql = "SELECT * FROM file_owners where file_id = '%d'" %(id)
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		for row in results:
			f_id = row[0]
			file_id = row[1]
			peer_ip = row[2]
			peer_list.append(peer_ip)
			print f_id,file_id,peer_ip
	except:
		print 'ERROR'
	return peer_list;




# get_owner_peer(get_file_info('a.png'));