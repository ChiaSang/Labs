import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

server = '192.168.6.1'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip, '\n')
request = "GET / HTTP/1.1\nHost :" + server + "\n\n"
s.connect((server, port))
s.send(request.encode())
result = s.recv(4096)
while (len(result) > 0):
    print(result)
    result = s.recv(128)


def pscan(port):
    try:
        s.connect((server, port))
        return True
    except:
        return False


for x in range(1, 1026):
    if pscan(x):
        print('Port:', x, 'is open')
    else:
        print('Port:', x, 'is closed')
