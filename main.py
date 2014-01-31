import random

def getWords(filename):
    fyle = open(filename)
    string = fyle.read()
    fyle.close()
    words = string.splitlines()
    return words

def startsWithVowel(word):
    if word[0] in 'aeiouAEIOU':
        return True
    else:
        return False

verbs = getWords("buildverbs.txt")
adjectives = getWords("buildadjectives.txt")
nouns = getWords("buildnouns.txt")
buildFillers = getWords("buildfillers.txt")
resultAdjectives = getWords("resultadjective.txt")
resultNouns = getWords("resultnoun.txt")

verb = random.choice(verbs)
adjective = random.choice(adjectives)
adjective2 = adjective
while adjective2 == adjective:
    adjective2 = random.choice(adjectives)
noun = random.choice(nouns)
buildFiller = random.choice(buildFillers)
resultAdjective = random.choice(resultAdjectives)
resultNoun = random.choice(resultNouns)
resultAdjective2 = resultAdjective
while resultAdjective2 == resultAdjective:
    resultAdjective2 = random.choice(resultAdjectives)
resultNoun2 = resultNoun
while resultNoun2 == resultNoun:
    resultNoun2 = random.choice(resultNouns)


if startsWithVowel(adjective):
    filler = " an "
else:
    filler = " a "

print (verb + filler + adjective + " " + adjective2 + " " +
      noun + buildFiller + " " + resultAdjective + " " + resultNoun + " and " +
      resultAdjective2 + " " + resultNoun2)
