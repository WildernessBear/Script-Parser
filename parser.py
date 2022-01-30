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

    # remove newline chars from names in nameFile then save characters
    # in list to check while iterating through script and also as an
    # empty nested ditionary
    name = name.rstrip()
    characterList.append(name)
    characterDict[name] = []

with open(file, 'r') as f:
    lines = f.readlines()

currName = ''
quote = ''
uppercase = []
inDialogueBlock = False
endOfDialogueBlock = False

for line in lines:

    # character name was found. Strip additional whitespace from
    # following line and append to quote text. If \n or empty list
    # then dialogue is over
    if inDialogueBlock:

        if line == '\n':
            inDialogueBlock = False
            endOfDialogueBlock = True
        else:
            line = line.strip()
            quote = quote + " " + line

    # charcter dialouge ended. Check there is text inside quaote
    # and then append it to the corresponding character in the
    # dictionary at next index in list
    if endOfDialogueBlock:

        if len(quote) != 0:
            characterDict[currName].append(quote)

        quote = ''
        inDialogueBlock = False
        endOfDialogueBlock = False
        currName = ''

    # search for main characters in script
    for searchName in characterList:
        if searchName in line:

            # check that this starts a dialogue and is not part of a scene
            # description. Name will be followed by a newline, (V.O.) voice
            # over, (CONT'D) continuation or (O.S) off screen line
            if (re.search("   " + searchName + "\n", line)) or ("(O.S)" or "(V.O.)" or "(CONT'D)" in line):
                inDialogueBlock = True
                currName = searchName
            else:
                inDialogueBlock = False

for key, value in characterDict.items():
    print(key)
    for a in value:
        print(a)
