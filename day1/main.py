#!/usr/bin/env python3

def anydup(thelist):
  seen = set()
  for x in thelist:
    if x in seen: return True
    seen.add(x)
  return False

with open("./input.txt", 'r') as f:
    lines = f.readlines()

    freq = 0
    previous_values = [freq]
    counter = 0
    break_loop = True
    while break_loop:
        for line in lines:
            counter = counter + 1
            freq = freq + int(line)
            if freq in previous_values:
                print("First repeated value is {}".format(str(freq)))
                break_loop = False
                break
            previous_values.append(freq)
    print(counter)
    print(previous_values)
    print(anydup(previous_values))

