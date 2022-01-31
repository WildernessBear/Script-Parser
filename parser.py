########################################################################
# parser.py
#
# parser.py reads in the character names from names_*file*.txt and saves
# all speaking lines from *file*.txt for that character. First the names
# are placed into a dictionary as keys and thier corresponding value is
# a nested empty list. The nested list will hold the character lines in
# the order they appear from the script in *file*.txt
import re

########################################################################
# def readFile(file):
# read in files


def readFile(file):
    with open(file, 'r') as f:
        text = f.readlines()
    return text


#########################################################################
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

########################################################################
# def printPretty(characterDict):
# prints the dictionary in a readable format


def printPretty(characterDict):
    for name, lines in characterDict.items():
        count = 1
        print("\n\n" + name)
        for line in lines:
            print(str(count) + " " + line)
            count = count + 1
    return


########################################################################
# def scrubLine(line):
# remove unnecessary whitespace from lines and also remove words that
# are surrounded by parenthesis. These are actions, not dialogue
def scrubLine(line):

    # no parenthesis
    if line.find("(") == -1 and line.find(")") == -1:
        fixedLine = ''
        line = line.strip()
        splitLine = line.split()

        for num in range(len(splitLine)):
            if num == 0:
                fixedLine = splitLine[0]
            else:
                fixedLine = fixedLine + " " + splitLine[num]

        return fixedLine

    # remove words in parenthesis by returning an empty string
    else:
        return ''

########################################################################
# def parser(characterList, characterDict, lines):
# parses the script into a dictionary by character name and line


def parser(characterList, characterDict, lines):
    currName = ''
    quote = ''
    inDialogueBlock = False
    endOfDialogueBlock = False

    for line in lines:

        # character name was found. Scrub additional whitespace from
        # following line and action words in parenthesis then append
        # to quote text. If newline then the dialogue is over
        if inDialogueBlock:

            if line.isspace():
                inDialogueBlock = False
                endOfDialogueBlock = True
            else:
                line = scrubLine(line)

                if len(quote) > 0:
                    quote = quote + " " + line
                else:
                    quote = line

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

    return characterDict


def main():

    # replace with files to be read
    lines = readFile('LOTRsFellowshipOfTheRing.txt')
    names = readFile('names_LOTRsFellowshipOfTheRing.txt')

    characterList, characterDict = populateCharacterNames(names)

    characterDict = parser(characterList, characterDict, lines)

    printPretty(characterDict)


main()
