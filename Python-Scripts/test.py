import socket
import sys
from time import sleep

def main():
	host = ""
	port = 5001
	host_addr = (host, port)

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	try:
		sock.bind(host_addr)
		print("Socket bound")
	except:
		print("Bind failed, ", socket.errori)
		sock.close()
		sys.exit()

	while True:
		sock.listen(1)
		print(f"Listening on {host}:{port}")

		try:
			conn, addr = sock.accept()
			print(f"Connected with {addr[0]}:{addr[1]}")

			handle_client(conn)
			conn.close()
		except KeyboardInterrupt:
			print("\nServer shutting down...")
			conn.close()
			sock.close()
			sys.exit()
		except socket.error as msg:
			print("Socket error: %s" % msg)


def handle_client(conn):
	while(True):
		print("Listening for message...")
		msg = conn.recv(4096).decode("utf-8")

		if not msg:
			print("Connection closed by client")
			break

		print("Message: ", msg)

		on = "ON"
		off = "OFF"
		end = "END"

		msg = msg.strip()

		if msg == on:
			print("Turned compressor on")
		elif msg == off:
			print("Turned compressor off")
		elif msg == end:
			print("Ending the connection")
			return

if __name__ == "__main__":
	main()
