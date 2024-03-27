import socket
import sys
from time import sleep

def main():
	host = ""
	port = 5001
	host_addr = (host, port)

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	while True:
		try:
			sock.bind(host_addr)
			print("Socket bound")
		except:
			print("Bind failed")
			sock.close()
			sys.exit()

		sock.listen(1)
		print(f"Listening on {host}:{port}")

		try:
			while True:
				conn, addr = sock.accept()
				print(f"Connected with {addr[0]}:{addr[1]}")

				handle_client(conn)
		except KeyboardInterrupt:
			print("\nServer shutting down...")
			sock.close()
			sys.exit()


def handle_client(conn):
	while(True):
		print("Listening for message...")
		msg = conn.recv(2048).decode("utf-8")

		print("Message: ", msg)

		on = "ON"
		off = "OFF"
		end = "END"

		if msg == on:
			print("Turned compressor on")
		elif msg == off:
			print("Turned compressor off")
		elif msg == end:
			print("Ending the connection")
			break

	conn.close()

if __name__ == "__main__":
	main()
