import socket
from time import sleep

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_addr = ("202.38.93.111", 18081)
tcp_socket.connect(server_addr)

data = '''GET / HTTP/1.1
Host: example.com

'''

data1 = '''P'''
data2 = '''OST / HTTP/1.1
Host: example.com
Content-Length: 14

239:[redacted]
'''

# tcp_socket.send(data.encode())
tcp_socket.send(data1.encode())
sleep(1)
tcp_socket.send(data2.encode())
tcp_socket.send(''.encode())

msg = tcp_socket.recv(2048)
print(msg.decode())

tcp_socket.close()
