from socket import error as socket_error
import socket

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
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.send(data.encode('utf-8'))
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()
    
sock.close()
os._exit(0)
