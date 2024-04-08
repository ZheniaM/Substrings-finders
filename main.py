from substring_finders import __all__ as sf__all__
import substring_finders
from argparse import ArgumentParser


def create_parser() -> ArgumentParser:
    parser: ArgumentParser = ArgumentParser(
        description="Find substrings in a given text.")
    parser.add_argument(
        "-t", "--text", type=str,
        help="The input text to search for substrings.")
    parser.add_argument(
        "-f", "--file", dest="filename", metavar='FILENAME',
        help="Read the input text from FILENAME instead of standard input.")
    parser.add_argument(
        "-s", "--substring", type=str, required=True,
        help="String to find within the input text")
    parser.add_argument(
        "--finder", type=str, default="bruteforce",
        dest="finder", choices=sf__all__,
        help=f"""Specify which algorithm to use for finding the substring.
             Choices are {'{'+', '.join(sf__all__)+'}'}
             (default is bruteforce).""")
    return parser


def main() -> None:
    args = create_parser().parse_args()
    if args.filename:
        with open(args.filename) as file:
            finder = getattr(substring_finders, args.finder)
            print(*finder(file.read(),  args.substring))

    elif args.text:
        finder = getattr(substring_finders, args.finder)
        print(*finder(args.text,  args.substring))


if __name__ == "__main__":
    main()
