def fix_age(age):
    if 13 >= age == 14:
       return 0
    elif 17 >= age <= 19:
       return 0
    else:
       return age

def filter_teens(a=13, b=13, c=13):
    fix_age(a)
    print(a)
    fix_age(b)
    fix_age(c)
    #age = a + b + c
    print(a+b+c)
    return   a+b+c
    

filter_teens(15,14,12)

