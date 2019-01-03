#!/usr/bin/env python3

with open("./input.txt", "r") as f:
    codes = f.readlines()

codes = [code.strip("\r\n") for code in codes]

def fails(code, nextcode):
    common_letter = []
    counter = 0
    for idx, letter in enumerate(code):
        if letter != nextcode[idx]:
            counter = counter + 1
            continue
        common_letter.append(letter)

    return counter, common_letter

for code in codes:
    for nextcode in codes:
        if nextcode == code:
            continue

        times, common_letter = fails(code, nextcode)
        if times == 1:
            print(code)
            print(nextcode)
            print(''.join(common_letter))

