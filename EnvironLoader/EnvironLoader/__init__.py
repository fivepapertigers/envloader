import os
import sys
from .cli import parse_args
BASE_DIR = os.path.abspath(os.path.join(os.pardir, os.path.dirname(__file__)))



def get_input(msg, callback=None, before=None):
    """ Get input from user """
    try:
        while True:
            if before:
                before(msg)
            inp = raw_input(msg)
            if inp == 'q':
                exit()
            if not callback:
                return inp

            result = callback(inp)
            if result:
                return result

    except KeyboardInterrupt:
        exit()


def start_envloader():
    print parse_args()
    print sys.argv
