from docopt import (
    parse_pattern, 
    formal_usage, 
    printable_usage, 
    Command, 
    Pattern, 
    Argument, 
    Required,
    Option
)


def get_commands(doc):
    patterns = parse_pattern(formal_usage(printable_usage(doc)), []).children[0]

    for r in patterns.flat(Required):
        if not any(isinstance(child, Command) for child in r.children):
            r.children.insert(0, Command(''))

    return [CommandWrapper(
                cmd.flat(Command)[0].name, 
                cmd.flat(Argument), 
                cmd.flat(Option)) 
            for cmd in patterns.flat(Required)]


def walk_tree(tree, function):
    if hasattr(tree, 'children'):
        function(tree)
        [function(c) for c in tree.children]

    elif isinstance(tree, list):
        [function(c) for c in tree]

    else:
        function(tree)


class CommandWrapper:
    def __init__(self, name, args, options):
        self.name = name
        self.args = args
        self.options = options

    def __repr__(self):
        return "CommandWrapper('%s', %r)" % (self.name, self.args)
