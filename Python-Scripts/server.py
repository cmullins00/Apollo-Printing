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

    # Create the global pin variables
    global compressor_pin
    global stepper_pin
    global step_direction
    global pump_direction
    global pump_pin

    # GPIO Pin for the compressor
    compressor_pin = 10

    # GPIO Pins for the stepper motor
    stepper_pin = 16
    step_direction = 21
    
    # GPIO Pins for the pump
    pump_pin = 36
    pump_direction = 40


    # Flag variables for stopping the threads
    global pumpStart
    global stepperStart
    pumpStart = False
    stepperStart = False

    # Set up the pins on the board
    GPIO.setup(compressor_pin, GPIO.OUT)
    GPIO.setup(stepper_pin, GPIO.OUT)
    GPIO.setup(step_direction, GPIO.OUT)
    GPIO.setup(pump_direction, GPIO.OUT)
    GPIO.setup(pump_pin, GPIO.OUT)

    GPIO.output(pump_pin, GPIO.LOW)
    GPIO.output(stepper_pin, GPIO.LOW)


    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:  # Try to bind the host address
        sock.bind(host_addr)
        print("Socket bound")
    except Exception as e:
        print("Bind failed:", e)
        GPIO.cleanup()
        conn.close()
        sock.close()
        sys.exit()

    sock.listen(1)  # Listen for only one connection
    
    try:  # Attempt to handle all requests of the client
        conn, addr = sock.accept()
        print(f"Connected with {addr[0]}:{addr[1]}")
        handle_client(conn)
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except Exception as e:
        print("Error: ", e)
    finally:
        GPIO.cleanup()
        conn.close()
        sock.close()  # Close the socket after the client disconnects
        sys.exit()

def handle_client(conn):
    global pumpStart
    global stepperStart

    while True:
        print("Listening for message...")
        msg = conn.recv(2048).decode("utf-8")   # Listen for incoming instructions from the robot controller

        if not msg:
            # Connection closed by client
            print("Client closed connection")
            break

        print("Message: ", msg)

        # Messages to be received
        stepOn = "stepOn"               # Turn on the stepper motor
        stepOff = "stepOff"             # Turn off the stepper motor
        stepReverse = "stepReverse"
        compressorOn = "compressorOn"   # Turn on the compressor
        compressorOff = "compressorOff" # Turn off the compressor
        pumpOn = "pumpOn"               # Turn on the peristaltic pump
        pumpOff = "pumpOff"             # Turn off the peristaltic pump
        end = "END"                     # End the socket connection

        msg = msg.strip()

        # Initialize threads to run the pump and stepper while still being able to listen to new messages from the controller
        pump_thread = threading.Thread(target = pumpStep, args=(pump_pin, 0.03))
        stepper_thread = threading.Thread(target = stepperStep, args=(stepper_pin, 0.05))

        if msg == pumpOn:
            print("Turned pump on")
            pumpStart = True
            pump_thread.start()
        elif msg == pumpOff:
            print("Turned pump off")
            pumpStart = False
            #if pump_thread is not None:
                #pump_thread.join()
            GPIO.output(pump_pin, GPIO.LOW)
            sleep(0.5)
        elif msg == compressorOn:
            print("Turned compressor on")
            GPIO.output(compressor_pin, GPIO.HIGH)
        elif msg == compressorOff:
            print("Turned compressor off")
            GPIO.output(compressor_pin, GPIO.LOW)
        elif msg == stepOn:
            print("Turned stepper motor on")
            stepperStep(stepper_pin, 0.02)
        elif msg == stepReverse:
            print("Reversed the direction of the stepper")
            stepperReverse(stepper_pin, 0.02)
        elif msg == stepOff:
            print("Turned stepper motor off")
            stepperStart = False
            #if stepper_thread is not None:
                #stepper_thread.join()
            GPIO.output(stepper_pin, GPIO.LOW)
            sleep(0.5)
        elif msg == end:
            print("Ending the connection")
            break

# Function to run the pump continuously until stopped
def pumpStep(pin, delay):
    global pumpStart
    global pump_direction
    GPIO.output(pin, pump_direction)

    delay = delay/2
    while pumpStart:
        GPIO.output(pin, GPIO.HIGH)
        sleep(delay)

        GPIO.output(pin, GPIO.LOW)
        sleep(delay)
    return

def stepperStep(pin, delay):
    global step_direction
    delay = delay/2
    steps = 150
    GPIO.output(step_direction, GPIO.HIGH)
    GPIO.output(pin, step_direction)
    
    for x in range(steps):
        GPIO.output(pin, GPIO.HIGH)
        sleep(delay)

        GPIO.output(pin, GPIO.LOW)
        sleep(delay)
    

'''
# Function to run the stepper motor continuously until stopped
def stepperStep(pin, delay):
    global stepperStart
    global step_direction
    GPIO.output(pin, step_direction)

    delay = delay/2
    while stepperStart:
        GPIO.output(pin, GPIO.HIGH)
        sleep(delay)

        GPIO.output(pin, GPIO.LOW)
        sleep(delay)
    return
'''

def stepperReverse(pin, delay):
    global step_direction
    delay = delay/2
    steps = 100
    GPIO.output(step_direction, GPIO.LOW)
    GPIO.output(pin, step_direction)
    
    for x in range(steps):
        GPIO.output(pin, GPIO.HIGH)
        sleep(delay)

        GPIO.output(pin, GPIO.LOW)
        sleep(delay)
    
    GPIO.output(step_direction, GPIO.LOW)
    
if __name__ == "__main__":
    main()
