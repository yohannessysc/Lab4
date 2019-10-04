# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, json

host = sys.argv[1]
textport = sys.argv[2]
repeat = int(sys.argv[3])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

x = { "name":"John", "age":30, "city":"New York"}
print("Initial: ", json.dumps(x))

for i in range(repeat):
    data = json.dumps(x)
    s.sendto(data.encode('utf-8'), server_address)
    x["age"] = x["age"] + 1

#s.shutdown(1)