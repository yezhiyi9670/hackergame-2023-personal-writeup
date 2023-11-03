import socket
from time import sleep

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_addr = ("202.38.93.111", 18080)

data = '''GET / HTTP/1.1
Host: example.com

'''

data2 = '''POST / HTTP/1.1
Host: example.com
Content-Length: 10

[redacted]
'''
# tcp_socket.send(data.encode())
tcp_socket.connect(server_addr)
tcp_socket.sendto(data.encode(), server_addr)

msg = tcp_socket.recv(2048)
print(msg.decode())

tcp_socket.close()
