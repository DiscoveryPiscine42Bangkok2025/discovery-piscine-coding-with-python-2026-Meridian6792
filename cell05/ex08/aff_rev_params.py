#!/usr/bin/env python3

import sys

A = [arg for arg in sys.argv[1:] if arg]
for arg in reversed(A):
    print(arg)
