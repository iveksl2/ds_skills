#! /usr/bin/env python3

data = input("this will come from STDIN: ")
print(f"Now we write it to STDOUT: {data}")
print("Now we generate an error to STDERR:"+  data + 1)
