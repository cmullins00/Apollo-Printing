import socket
import sys
import RPi.GPIO as GPIO
import threading
from time import sleep

def main():
    host = ""
    port = 5001
    host_addr = (host, port)

    GPIO.setmode(GPIO.BOARD)
    global compressor_pin
    #global stepper_pin
    global pump_direction
    global pump_pin
    global motorStep

    motorStep = False

    # GPIO Pin for the compressor
    compressor_pin = 10

    # GPIO Pins for the stepper motor
    #stepper_pin = 16
    #step_direction = 21
    
    # GPIO Pin for the pump
    pump_pin = 36
    pump_direction = 40

    # Set up the pins on the board
    GPIO.setup(compressor_pin, GPIO.OUT)
    #GPIO.setup(stepper_pin, GPIO.OUT)
    GPIO.setup(pump_direction, GPIO.OUT)
    GPIO.setup(pump_pin, GPIO.OUT)

    # Set direction to clockwise
    GPIO.output(pump_direction, GPIO.HIGH)

    while True:  # Outer loop for server restart
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:  # Try to bind the host address
            sock.bind(host_addr)
            print("Socket bound")
        except Exception as e:
            print("Bind failed:", e)
            sock.close()
            GPIO.cleanup()
            sys.exit()

        sock.listen(1)  # Listen for only one connection

        try:  # Attempt to handle all requests of the client
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
            threading._shutdown()
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

        # Messages to be received
        stepOn = "stepOn"               # Turn on the stepper motor
        stepOff = "stepOff"             # Turn off the stepper motor
        compressorOn = "compressorOn"   # Turn on the compressor
        compressorOff = "compressorOff" # Turn off the compressor
        pumpOn = "pumpOn"               # Turn on the peristaltic pump
        pumpOff = "pumpOff"             # Turn off the peristaltic pump
        end = "END"

        msg = msg.strip()

        if msg == pumpOn:
            print("Turned pump on")
            motorStep = True
            test_thread = threading.Thread(target = step(), args=(pump_pin, 0.1), daemon=True)
            test_thread.start()
        elif msg == pumpOff:
            print("Turned pump off")
            #test_thread.join() 
            motorStep = False
            sleep(0.5)
        elif msg == compressorOn:
            print("Turned compressor on")
            #GPIO.output(forward_pin, GPIO.HIGH)
        elif msg == compressorOff:
            print("Turned compressor off")
            #GPIO.output(forward_pin, GPIO.LOW)
        elif msg == stepOn:
            print("Turned stepper motor on")
            #GPIO.output(pump_pin, GPIO.HIGH)
        elif msg == stepOff:
            print("Turned stepper motor off")
            GPIO.output(pump_pin, GPIO.LOW)
        elif msg == end:
            print("Ending the connection")
            break

def step(pin, delay):
    delay = delay/2
    while motorStep:
        GPIO.output(pin, GPIO.HIGH)
        sleep(delay)

        GPIO.output(pin, GPIO.LOW)
        sleep(delay)
    return

if __name__ == "__main__":
    main()
