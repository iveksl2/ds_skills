#!/usr/bin/env python3
# Reading and writing files - https://docs.python.org/3/library/functions.html#open

file = open('random_file.txt')

print(file.readline())

print(file.read()) # starts at current line and reads all the way through

file.close()

# # automatically closes a file
#with open('random_file.txt') as file:
#    print(file.readline())

with open('random_file.txt') as file:
    print(file.readline())
    for line in file:
            print(line.strip().upper())

# read into list
file = open("random_file.txt")
lines = file.readlines() #This can be dangerous if a file is very large
file.close()

lines.sort()
print(lines)

## ----- writing ---
# https://docs.python.org/3/library/functions.html#open

with open("novel.txt", "w") as file:
    file.write("this is novel text")
    
# working with the OS.  
import os #platform independent. Note that paths can be different

os.remove('file.txt')
os.rename('novel2.txt', 'finished_masterpiece.txt')

os.path.exists("finished_masterpiece.txt")
os.path.exists('non_existant_file.txt')
os.path.getsize('novel.txt') # size in bytes
os.path.getmtime('novel.txt') # file was last modified. Timestamp since jan 1st, 1970

import datetime
timestamp = os.path.getmtime('novel.txt')
datetime.datetime.fromtimestamp(timestamp)

os.path.abspath("novel.txt")

os.getcwd()

os.mkdir('new_dir')
os.chdir("new_dir")
os.getcwd()
os.mkdir('newer_dir')
os.rmdir('newer_dir')
os.listdir('.')

dir = '.'
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname): # Allows us to be independent of the OS
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")

# https://docs.python.org/3/library/os.html
# https://docs.python.org/3/library/os.path.html
# https://en.wikipedia.org/wiki/Unix_time

# ----------- csv files ----------------
import csv
f = open('csv_file.txt')
csv_f = csv.reader(f)

for row in csv_f:
    name, phone, role = row #unpacking - Can usae indexes, but readibility becomes harder
    print(f"Name: {name}, Phone: {phone}, Role: {role}") 

csv_f.close()

# generating CSV files
hosts =  [["workstation.local", "192.168.25.26"], ["webservr.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
    
with open('software.csv' as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(row["name"], row["users"]) # order doesn't matter

# users = [{'name': 'sol Mansi', 'username': solm'}, {'name', Lio Nelson', ..
with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, filednames=keys)
    writer.writeheader()
    writer.writerows(users)

# csv cheatsheets
# https://docs.python.org/3/library/csv.html
# https://realpython.com/python-csv/

