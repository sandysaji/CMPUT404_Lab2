import socket
HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",8001))
s.sendall(payload.encode())
s.shutdown(socket.SHUT_WR)
full_data = s.recv(BUFFER_SIZE)
print(full_data)
s.close()
