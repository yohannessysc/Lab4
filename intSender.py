# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, random, sys, math

host = sys.argv[1]
textport = sys.argv[2]
repeat = 10

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

# Repeat specified number of times
for i in range(repeat):
    r = int(random.random()*sys.maxint);
    data = str(r)
    s.sendto(data.encode('utf-8'), server_address)

#s.shutdown(1)