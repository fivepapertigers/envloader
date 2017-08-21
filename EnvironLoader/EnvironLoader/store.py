""" Module for storing environment variables """
from .cli import get_input
from .db import insert_env_var


def main(key=None, val=None, description=None):
    print "\n---------------------------"
    print "Store environment variables"
    print "---------------------------\n"
    while True:
        print "New environment variable:"
        if not key:
            key = get_input('Key? ', _require_value) or ''
        if not val:
            val = get_input('Value? ', _require_value) or ''
        if not description:
            description = get_input('What is the description? ') or ''
        insert_env_var(key, val, description)
        print "Saved!\n"

        another = get_input('Would you like to store another? [Y,n] ')
        if another and another.lower() == 'n':
            break
        print '\n'

def _require_value(inp):
    if inp:
        return inp
    print "ERROR: you must enter a value for this field"

if __name__ == '__main__':
    main()
