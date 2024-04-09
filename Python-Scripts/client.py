import socket
from time import sleep

def main():
    host = "192.168.0.100"
    port = 5001

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((host, port))
        print("Connected to server.")

        while True:
            message = "ON"
            client.sendall(message.encode())
            sleep(1)

            message = "OFF"
            client.sendall(message.encode())
            sleep(1)


    except KeyboardInterrupt:
        print("Closing the connection")
    except Exception as e:
        print("Error:", e)
    finally:
        client.close()

if __name__ == "__main__":
    main()
