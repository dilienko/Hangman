from random import choice
from addition import drawHangman
from addition import showRules
import os
import re

#read words from file 
file = open('dictionary.txt')
allWords = file.read().split('\n')
file.close()
#game score initialization
gamePoints = 0

while True:
    randomWord = choice(allWords)
    allLetter = ['a','b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j', 'k' ,'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t','u','v','w','x','y','z', 'help', 'quit']
    previousGuessed = False
    avaliableLetters = allLetter
    tries = 10 
    hiddenWord = re.sub('[A-Za-z]', '_', randomWord)
    isStartOfGame = True

    while tries > 0:
        # clear console and show all necessary information
        os.system('cls||clear')
        print("HANGMAN\n")
        if isStartOfGame:
            showRules()
        isStartOfGame = False
        print ('You have ' + str(round(gamePoints))+ ' points')
        print('You have ' + str(tries) + ' tries')
        drawHangman(tries)
        print(hiddenWord)
        # ask enter a letter. If it`s missing in avaliable list, start new loop interation 
        userLetter = input("Guess a letter " + str(avaliableLetters) + ": ").lower()
        if avaliableLetters.count(userLetter) == 0:
            continue
        
        # open random letter in hidden word, if user enter 'help'
        if userLetter == 'help':
            previousGuessed = False
            while randomWord.find(userLetter) == -1:
                userLetter = choice(avaliableLetters)
            gamePoints = (gamePoints / 2) - 10
            avaliableLetters.remove('help')

        # stop game, if user want it (enter 'quit')
        if userLetter == 'quit':
            break

        # finds indexes of letter which user
        # input in hidden word
        startPoint = 0
        indexes = []
        while True:
            indexOfLetter = randomWord.find(userLetter, startPoint)
            if indexOfLetter == -1:
                break
            indexes.append(indexOfLetter)
            startPoint = indexOfLetter + 1

        if len(indexes) > 0:
            # add points for a guessed letter 
            if previousGuessed:
                gamePoints = gamePoints + 20
            else:
                gamePoints = gamePoints + 10
            previousGuessed = True 
            ## replace hidden symbols with letter
            for index in indexes:
                hiddenWordCopied = hiddenWord
                hiddenWord = ''
                hiddenWord =  hiddenWordCopied[:index] + userLetter + hiddenWordCopied[index+1:]
        else:
            previousGuessed = False
            tries = tries - 1   
        
        # removing current letter from avaliable letters list 
        for letter in allLetter:
            if userLetter == letter:
                avaliableLetters.remove(userLetter)

        # check if there are hidden symbols 
        # if they aren't - user win
        if hiddenWord.find('_') == -1:
            os.system('cls||clear')
            print ('You have ' + str(round(gamePoints))+ ' points')
            drawHangman(tries)
            print("You won!")
            print("The answer was " + randomWord + ".")
            break

    # Output infrormation about player`s loss   
    if tries == 0:
        os.system('cls||clear')
        print ('You have ' + str(round(gamePoints))+ ' points')
        drawHangman(tries)
        print("You lost!")
        print("The answer was " + randomWord + ".")
    
    # suggest to continue game
    answer = input('Would you like continue game (y/n)? ').lower()
    if answer == 'y' or answer == 'yes':
        continue
    else:
        break

