#!/usr/bin/python

import sys

def get_new_row(row):
    new_row = ""
    for i in range(0, len(row)):
        
        prev_row = ""
        for x in range(i-1, i+2):
            if x < 0 or x > len(row)-1:
                prev_row += "."
            else:
                prev_row += row[x]
               
        if prev_row in ["^^.", ".^^", "^..", "..^"]:
            new_row += "^"
        else:
            new_row += "."

    return new_row        

first_row = sys.argv[1]
num_rows = int(sys.argv[2])
my_map = [first_row]

while len(my_map) < num_rows:
    my_map.append(get_new_row(my_map[-1]))

all_rows = ""
for row in my_map:
    print row
    all_rows += row

print len(all_rows.replace("^", ""))    
