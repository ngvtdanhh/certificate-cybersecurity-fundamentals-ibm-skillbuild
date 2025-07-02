import socket
common = {21: 'FTP', 22: 'SSH', 80: 'HTTP', 443: 'HTTPS', 3306: 'MySQL'}

def scan(ip):
    return [f"{p} ({s}) open" for p, s in common.items()
            if not socket.socket().connect_ex((ip, p))]

# Example
# print(scan("127.0.0.1"))
