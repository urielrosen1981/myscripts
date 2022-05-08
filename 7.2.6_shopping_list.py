def shopping_menu():
    print("""1. List of products \n2. Number of products\n3. Is my product in list\n4. How many times a product is in the list\n5. Enter product to delete\n6. Add product to list\n7. Print illegal products\n8. Remove duplicates from list\n9. exit      """)
    num = 0
    products = list(input("please enter items for shoping list: ").split(","))
    while (num < 9 ):
        num = int(input("Please enter a number between 1-9: "))
        if (num == 1):
            func1(products)
        elif (num == 2):
            func2(products)
        elif (num == 3):
            func3(products)
        elif (num == 4):
            func4(products)
        elif (num == 5):
            func5(products)
        elif (num == 6):
            func6(products)
        elif (num == 7):
            func7(products)
        elif (num == 8):
            func8(products)
        elif (num == 9):
            break
    return products

def func1(products):
    print(products)
def func2(products):
    num_products = len(products)
    print("The number of products you entered: " ,num_products)
def func3(products):
    check_product = input("please enter item to check if in the list ")
    if check_product in products:
        print("product" ,check_product, "in list" )
    else:
        print(check_product ,"not in list")
def func4(products):
    check_product = input("please enter item to check how many of it are in the list ")
    if check_product in products:
        prods = products.count(check_product)
        print(prods)
    else:
        print("not in list")

def func5(products):
    print(products)
    prodremove = input("please enter item to remove: ")
    products.remove(prodremove)
    print(products)
def func6(products):
    print(products)
    prodadd = input("please enter item to add: ")
    products.append(prodadd)
    print(products)
def func7(products):
    for ill_prod in products:
        #if ill_prod.isalpha == False:
        if len(ill_prod) < 3 or  ill_prod.isalpha() == False:    
            ill_list = []
            ill_list.append(ill_prod)
            print(ill_list)
def func8(products):
    print(products)
    a = list(set(products))
    print(a)
def main():
    # Call the function func
    shopping_menu()
if __name__ == "__main__":
    main()