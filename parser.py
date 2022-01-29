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

    # remove newline chars from names in nameFile then
    # save characters in list to check while iterating
    # through script and also as an empty nested ditionary
    name = name.rstrip()
    characterList.append(name)
    characterDict[name] = []

with open(file, 'r') as f:
    lines = f.readlines()


quote = []
uppercase = []
inDialogueBlock = False
endOfDialogueBlock = False
foundCharacterName = False

for line in lines:

    input(" ")
    print(line)

    # character name was found, add line to quote text
    if inDialogueBlock:

        print("---------------------")
        print("Block started:")

        quote.append(line)
        inDialogueBlock = False
        endOfDialogueBlock = True

    # charcter dialouge ended, append quote to corresponding
    # character in the dictionary at next index in list
    if endOfDialogueBlock:

        print("Block Ended")
        print("Quote is:")
        print(quote)
        print("---------------------")

        characterDict[uppercase[i]].append(quote)
        quote = []
        inDialogueBlock = False
        endOfDialogueBlock = False

    # find uppercase words in script then check
    # if uppercase word is also a main character
    i = 0
    foundCharacterName = False
    uppercase = re.findall(r"(\b[A-Z][A-Z]+(?:\s+[A-Z]+)*\b)", line)
    index = len(uppercase)

    name = ""
    if index > 0:
        while i < index:

            print(uppercase[i] + " i = " + str(i) + " index = " + str(index))

            if uppercase[i] in characterList:

                name = uppercase[i]
                print("Found name: " + name)
                foundCharacterName = True
                break
            i = i+1

        if foundCharacterName == True:

            print(name)

            # check that this starts a speaking section
            # and is not part of a scene description
            if re.search("   " + str(uppercase[i]) + "\n", line):
                block = True
            else:
                block = False

            # if it is a voice over (V.O.) then
            # character name will not be followed by newline
            if re.findall(r"\B\(V\.O\.\)", line):
                voiceOver = True
            else:
                voiceOver = False

            # if it is continuation (CONT'D) then
            # character name will not be followed by newline
            if re.findall(r"\(CONT\'D\)\B", line):
                continuation = True
            else:
                continuation = False

            # if it is a line off screen (O.S) then
            # character name will not be followed by newline
            if re.findall(r"\(O\.S\.\)\B", line):
                offScreen = True
            else:
                offScreen = False

            if block or voiceOver or continuation or offScreen:
                inDialogueBlock = True
            else:
                inDialogueBlock = False

for x, y in characterDict.items():
    print(x, y)
