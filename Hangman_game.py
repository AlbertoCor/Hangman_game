import os
import random
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
#Check this open file
#(
    #     words = []
    # with open('./files/data.txt', 'r', encoding='utf-8') as file: # Here we get the words from the file and make a list
    #     for line in file:
    #         words.append(line.strip().upper())

    # the_word = random.choice(words).upper() #Here we make the '_' list according to the random selected word
    # the_secret_word = ['_' for letter in the_word]
    # keep_trying = True
# )



def read():
    words = []
    with open("Python_Intermedio\Hangman_Game\Data\data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line)
            # print(line)
    word = list(words)
    randomword = random.choice(word)
    print(f"\nEsta es la palabra secreta: {randomword}")
    return randomword

def hide_words(word):
    the_secret_word = ['_' for letter in word]
    numb_underline = len(word.rstrip())
    # print(numb_underline)
    under_line = "_"
    print(under_line * numb_underline)

def compare_words(randomword, lines):
    # lenght = list(enumerate(randomword.rstrip(),0))
    # print(lenght)
    # if guess_word in str(lenght):
        # print("ther its a letter")        
    rand_word = list(randomword)
    hiden_lines = list(lines)
    keep_try = True
    while keep_try:
        # assert len(user) == 1, "presiona mas de una letra"
        os.system("cls")        #clear windows every try
        for i in range(0, len(rand_word)):
            if rand_word[i] == keep_try:
                hiden_lines[i] = rand_word[i]
        print(hiden_lines.upper())
        print("\n")
    print("you win")

    #   for i in range(len(the_word)): #This is the check for every input
    #         for l in range(len(the_word)):
    #             the_letter = normalize(the_word[l])
    #             if your_letter == the_letter:
    #                 if your_letter == the_secret_word[l]:
    #                     you_got_it = True
    #                     continue
    #                 else:
    #                     the_secret_word[l] = the_word[l]
    #                     points += 100
    #                     you_got_it = True
    #                     continue
        

def run():

    rand_word = read()
    # hide_words(rand_word)
    # lines = hide_words()
    lines = "blue"
    # hide_letter = list(enumerate(rand_word))
    # guess_word = input("Teclea una letra: ")
    compare_words("blue", lines)
       


if __name__ == "__main__":
    run()
            

#check ascii theme
#https://dev.to/lakatos88/ascii-themes-node-js-cli-interface-to-generate-themed-ascii-art-4ck8

    