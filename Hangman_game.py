import os
import random
# import pygame             # pygame module version of hagman game

# to be added to another file
#------------------------------------------------------
def display():              # Screen dimensions usable for pygame module
    pass

def menu():                 # Screen with menu of configurations  selected by the player
    pass

def two_players():          # 2 players mode 
    pass

#------------------------------------------------------

def read():                                                                                     # In this function we read file.txt and return a random word from the file
    words = []                                                                                  # An empty list will store the words from the file.txt
    with open("Python_Intermedio\Hangman_Game\Data\data.txt", "r", encoding="utf-8") as f:      # function used to open a file from path writed as reading, encode as utf-8, renamed as f
        for line in f:                                                                          # loop for format the data
            words.append(line.strip())                                                          # List storage of words from file.txt and rip any blank space
    randomword = random.choice(words)                                                           # A random word selected from formated file.txt 
    print(f"\nEsta es la palabra secreta: {randomword}")                                        # A print statement for chechk secret word
    return randomword                                                                           # Return the value it keep a random word selected from file .txt

def normalize(s):                                                                               # It removes the accents of a string
    replacements = (                                                                            # A tuple contain special caracters will be simplified to verificate with word
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:                                                                   # Loop for check all special caracters in tuple
        s = s.replace(a, b).replace(a.upper(), b.upper())                                       # the variable s store for replaced special character to a letter
    return s                                                                                    # Value character without aphostrophe returned as s variable

def hide_words(word):                                                                           #
    hide = ['_' for letter in word]                                                             # With this loop generate number of underdash of the secret word
    hide_word = "".join(hide)                                                                   # Here join underdash of a hidden secret word
    print(hide_word)                                                                            # Test output underdash of secret word
    return hide                                                                                 # Return underdash number of letters in the secret word

def compare_words(randomword, guess_letter, hide_word):                                         #
    # assert len(user) == 1, "presiona mas de una letra"
    you_got_it = False                                                                          # Parameter will be false to 
    for l in range(len(randomword)):                                                            # This is the check for every input
        # the_letter = normalize(randomword[l])
        rand_word = randomword[l]                                                               # Random word from read function, spell every letter as loop
        if guess_letter == rand_word:                                                           # Condition if letter input from user and letter from random word to compare
            if guess_letter == hide_word[l]:                                                    # Condition if letter input from user and 
                you_got_it = True
                continue
            else:
                hide_word[l] = randomword[l]
                # points += 100
                you_got_it = True
                continue
    if you_got_it == False: #This is the life check
        input('You lose one life, PRESS A KEY TO CONTINUE')

def life_points():
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
            break
        print(printable_secret_word)
        print(f"Esta es la palabra secret: {rand_word}")
        guess_letter = input("\nTeclea una letra: ")
        compare_words(rand_word , guess_letter, hide_word)
        

if __name__ == "__main__":
    run()
            

#check ascii theme
#https://dev.to/lakatos88/ascii-themes-node-js-cli-interface-to-generate-themed-ascii-art-4ck8

    