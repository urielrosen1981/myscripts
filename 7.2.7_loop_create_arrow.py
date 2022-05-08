def arrow(my_char, max_length):
    my_str = ""
    i = 1
    for num in range(max_length):
        my_str += (my_char*i)
        my_str += "\n"
        i += 1
        print(my_str)
    i = -2
    for num in range(max_length):
        my_str += (my_char*i)
        my_str += "\n"
        i -= 1
        print(my_str) 
    return my_str  

def main():
    # Call the function func
    arrow("$", 5)
if __name__ == "__main__":
    main()