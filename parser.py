# parser.py
#
# parser.py reads in the character names from names_*file*.txt and saves
# all speaking lines from *file*.txt for that character. First the names
# are placed into a dictionary as keys and thier corresponding value is
# a nested empty dictionary. The nested dictionary will hold numerically
# ordered keys with values that are the characters lines from *file*.txt
##########################################################################

# replace with files to be read
file = 'LOTRsFellowshipOfTheRing.txt'
nameFile = 'names_LOTRsFellowshipOfTheRing.txt'

with open(nameFile, 'r') as f:
    names = f.readlines()

characterDict = {}

# remove newline chars from nameFile and
# save name as an empty nested ditionary
for name in names:
    name = name.rstrip()
    characterDict[name] = {}

print(characterDict)

# need to make sure there is a new line after names & check on voiceovers
