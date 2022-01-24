# findNames.py
#
# This file reads the script and finds all the speaking
# character roles by finding all words that are in all
# uppercases. The names are put into a list to be used
# in the parser.
############################################

import re

# with open('LOTRs.txt', 'r') as f:
with open('LOTRsFellowshipOfTheRing.txt', 'r') as f:
    lines = f.readlines()


for line in lines:
    # matches = re.findall(
    #     r"(\b(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b(?:\s+(?:[A-Z]+[a-z]?[A-Z]*|[A-Z]*[a-z]?[A-Z]+)\b)*)", line)
    #     r"(\b[A-Z][A-Z]+\b)", line)
    #     r"(\b[A-Z]+(?:\s+[A-Z]+)*\b)", line)

    matches = re.findall(
        r"(\b[A-Z][A-Z]+(?:\s+[A-Z]+)*\b)", line)

    if len(matches) > 0:
        print(matches)
