import socket
import sys
import RPi.GPIO as gpio

host = ""
port = 5001
host_addr = (host, port)

#print(host)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
	sock.bind(host_addr)
except:
	print("Bind Failed")
	sys.exit()

print("Socket bound")

sock.listen()
print(f"listening on {host}:{port}")

conn,addr = sock.accept()
print(f"Connected with {addr[0]}:{addr[1]}")

msg = conn.recv(4).decode("utf-8")

print(f"[{addr}] {msg}")

conn.close()

