# parser.py
#
# parser.py reads in the character names from names_*file*.txt and saves
# all speaking lines from *file*.txt for that character. First the names
# are placed into a dictionary as keys and thier corresponding value is
# a nested empty list. The nested list will hold the character lines in
# the order they appear from the script in *file*.txt
##########################################################################
import re

# replace with files to be read
file = 'LOTRsFellowshipOfTheRing.txt'
nameFile = 'names_LOTRsFellowshipOfTheRing.txt'

with open(nameFile, 'r') as f:
    names = f.readlines()

characterList = []
characterDict = {}
for name in names:

    # remove newline chars from names in nameFile
    name = name.rstrip()

    # save characters in list to check while iterating through
    # script and also as an empty nested ditionary
    characterList.append(name)
    characterDict[name] = []

with open(file, 'r') as f:
    lines = f.readlines()

quote = []
uppercase = []
appendLine = False
i = 0

for line in lines:

    if appendLine:
        quote.append(line)
        characterDict[uppercase[i]].append(quote)
        # print(quote)
        appendLine = False
        quote = []

    # find uppercase words in script
    uppercase = re.findall(r"(\b[A-Z][A-Z]+(?:\s+[A-Z]+)*\b)", line)

    # see if word is a main character
    i = 0
    index = len(uppercase)
    if index > 0:
        while i < index:
            if uppercase[i] in characterList:
                appendLine = True
                break
            i = i+1


for x, y in characterDict.items():
    print(x, y)


# if it is a voice over (V.O.) then
# character name will not be followed by newline
#voiceOver = re.findall(r"\B\(V\.O\.\)", line)

# if it is continuation (CONT'D) then
# character name will not be followed by newline
#continuation = re.findall(r"\(CONT\'D\)\B", line)

# if it is a line off screen (O.S) then
# character name will not be followed by newline
#offScreen = re.findall(r"\(O\.S\.\)\B", line)

# if voiceOver or continuation or offScreen:
#     print(line)
