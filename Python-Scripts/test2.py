import socket
import sys
import RPi.GPIO as GPIO

def main():
    host = ""
    port = 5001
    host_addr = (host, port)

    GPIO.setmode(GPIO.BOARD)
    global forward_pin
    forward_pin = 10
    GPIO.setup(forward_pin, GPIO.OUT)

    while True:  # Outer loop for server restart
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            sock.bind(host_addr)
            print("Socket bound")
        except Exception as e:
            print("Bind failed:", e)
            sock.close()
            GPIO.cleanup()
            sys.exit()

        sock.listen(1)  # Listen for only one connection

        try:
            conn, addr = sock.accept()
            print(f"Connected with {addr[0]}:{addr[1]}")

            handle_client(conn)
            conn.close()
        except KeyboardInterrupt:
            print("\nServer shutting down...")
            sock.close()
            sys.exit()
        except Exception as e:
            print("Error: ", e)
            sock.close()
            sys.exit()
        finally:
            sock.close()  # Close the socket after the client disconnects

def handle_client(conn):
    while True:
        print("Listening for message...")
        msg = conn.recv(2048).decode("utf-8")

        if not msg:
            # Connection closed by client
            print("Client closed connection")
            break

        print("Message: ", msg)

        on = "ON"
        off = "OFF"
        end = "END"

        msg = msg.strip()

        if msg == on:
            print("Turned compressor on")
            GPIO.output(forward_pin, GPIO.HIGH)
        elif msg == off:
            print("Turned compressor off")
            GPIO.output(forward_pin, GPIO.LOW)
        elif msg == end:
            print("Ending the connection")
            break

if __name__ == "__main__":
    main()
