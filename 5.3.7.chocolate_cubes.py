def chocolate_maker(small, big, x):
    small_length = 1
    big_length = 5
    row_length = (small_length * small) + (big_length * big)
    print(row_length)
    if row_length == x:
        print(True)
    else:
        print(False)
chocolate_maker(3, 1, 8)