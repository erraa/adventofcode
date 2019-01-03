#!/usr/bin/env python3

with open("./input.txt", "r") as f:
    codes = f.readlines()

twos = 0
threes = 0

for code in codes:
    code = code.strip("\r\n")
    two = False
    three = False
    for letter in code:
        if code.count(letter) == 2:
            two = True
        elif code.count(letter) == 3:
            three = True
    if two:
        twos = twos + 1
    if three:
        threes = threes + 1

print(twos)
print(threes)
print(threes * twos)


