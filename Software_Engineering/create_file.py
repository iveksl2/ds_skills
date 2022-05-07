#! /usr/bin/env python3
import os
import sys

filename=sys.argv[1]

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("new file created\n")
else:
    print(f"error, the file {filename} already exists!")
    sys.exit(1)
