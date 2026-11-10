"""Run the app: python -m app <command> ..."""

import argparse
import sys

from app import __version__


def main(argv=None):
    parser = argparse.ArgumentParser(prog="python -m app")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("version", help="print the app's version")
    args = parser.parse_args(argv)
    if args.command == "version":
        print(__version__)
    return 0


if __name__ == "__main__":
    sys.exit(main())
