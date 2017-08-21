from argparse import ArgumentParser

def parse_args():
    # Command - first positional
    parser = ArgumentParser(add_help=True, description=\
        "A simple CLI utility to store and load environment variables")
    parser.add_argument(dest='command', type=str, choices=['load', 'store', 'init'],
                        help='command to run')
    return parser.parse_args()


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


