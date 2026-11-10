#!/usr/bin/env python3
"""TextTools - everyday text transformations from the command line.

Standard library only. Every subcommand takes its input from exactly
one of --text "..." or --file path, and writes the result to stdout.
"""

import argparse
import re
import sys


def read_input(args):
    """Return the input text from --text or --file."""
    if args.text is not None:
        return args.text
    try:
        with open(args.file, "r", encoding="utf-8") as handle:
            return handle.read()
    except FileNotFoundError:
        print(f"error: file not found: {args.file}", file=sys.stderr)
        sys.exit(2)
    except OSError as exc:
        print(f"error: cannot read file {args.file}: {exc}", file=sys.stderr)
        sys.exit(2)


def cmd_upper(text):
    print(text.upper())


def cmd_lower(text):
    print(text.lower())


def cmd_title(text):
    print(text.title())


def cmd_slugify(text):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    print(slug)


def cmd_squeeze(text):
    print(" ".join(text.split()))


def cmd_dedupe(text):
    seen = set()
    unique = []
    for line in text.splitlines():
        if line not in seen:
            seen.add(line)
            unique.append(line)
    for line in unique:
        print(line)


def cmd_wordcount(text):
    words = len(text.split())
    characters = len(text)
    lines = len(text.splitlines()) if text else 0
    print(f"Words: {words}")
    print(f"Characters: {characters}")
    print(f"Lines: {lines}")


COMMANDS = {
    "upper": cmd_upper,
    "lower": cmd_lower,
    "title": cmd_title,
    "slugify": cmd_slugify,
    "squeeze": cmd_squeeze,
    "dedupe": cmd_dedupe,
    "wordcount": cmd_wordcount,
}


def build_parser():
    parser = argparse.ArgumentParser(
        prog="texttools.py",
        description="Everyday text transformations: case changes, slugify, "
                    "whitespace cleanup, line dedupe and word counts.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    help_texts = {
        "upper": "Print the text in UPPERCASE.",
        "lower": "Print the text in lowercase.",
        "title": "Print the text in Title Case.",
        "slugify": "Turn the text into a URL-friendly slug.",
        "squeeze": "Collapse all whitespace runs to single spaces and trim.",
        "dedupe": "Remove duplicate lines, keeping first occurrence order.",
        "wordcount": "Print word, character and line counts.",
    }
    for name, help_text in help_texts.items():
        sub = subparsers.add_parser(name, help=help_text)
        group = sub.add_mutually_exclusive_group(required=True)
        group.add_argument("--text", help="Input text given directly.")
        group.add_argument("--file", help="Path to a file to read input from.")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    text = read_input(args)
    COMMANDS[args.command](text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
