import sys
from docopt_gui import application


def main(path):
    application.Application(path).run()


if __name__ == '__main__':
    main(sys.argv[1])
