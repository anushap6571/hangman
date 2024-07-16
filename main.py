import sys
import random


def check(word, guess):
    tracker = 0;
    lives_lost = 0
    for letter in word:
        if letter == guess:
            print("Right ")
        else:
            print("Wrong ")
            tracker +=1
    if tracker == len(word):
        lives_lost += 1
    return lives_lost
    
word_list = ["smart", "birthday", "fashion", "python"]
word = random.choice(word_list)
lives = 5
lives_lost = 0

while lives_lost <= lives:
    guess = input("Guess a letter or word: ").lower()
    if len(guess) > 1:
        if guess == word:
            print("correct")
            sys.exit()
        else: 
            print("incorrect")
            lives_lost += 1
    lives_lost = lives_lost + check(word, guess)
    print("Remaining Lives: ", (5 - lives_lost))