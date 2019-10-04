# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, json

textport = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)
while True:
    buf, address = s.recvfrom(port)

    if not len(buf):
        break

    print("Received %s bytes from %s : " % (len(buf), address))
    print("Name {} | Age {} | City {}".format(json.loads(buf)["name"],
          json.loads(buf)["age"], json.loads(buf)["city"]))

s.shutdown(1)