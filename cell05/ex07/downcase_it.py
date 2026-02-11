#!/usr/bin/env python3

import sys
if len(sys.argv) != 2:
    display = "none"
else:
    display = sys.argv[1].lower()
print(display)
