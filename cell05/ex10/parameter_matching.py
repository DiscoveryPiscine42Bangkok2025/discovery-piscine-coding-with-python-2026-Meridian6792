#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 2:
    print("none")
else:
    pattern = sys.argv[1]
    given = input("What was the parameter? ")
    if re.fullmatch(pattern, given):
        print("Good job!")
    else:
        print("Nope, sorry")
