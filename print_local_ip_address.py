import socket 

def get_ip():
    return socket.gethostbyname(socket.gethostname())

print(get_ip())