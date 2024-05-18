import socket
import sys
import RPi.GPIO as GPIO
import threading

def handle_client(conn):
    while True:
        try:
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
        except ConnectionResetError:
            print("Connection reset by peer. Reconnecting...")
            break  # Exit the loop and attempt reconnection
        except Exception as e:
            print("Error:", e)

    # Attempt reconnection
    while True:
        try:
            print("Attempting to reconnect...")
            conn, addr = sock.accept()
            print(f"Reconnected with {addr[0]}:{addr[1]}")
            handle_client(conn)  # Call handle_client recursively for the new connection
            break  # Exit the loop if the connection is established
        except KeyboardInterrupt:
            print("\nServer shutting down...")
            sys.exit()
        except Exception as e:
            print("Error:", e)

def main():
    # Your existing code for server setup here...

if __name__ == "__main__":
    main()
