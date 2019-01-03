
with open("./input.txt", "r") as f:
    lines = f.readlines()

line = lines[0].strip("\n")

previous_letter = ""
done = False
while True:
    for idx, letter in enumerate(line):
        if idx == 0:
            continue

        if line[idx-1].isupper() and letter.islower():
            if line[idx-1].upper() == letter.upper():
                line = line[:(idx-1)] + line[(idx+1):]
                break
        elif line[idx-1].islower() and letter.isupper():
            if line[idx-1].lower() == letter.lower():
                line = line[:(idx-1)] + line[(idx+1):]
                break

        if idx == (len(line) - 1):
            done = True

    if done:
        break
print(line)
print(len(line))

#I am an idiot
#dont ever let me program something important


