# findNames.py
#
# findNames.py reads the script *file* and parses out all the speaking
# character roles by finding any words that are in all uppercases. The
# names are put into a dictionary, which I printed out and saved to
# output_findNames_*file*.txt. I manually reviewed the list and saved
# all character names to be used in parser.py in names_*file*.txt.
##########################################################################

import re

# update to location of file script to be used
file = 'LOTRs3\LOTRsTheReturnOfTheKing.txt'

with open(file, 'r', encoding='UTF8') as f:
    lines = f.readlines()

characterDict = {}

for line in lines:

    # find character names
    uppercase = re.findall(
        r"(\b[A-Z][A-Z]+(?:\s+[A-Z]+)*\b)", line)

    # totally up how many speaking blocks they have
    if len(uppercase) > 0:
        for name in uppercase:
            if name not in characterDict:
                characterDict[name] = 1
            else:
                i = characterDict[name]
                characterDict.update({name: i+1})

# only show characters with at least 5 lines
for x, y in characterDict.items():
    if y > 5:
        print(y, x)
