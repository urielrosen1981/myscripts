
def squared_numbers(start, stop):
    start
    list = []
    while start <= stop:
        list.append(start ** 2)
        start +=1
        
    print(list)



def main():
    # Call the function func
    squared_numbers(1, 100)
if __name__ == "__main__":
    main()