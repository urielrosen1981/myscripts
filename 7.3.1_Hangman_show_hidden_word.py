#old_letters_guessed = ""
#def show_hidden_word(secret_word, old_letters_guessed): 
    #old_letters_guessed = input("please guess a letter ")
    #secret_word_count = len(secret_word)
    #print(secret_word_count)
    #old_letters_guessed_list = []
    #old_letters_guessed = input("please guess a letter ") 
   # print(old_letters_guessed_list)
    
    #for old_letters_guessed in secret_word:
        #if old_letters_guessed not in secret_word:
            #old_letters_guessed_list.append(old_letters_guessed)
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





def main():
    # Call the function func
    old_letters_guessed = []
    show_hidden_word("happy",old_letters_guessed)
if __name__ == "__main__":
    main()