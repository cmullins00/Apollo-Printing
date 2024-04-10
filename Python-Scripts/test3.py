import socket
import sys
import RPi.GPIO as GPIO
import threading

def handle_client(conn):
    # Function to handle client connections
    try:
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
    finally:
        conn.close()  # Close the connection when the client disconnects

def main():
    host = ""  # Listen on all available interfaces
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

    sock.listen(5)  # Listen for client connections

    try:
        while True:
            conn, addr = sock.accept()
            print(f"Connected with {addr[0]}:{addr[1]}")

            # Create a new thread to handle the client connection
            client_thread = threading.Thread(target=handle_client, args=(conn,))
            client_thread.start()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
