import random

def getRandomWord():
    words = ['pizza', 'cheese', 'apples']
    word = words[random.randint(0, len(words)-1)]
    return word

def showWord(word):
    for character in word:
        print(character, ' ', end='')
    print('')

def getGuess():
    print('Enter a letter: ')
    return input()

def printStrikes(numberOfStrikes):
    for i in range (0, numberOfStrikes):
        print(' X ', end='')
    print('')

def processLetter(letter, secretWord, blankedWord):
    result = False

    for i in range(0, len(secretWord)):
        if secretWord[i] == letter:
            result = True
            blankedWord[i] = letter
    return result
                 

def playWordGame():
    strikes = 0
    maxStrikes = 3
    playing = True

    word = getRandomWord()
    blankedWord = list('_' * len(word))

    while playing:
        showWord(blankedWord)
        letter = getGuess()
        found = processLetter(letter, word, blankedWord)

        if not found:    
            strikes += 1
            printStrikes(strikes)

        if strikes >= maxStrikes:
            playing = False

        if not '_' in blankedWord:
            playing = False

    if strikes >= maxStrikes:
        print('Loser')
    else:
        print('Winner!!!!')
    



print('Game Started')
playWordGame()
print('Game Over')
