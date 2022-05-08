def longest(my_list):

    my_list_sorted = sorted(my_list, key=len)
    last_and_longest = my_list_sorted[-1]
    print(last_and_longest)
    return my_list

my_list = ["111", "234", "2000", "goru", "birthday", "09"]
def main():
    # Call the function func
    longest(my_list)
if __name__ == "__main__":
    main()

    