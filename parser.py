# parser.py
#
# parser.py reads in the character names from names_*file*.txt and saves
# all speaking lines from *file*.txt for that character. First the names
# are placed into a dictionary as keys and thier corresponding value is
# a nested empty list. The nested list will hold the character lines in
# the order they appear from the script in *file*.txt
##########################################################################
import re

# def readFile(file):
# read in files


def readFile(file):
    with open(file, 'r') as f:
        text = f.readlines()
    return text


# def populateCharacterNames(names):
# remove newline chars from names in names_*file*.txt then save
# characters in list to check while iterating through script and
# also as an empty nested ditionary for saving all dialouge


def populateCharacterNames(names):
    characterList = []
    characterDict = {}
    for name in names:
        name = name.rstrip()
        characterList.append(name)
        characterDict[name] = []
    return characterList, characterDict


def printPretty(characterDict):
    for key, value in characterDict.items():
        e = 1
        print(key)
        for a in value:
            print(str(e) + " " + a)
            e = e + 1
    return


def main():

    # replace with files to be read
    lines = readFile('LOTRsFellowshipOfTheRing.txt')
    names = readFile('names_LOTRsFellowshipOfTheRing.txt')

    characterList, characterDict = populateCharacterNames(names)

    currName = ''
    quote = ''
    inDialogueBlock = False
    endOfDialogueBlock = False

    for line in lines:

        # character name was found. Strip additional whitespace from
        # following line and append to quote text. If \n or empty list
        # then dialogue is over
        if inDialogueBlock:

            if line.isspace():
                inDialogueBlock = False
                endOfDialogueBlock = True
            else:
                line = line.strip()
                quote = quote + " " + line

        # charcter dialouge ended. Check there is text inside quote
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

                if line.isupper():
                    inDialogueBlock = True
                    currName = searchName
                else:
                    inDialogueBlock = False

    printPretty(characterDict)


main()
