import socket
import sys
import RPi.GPIO as GPIO
from time import sleep

host = ""
port = 5001
host_addr = (host, port)

GPIO.setmode(GPIO.BOARD)
forward_pin = 10
GPIO.setup(forward_pin, GPIO.OUT)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.settimeout(None)
#sock.setblocking(False)

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
run = True
on = "ON"
off = "OFF"
end = "END"
while(run == True):
	try:
		print("Listening for message")
		msg = conn.recv(1024).decode("utf-8")
	except KeyboardInterrupt:
		break

	msg = msg.strip()
	print("Message:", msg)

	if msg == on:
		GPIO.output(forward_pin, GPIO.HIGH)
		print("Turned compressor on")
	elif msg == off:
		GPIO.output(forward_pin, GPIO.LOW)
		print("Turned compressor off")
	elif msg == end:
		print("ending the program")
		run = False

conn.close()
gpio.cleanup()
