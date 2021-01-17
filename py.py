#!/usr/bin/python3
def f(x, y = 1):
    """
    Returns x * y
    :param x: int first integer to be added.
    :param y: int second integer to be added (Not requared, 1 by default).
    :return : int multiplication of x and y.
    """
    return x * y
x = 5
#print(f(2))

#a = int(input('type a number'))
#b = int(input('type another number'))
#try:
#    print(a / b)
#except ZeroDivisionError:
#    print('b cannot be zero. Try again')

def fac(x):
    """
    Returns x!
    :param x: int integer to be added
    :return : int integer x!
    """
    if x == 1 or x == 0:
        return 1
    else:
        return x * fac(x-1)
print(fac(4))
