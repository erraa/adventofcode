from multiprocessing import Pool

with open("./input.txt", "r") as f:
    lines = f.readlines()

superline = lines[0].strip("\n")

uniq_letters = set([x.lower() for x in superline])
print(uniq_letters)


def calc_behaviour(line_uniq):
    line, uniq = line_uniq[0], line_uniq[1]

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
    return (len(line), uniq)

def main():
    results = []
    pool = Pool(processes=4)
    list_of_line = [(superline.replace(uniq, "").replace(uniq.upper(), ""), uniq) for uniq in uniq_letters]
    print(len(list_of_line))
    for i in pool.imap_unordered(calc_behaviour, list_of_line):
        print(i)

main()
#I am an idiot
#dont ever let me program something important


