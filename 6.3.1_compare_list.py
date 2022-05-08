def are_lists_equal(list1, list2):
    lenlist1 = len(list1)
    lenlist2 = len(list2)
    if lenlist1 == lenlist2:
        print("True")
    else:
        print("False")

    list1.sort()
    print(list1)
    list2.sort()
    print(list2)
    if(list1==list2):
        #return "Equal"
        print("equal")
    else:
        print("not equal")
        #return "Non equal"

list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
list3 = [9, 0, 5, 10.5]
#my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"] 
def main():
    # Call the function func
    are_lists_equal(list1, list2)
if __name__ == "__main__":
    main()
