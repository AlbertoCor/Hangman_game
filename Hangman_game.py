import os
# import pygame
import random

# to be added to another file
#------------------------------------------------------

def display():
    pass

def menu():
    pass

def two_players():
    pass

#------------------------------------------------------

def read():
    words = []
    with open("Python_Intermedio\Hangman_Game\Data\data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line)
            # print(line)
    word = list(words)
    randomword = random.choice(word)
    print(randomword)
    lenght = list(enumerate(randomword.rstrip(),0))
    # print(lenght)
    numb_underline = len(randomword.rstrip())
    # print(numb_underline)
    under_line = " _"
    print(under_line * numb_underline)
    return lenght

    # for hides in lenght:
    #     hide_word.append("_")
    # print(str(hide_word)[1:-1])           #use for quit brackets on list
    
    # word = list(enumerate(words))
    # print(word)
    # print(line)


def run():
    read()
    guess_word = input("Teclea una letra: ")

    # while True:           #loop for  checking letters with secret word
    #     pass        


    # lenghtWord = len()
    # while True:
    #     print("guess the word >:V")
    #     word
    #     letter = input("type a letter: ")
        

if __name__ == "__main__":
    run()
    # while True:
    #     print("Guess the word >:V !!!")
    #     read.lenght()
    #     pass

    