from docopt import parse_pattern, formal_usage, printable_usage


def get_commands(doc):
    parsed = parse_pattern(formal_usage(printable_usage(doc)), [])

    commands = []
    for command in parsed.children[0].children:
        children = command.children
        if children:
            commands.append(children[0])

    return commands
