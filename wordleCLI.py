import os
import time
import random

wordList = open("wordlelist", "r").readlines()
random.seed()
word = wordList[random.randint(0,len(wordList)-1)].strip("\n")
guesses = 6
solved = False

while (guesses > 0) and (solved == False):
    feedback = "....."
    guesses = guesses - 1
    valid = False
    guess = ""
    while not valid:
        guess = input("Make a guess:")
        if guess.isalpha():
            if len(guess) == 5:
                if guess + "\n" in wordList:
                    valid = True
                else:
                    print("Invalid guess. I don't know that word")

            else:
                print("Invalid guess. Only use 5 letter words")
        else:
            print("Invalid guess. Only use letters")
    if guess ==  word:
        solved = True
    tempword = word
    for x in range(5):
        if guess[x] == tempword[x]:
            feedback = feedback[:x] + 'G' + feedback[x+1:]
            tempword = tempword[:x] + '.' + tempword[x+1:]
    for x in range(5):
        if guess[x] in tempword and feedback[x] != 'G':
            feedback = feedback[:x] + 'Y' + feedback[x+1:]
    print(feedback)

if solved == True:
    print("Success!")
else:
    print("Failure, the word was " + word)
