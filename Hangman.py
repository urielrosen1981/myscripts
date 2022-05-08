import random

HANGMAN_ASCII_ART = (""" \n 
 Welcome to the game Hangman 
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_  \ 
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                       __/ |
                      |___/  
                      """)


print(HANGMAN_ASCII_ART)

MAX_TRIES = 6
print(MAX_TRIES)

#charater = input("Guess a letter: ")
#lower_guessed_character = charater.lower()
#print(lower_guessed_character)

get_user_input = input("please enter a word: ")
word_length = len(get_user_input)
show_uderscores = word_length * "_ "
print(show_uderscores) 

