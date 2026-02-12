#!/usr/bin/env python3
import sys
from checkmate import checkmate

def main():
    if len(sys.argv) < 2:
        print("Error: No filename provided")
        return
    boardlist = [name for name in sys.argv[1:]]
    for filename in boardlist:
        with open(filename, "r") as f:
            board = f.read()
            checkmate(board)

if __name__ == "__main__":
    main()
