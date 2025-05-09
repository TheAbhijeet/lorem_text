import argparse
import sys
from lorem_text import lorem


def lorem_cli():
    parser = argparse.ArgumentParser(description="Console script for lorem.")
    parser.add_argument("--words", type=int, help="Returns lorem ipsum words")
    parser.add_argument("--s", action="store_true", help="Returns lorem ipsum sentence")
    args = parser.parse_args()

    # Returns lorem ipsum words
    if args.words:
        print(lorem.words(args.words))

    # Returns a lorem ipsum sentence
    elif args.s:
        print(lorem.sentence())

    # Returns a lorem ipsum paragraph by default
    else:
        print(lorem.paragraph())


if __name__ == "__main__":
    sys.exit(lorem_cli())  # pragma: no cover
