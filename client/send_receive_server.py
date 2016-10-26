from socket import *
import time
host = ''
port = 5005
address = (host,port)
buf = 1024
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(address)
sock.listen(1)
print ("Waiting to receive messages...")
conn,addr = sock.accept()
print ('Connection address:',addr)
while True:
	try:
		# Receive the data in small chunks and retransmit it
		while True:
			data = conn.recv(buf)
			print("received: ", data)
			if data:
                		print ('sending data back to the client')
				conn.send(data.encode('utf-8'))	
			else:
				print ('no more data from', addr)
				break
      	finally:
		print("Closing connection")
		conn.close()
		conn,addr = sock.accept()
	time.sleep(1)      
sock.close()
os._exit(0)
