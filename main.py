import sys
import random


def check(word, guess):
    lives_lost_in_round = 0
    if len(guess) > 1:
            if guess == word:
                print("correct")
                sys.exit()
            else: 
                print("incorrect")
                lives_lost_in_round += 1
                return lives_lost_in_round

    tracker = 0;
    for letter in word:
        if letter == guess:
            print("Right ")
        else:
            print("Wrong ")
            tracker +=1
    if tracker == len(word):
        lives_lost_in_round += 1
        print(lives_lost_in_round)
    return lives_lost_in_round

def main():
    word_list = ["smart", "birthday", "fashion", "python"]
    word = random.choice(word_list)
    lives = 5
    lives_lost = 0

    while lives_lost < lives:
        guess = input("Guess a letter or word: ").lower()
        
        lives_lost = lives_lost + check(word, guess)
        print("Remaining Lives: ", (lives - lives_lost))

if __name__ == '__main__':
    main()