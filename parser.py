########################################################################
# parser.py
#
# parser.py reads in the character names from names_*file*.txt and saves
# all speaking lines from *file*.txt for that character. First the names
# are placed into a dictionary as keys and thier corresponding value is
# a nested empty list. The nested list will hold the character lines in
# the order they appear from the script in *file*.txt

########################################################################
# def readFile(file):
# Read in files

def readFile(file):
    with open(file, 'r') as f:
        text = f.readlines()
    return text

#########################################################################
# def populateCharacterNames(names):
# Remove newline chars from names in names_*file*.txt then save
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
# Prints the dictionary in a readable format


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
# Remove unnecessary whitespace from lines and also remove words that
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
# Parses the script into a dictionary by character name and line


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


########################################################################
# def mostCommonWords(characterDict):
# Create a list that contains as many nested dictionaries as there is
# characters. Each dictionary key will hold a unique word and the values
# are words count tally


def mostCommonWordsByCharacter(wordDict, characterList):
    length = len(characterList)
    wordList = [''] * length

    for i in range(length):
        wordList[i] = {}

# name????????????????????
    i = -1
    for name, words in wordDict.items():
        i = i + 1
        for word in words:
            if word not in wordList[i]:
                wordList[i][word] = 1
            else:
                count = wordList[i][word]
                wordList[i][word] = count + 1

    for i in range(length):
        print(characterList[i])
        for x in wordList[i]:
            y = wordList[i][x]
            print(x, y)

    # print(wordList)

########################################################################
# def stripAllWords(characterDict):
# Iterate through all words spoken by chacters and strip any punctuation
# from it, and save it back in new dictionary.


def stripAllWords(characterDict):
    # append character name as key to new dictionary
    wordDict = {}
    for name, lines in characterDict.items():
        wordDict[name] = []
        for line in lines:

            # make all letters lowercase and remove all punctuation
            line = line.lower()
            for ch in ['.', '?', ':', '&', '!', '-', '"', ',', ';', '\'']:
                if ch in line:
                    line = line.replace(ch, ' ')

            # split into individual words and append to end of list
            split = line.split()
            for word in split:
                word = word.strip()
                wordDict[name].append(word)

    return wordDict

########################################################################
# def printNumWords(wordDict):
# Print out the name and word count per character


def printNumWords(wordDict):
    for name, words in wordDict.items():
        print("\t" + name + ": " + str(len(words)) + " words")
    print()
    return

########################################################################
# def mostCommonWordsOverAll(wordDict):
#


def mostCommonWordsOverAll(wordDict):
    return


########################################################################
########################################################################


def main():

    # replace with files to be read
    lines = readFile('LOTRs1/LOTRsFellowshipOfTheRing.txt')
    names = readFile('LOTRs1/names_LOTRsFellowshipOfTheRing.txt')

    characterList, characterDict = populateCharacterNames(names)
    characterDict = parser(characterList, characterDict, lines)
    # printPretty(characterDict)

    wordDict = stripAllWords(characterDict)
    mostCommonWordsByCharacter(wordDict, characterList)

    print('--------------------------------------------------------------------\n\nSpoken words:\n\n')
    printNumWords(wordDict)
    print('--------------------------------------------------------------------\n\nSomething:\n\n')

    mostCommonWordsOverAll(wordDict)


main()
