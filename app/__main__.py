"""Run the app: python -m app <command> ..."""

import argparse
import sys

from app import __version__
from app.count import count_words


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python -m app")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("version", help="print the app's version")
    count = sub.add_parser("count", help="count the words in a text file")
    count.add_argument("file", help="the text file to count")
    args = parser.parse_args(argv)
    if args.command == "version":
        print(__version__)
        return 0
    try:
        n = count_words(args.file)
    except FileNotFoundError:
        print(f"cannot open {args.file}", file=sys.stderr)
        return 2
    print(f"words: {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
