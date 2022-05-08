import re

def numbers_letters_count(s):
    #s = "jjjj jklkjl 88808.7"
    n = a = ""
    strlen = len(s)
    print(strlen)
    for x in s:
        if x.isdigit():
            n += x
    
    digitlen = len(n)
    charlen = strlen - digitlen
    list = [digitlen, charlen]

    print (digitlen)
    print (charlen)
    print(list)
    print("Numbers in string=", n)


def main():
    # Call the function func
    numbers_letters_count("vjhvj jhbkjbkjb 6666.6")
if __name__ == "__main__":
    main()