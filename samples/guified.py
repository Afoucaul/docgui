'''Dummy program

Usage:
    dummy
    dummy foo
    dummy bar <a>
'''

from docopt import docopt
from docgui import guify


def no_command(args):
    print("NO COMMAND", args)


def command_foo(args):
    print("COMMAND FOO", args)


def command_bar(args):
    print("COMMAND BAR", args)


def main(args):
    if args['foo']:
        command_foo(args)
    elif args['bar']:
        command_bar(args)
    else:
        no_command(args)


guify()
