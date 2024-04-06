#!/usr/bin/python3
#This is a code that prints all possible different combinations of two digits
for x in range(0, 10):
    for y in range(x + 1, 10):
        if x == 0 and y == 9:
            print('89')
        else:
            print('{}{}, '.format(x, y), end='')
