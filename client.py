import socket, sys

host = "www.google.com"
port = 80
payload = 'GET / HTTP/1.0\r\nHost: {}\r\n\r\n'.format(host)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buffer_size = 4096

remote_ip = socket.gethostbyname(host)
s.connect((remote_ip,port))
s.sendall(payload.encode())
s.shutdown(socket.SHUT_WR)
full_data = b""
while True:
	data = s.recv(buffer_size)
	if not data:
		break
	full_data += data
print(full_data)
