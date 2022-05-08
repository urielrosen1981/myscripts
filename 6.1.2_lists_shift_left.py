def shift_left(my_list):
    my_list = my_list[1:] + my_list[:1]
    print(my_list)
    return my_list
my_list = ["test", "pppoo", "uvhgvh"]
shift_left(my_list)