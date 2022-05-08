
def seven_boom(end_number):
    list = []
    for num in range(0,end_number):
        if "7" in str(num) or num%7  == 0:
            num = "BOOM"
            list.append(num)
        else:
            list.append(num)
        #return list    
            print(list)

             
def main():
    # Call the function func
    seven_boom(100)
if __name__ == "__main__":
    main()