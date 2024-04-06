#!/usr/bin/python3
# This code prints the ASCII alphabet in reverse order in alternating mode
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        diff = 0
    else:
        diff = 32
    print('{}'.format(chr(i - diff)), end='')
