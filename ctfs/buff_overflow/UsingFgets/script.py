#!/bin/env python
import sys

buffer = ("A" * 30)

# buffer = b"\x00"

sys.stdout.buffer.write(buffer.encode('utf-8'))
# sys.stdout.buffer.write(buffer)