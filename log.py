#!/usr/bin/env python

from random import Random

def random_str(randomlength=24):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def out():
    i = 0
    for i in range[0,1000]:
        i =+1
        return i



if __name__ == '__main__':
#    print random_str()
    print out()
