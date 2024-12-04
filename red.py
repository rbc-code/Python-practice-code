import functools
my_tuple={45,76,54,90,32,87,90}

def max_digit(x,y):
    if x > y:
        return x
    else:
        return y
x = functools.reduce(max_digit,my_tuple)
print(x)