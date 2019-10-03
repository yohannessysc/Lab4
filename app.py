
import socket, sys, time
import json
host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)
i = 0
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x);

while i < 10 :
    print (y["age"])
    #print("Enter data to transmit: ENTER to quit")
    y['age'] = y['age'] + 1
    data = str(y)

    if not len(data):
        break
#    s.sendall(data.encode('utf-8'))
    s.sendto(data.encode('utf-8'), server_address)
    i = i + 1
s.shutdown(1)       