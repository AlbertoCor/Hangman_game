import os
import random
import numpy
# import pygame

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
            words.append(line.strip())
    randomword = random.choice(words)
    print(f"\nEsta es la palabra secreta: {randomword}")
    return randomword

def normalize(s): # It removes the accents of a string
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def hide_words(word):
    hide = ['_' for letter in word]     # With this loop generate number of underdash of the secret word
    hide_word = "".join(hide)           # Here join underdash of a hidden secret word
    print(hide_word)                    # Test output underdash of secret word
    return hide

def compare_words(randomword, guess_letter, hide_word):      
    # assert len(user) == 1, "presiona mas de una letra"
    you_got_it = False
    for l in range(len(randomword)):        #This is the check for every input
        # print(l)
        # the_letter = normalize(randomword[l])
        rand_word = randomword[l]
        # print(rand_word)
        if guess_letter == rand_word:
            if guess_letter == hide_word[l]:
                print("you dont guess one >:V")
                you_got_it = True
                # continue
            else:
                hide_word[l] = randomword[l]
                print("you have guess one :V")
                # points += 100
                you_got_it = True
                # continue
    if you_got_it == False: #This is the life check
        input('You lose one life, PRESS A KEY TO CONTINUE')
    # lifes -= 1
    # if lifes == -1:
    #     print(f'The word was {the_word}')
    #     choice = input('☠ Press X to play again, press any other key to quit ☠').upper()
    #     if choice == 'X':
    #         lifes = 7
    #         the_word = random.choice(words)
    #         the_secret_word = ['_' for letter in the_word]
    #         continue
    #     else:
            # break


def life_points():
    pass

def run():
    keep_try = True
    rand_word = read()
    hide_word = hide_words(rand_word)
    while keep_try:
        os.system("cls")        #clear windows every try
        printable_secret_word = ''.join(hide_word) #It's the random selected word but like this ______ and it's being updated
        if printable_secret_word == rand_word: #This is the win check
            print("you win")
        print(printable_secret_word)
        print(f"Esta es la palabra secret: {rand_word}")
        guess_letter = input("\nTeclea una letra: ")
        compare_words(rand_word , guess_letter, hide_word)
        

if __name__ == "__main__":
    run()
            

#check ascii theme
#https://dev.to/lakatos88/ascii-themes-node-js-cli-interface-to-generate-themed-ascii-art-4ck8

    