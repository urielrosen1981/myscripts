letter_guessed = input("Guess a letter: ")
def check_valid_input(letter_guessed, old_letters_guessed): 
        
        charcount = len(letter_guessed)
        print(charcount)
        if charcount >= 2:
            print("False")
            return False
        elif letter_guessed.isalpha == False:
            print("False")
            return False
        
        elif charcount == 1 and letter_guessed.isalpha == True:
            print("True")
            return True
        elif letter_guessed in old_letters_guessed:
            print("False")
        else:
            old_letters_guessed.append(letter_guessed)
            print(old_letters_guessed)

old_letters_guessed = ["a"] 




def main():
    # Call the function func
    check_valid_input(letter_guessed, old_letters_guessed)
if __name__ == "__main__":
    main()