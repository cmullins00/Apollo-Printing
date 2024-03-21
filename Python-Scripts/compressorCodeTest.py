import socket
import sys
import RPi.GPIO
from time import sleep

host = ""
port = 5001
host_addr = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

gpio.setmode(gpio.BOARD)
forward_pin = 10
gpio.setup(forward_pin, gpio.OUT)

try:
	sock.bind(host_addr)
except:
	#print(f"Bind failed. Error code: {message[0]} Message {message[1]}")
	print("Bind failed")
	sys.exit()

print("socket bound")

sock.listen(9)
print(f"Listening on {host}:{port}")

conn, addr = sock.accept()
print(f"Connected with {addr[0]}:{addr[1]}")

msg = conn.recv(4).decode("utf-8")

if msg == ":)":
	gpio.output(forward_pin, gpio.HIGH)
	sleep(5.0)
	gpio.output(forward_pin, gpio.LOW)

print(f"[{addr}] {msg}")

gpio.cleanup()
