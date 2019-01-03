
with open("./input.txt", "r") as f:
    lines = f.readlines()

superline = lines[0].strip("\n")

uniq_letters = set([x.lower() for x in superline])
print(uniq_letters)


def calc_behaviour(line):
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
    return len(line)

def main():
    results = []
    for i in uniq_letters:
        result = calc_behaviour(superline.replace(i, ""))
        results.append(result)
        print(i)
        print(result)
    print(sorted(results)[0])

main()
#I am an idiot
#dont ever let me program something important


