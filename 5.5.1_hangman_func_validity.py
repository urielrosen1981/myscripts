def is_valid_input(letter_guessed): 
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
        
    else:
        print("hgggg")

def main():
    # Call the function func
    is_valid_input("##")

if __name__ == "__main__":
    main()
