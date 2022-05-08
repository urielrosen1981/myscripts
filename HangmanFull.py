WELCOME = ("""| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\\__,_|_| |_|\__, |_| |_| |_|\\__,_|_| |_|
                     __/ |                      
                    |___/ """)

hangman_photos = {1: " x-------x ", 2: """    x-------x
    |
    |
    |
    |
    |""", 3: """    x-------x
    |       |
    |       0
    |
    |
    |""", 4: """    x-------x
    |       |
    |       0
    |       |
    |
    |""", 5: """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 6: """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", 7: """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""} 


def print_hangman(num_of_tries):
    return hangman_photos[num_of_tries]    
    #func prints the hangman photoes according to player guesses

def check_input(str):
    # func return False in case the input is not valid or has been guessed before
    #letter_guessed = input("please enter a letter: ")
    str = str.lower()
    if len(str) > 1:
        a = 0
        for i in str:
            if i.isalpha() == False:
                a = a + 1
        if a > 0: 
            return "E3"
        else:
            return "E1"
    elif str.isalpha() == False:
        return "E2"
    else:
        return (str)
    
def is_valid_input(letter_guessed):
    #this function checks if the guessed letter by the player is valid
    #function accepts strings
    #letter must be in english, only 1 letter, no symbols or numbers
    result = check_input(letter_guessed)
    if result == letter_guessed:
        return True
    else:
        return False

def check_valid_input(letter_guessed, old_letters_guessed):
    #this func checks if the letter has been guessed before as well as valid
    result = is_valid_input(letter_guessed)
    if result == True:
        if letter_guessed not in old_letters_guessed:
            return True
    else:
        return False


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    #func checks the letter guessed by player according to rulse and return
    #the guessed letters in order
    result = check_valid_input(letter_guessed, old_letters_guessed)
    if result == True:
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        separetor = '-> '
        lst = sorted(old_letters_guessed)
        print(separetor.join(lst))
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    # function take a str (secrat word, and the list of already guessed letters,
    # and print the letters in the exact places in the word
    str = ""
    word = list(secret_word)
    for i in word:
        if i in old_letters_guessed:
            str = str + i + " "
        else:
            str = str + "_ "
    return str

def check_win(secret_word, old_letters_guessed):
    #func checks if player won the game
    str = show_hidden_word(secret_word, old_letters_guessed)
    if "_" in str:
        return False
    else:
        return True
    
def choose_word(file_path, index):
    #func recive a text file with words and return a tuple with two obj:
    #how many words in file , the word in the index
    file = open(file_path, 'r')
    words_str = file.read()
    lst = words_str.split(' ')
    new_lst = []
    for i in lst:
        if lst.count(i) > 1:
            lst.remove(i)
    a = ""
    if int(index) > len(lst):
        a = lst[int(index) - len(lst)]
    else:
        a = lst[int(index)]
    return a

def print_spaces(secret_word):
    number_of_spaces = len(secret_word)
    spaces = "_ "
    return (spaces * number_of_spaces)
#-----------------------------------------------------
#lets start
def main():
    print(WELCOME)

    path = input("please add a path for a word bank (txt only): ")
    word_index = input("please choose a number as a word index: ")

    print (hangman_photos[1])
    secret_word = choose_word(path, word_index)
    print(print_spaces(secret_word))

    num_of_tries = 1
    old_letters_guessed = []
    while num_of_tries < 7:
        letter_guessed = input("plese guess a letter: ")
        letter_guessed = letter_guessed.lower()
        old_letters_guessed.append(letter_guessed)
        check = try_update_letter_guessed(letter_guessed, old_letters_guessed)
        if check is False and letter_guessed not in secret_word:
            num_of_tries += 1
            print(':-(')
            print(hangman_photos[num_of_tries])
            print(show_hidden_word(secret_word, old_letters_guessed))

        else:
            print(":-)")
            print(show_hidden_word(secret_word, old_letters_guessed))
        
        win = check_win(secret_word, old_letters_guessed)
        if win is True:
            print('WIN :-)')
            break
        else:
            continue
    if num_of_tries > 6:
        print('lose :-(')
 
if __name__ == '__main__':
    main()