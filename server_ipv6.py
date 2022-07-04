import socket
ip, port = "2804::", 5005
info = socket.getaddrinfo(ip, port, socket.AF_INET6, socket.SOCK_STREAM,0, socket.AI_PASSIVE)
af, socktype, proto, canonname, sa = info[0]
sock = socket.socket(af, socktype, proto)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
sock.bind(sa)
sock.listen()
while True:
    conn, src = sock.accept()
    print(src[0])
    c=conn.recv(1)
    data=str()
    while c:
        data+=c.decode()
        c=conn.recv(1)
    conn.close()
    print(data)
