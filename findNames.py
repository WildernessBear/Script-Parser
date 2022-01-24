import re

print('\n. . . parsing\n')

with open('LOTRs.txt', 'r') as f:
    lines = f.readlines()


for line in lines:
    matches = re.findall(
        r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)", line)
    print(matches)

    # x = re.search(r"\bS\w+", line)
    # print(x.group())
