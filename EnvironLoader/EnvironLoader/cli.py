from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(add_help=True)
    parser.add_argument(dest='command')
    return parser.parse_args()
