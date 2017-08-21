import os
import sys
from .load import main as load
from .store import main as store
from .init import main as init
from .cli import parse_args


def start_envloader():
    args = parse_args()
    if args.command == 'load':
        load()
    if args.command == 'store':
        store()
    if args.command == 'init':
        init()
