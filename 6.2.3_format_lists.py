def format_list(my_list):
    uneven_list_members = my_list[0::2]
    joinlist = ",".join(uneven_list_members) + ", and " + my_list[-1]
    print(joinlist)


my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"] 
def main():
    # Call the function func
    format_list(my_list)
if __name__ == "__main__":
    main()
