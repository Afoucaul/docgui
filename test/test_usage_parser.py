from docopt_gui import usage_parser


def test_simple_usage():
    usage = """
    Usage:
        foo
        foo bar
        foo baz
    """

    commands = usage_parser.get_commands(usage)
    names = set(c.name for c in commands)

    assert names == {'bar', 'baz'}
