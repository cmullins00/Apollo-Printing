import socket
import sys
import RPi.GPIO as GPIO

def main():
    host = "192.168.0.100"  # Set the server's IP address here
    port = 5001
    host_addr = (host, port)

    GPIO.setmode(GPIO.BOARD)
    global forward_pin
    forward_pin = 10
    GPIO.setup(forward_pin, GPIO.OUT)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        sock.bind(host_addr)
        print("Socket bound to", host_addr)
    except Exception as e:
        print("Bind failed:", e)
        GPIO.cleanup()
        sys.exit()

    sock.listen(1)  # Listen for only one connection

    while True:  # Outer loop for server restart
        conn, addr = sock.accept()
        print(f"Connected with {addr[0]}:{addr[1]}")

        try:
            handle_client(conn)
        except KeyboardInterrupt:
            print("\nServer shutting down...")
            conn.close()
            sock.close()
            sys.exit()
        except Exception as e:
            print("Error: ", e)
            conn.close()

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

    conn.close()  # Close the connection when the client disconnects

if __name__ == "__main__":
    main()
