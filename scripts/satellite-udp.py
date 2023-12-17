import socket
import struct
import sys
import random
import time

MCAST_GRP = sys.argv[1]
MCAST_PORT = int(sys.argv[2])
SCIPER = sys.argv[3]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# on this port, listen ONLY to MCAST_GRP
sock.bind((MCAST_GRP, MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

cmd_list = ['w', 'a', 's', 'd']

while True:
  message = cmd_list[random.randint(0, len(cmd_list)-1)]
  sock.sendto(message.encode(), (MCAST_GRP, MCAST_PORT))
  time.sleep(1)

sock.close()