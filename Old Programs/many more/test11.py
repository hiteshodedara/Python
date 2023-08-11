import socket
import time

while True:


    def is_connected():
        try:
            # connect to the host -- tells us if the host is actually reachable
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False

    if is_connected():
        print("Internet connection is available")
    else:
        print("Internet connection is not available")

    time.sleep(5)