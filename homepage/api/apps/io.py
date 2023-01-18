"""Utilities for page interfaces."""

import socket

def send_msg(msg: str, server_host: str, server_port: int):
    """Send raw byte msg to port."""
    host = "localhost"
    port = 0
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listen_sock:
        # bind worker socket to its server
        listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        listen_sock.bind((host, port))
        port = listen_sock.getsockname()[1]

        listen_sock.listen()
        # send msg
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as send_sock:

            # persistently attempt to establish connection with tag server
            while True:
                try:
                    send_sock.connect((server_host, server_port))
                    break
                except:
                    continue

            # register with manager
            send_sock.sendall(msg.encode('utf-8'),)
    