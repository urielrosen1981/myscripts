from typing import Counter


charater = input("Guess a letter: ")
lower_guessed_character = charater.lower()
charcount = len(charater)
print(charcount)
if charcount > 1 and  charater.isalpha() == False:
    print("E3")
elif charater.isalpha() == False:
    print("E2")
elif charcount > 1:
    print("E1")
elif charcount == 1:
    print(lower_guessed_character)
else :
    print("bye")

