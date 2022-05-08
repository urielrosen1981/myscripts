def is_greater(my_list, n):
    
    list2 = []

    for i in my_list:
        if i > n:
        #print(i)
        #if n > my_list:
        
            list2.append(i)
            print(list2)
            #return(a)
            #print(list2)           #print(list2)
            #print(a)
my_list = [1, 30, 25, 60, 27, 28]
def main():
    # Call the function func
    is_greater(my_list,10)
if __name__ == "__main__":
    main()