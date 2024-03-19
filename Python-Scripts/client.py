import socket
import sys

s = socket.socket()
host = "127.0.0.1"
port = 5001

s.connect((host, port))
print(host)
s.close
