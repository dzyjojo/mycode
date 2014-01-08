#! /usr/bin/env python
import os
import sys

def get_environ():
    environ = os.environ
    return environ

def print_environ(environ):
    for key in environ.keys():
       value = environ[key]
       print '%-40s\t%.40s' % (key, value)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        # in a case of ./get_env PWD
        key = sys.argv[1]
        # key should be PWD
        environ = get_environ()
        print environ[key]
    elif len(sys.argv) == 1:
        # in a case of ./get_env
        environ = get_environ()
        print_environ(environ)
    else:
        # do nothing
        pass

