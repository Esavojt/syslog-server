import datetime
import socket
import signal

PORT = 514

server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_sock.bind(("0.0.0.0", PORT))

print("Server started!")

with open("/var/log/syslog-server.log", "w") as file:

    def exit_gracefully(*args):
        file.close()
        print("Closing file and exiting")
        exit(0)
        
    signal.signal(signal.SIGINT, exit_gracefully)
    signal.signal(signal.SIGTERM, exit_gracefully)

    while True:
        buff = str(datetime.datetime.now()) + " " + server_sock.recv(512).decode("utf-8")
        file.write(buff + "\n")
        file.flush()
        print(buff)
