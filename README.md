# TextTools

Everyday text transformations from the command line: case changes, URL slugs, whitespace cleanup, duplicate line removal and word counts, in one tiny script.

## Subcommands

Every subcommand takes input from exactly one of `--text "..."` or `--file path`, and prints the result to stdout.

- `upper` — print the text in UPPERCASE. Example: `python3 texttools.py upper --text "hello there"` prints `HELLO THERE`.
- `lower` — print the text in lowercase. Example: `python3 texttools.py lower --text "Hello There"` prints `hello there`.
- `title` — print the text in Title Case. Example: `python3 texttools.py title --text "hello there"` prints `Hello There`.
- `slugify` — lowercase the text, replace any run of non-alphanumeric characters with a single hyphen, and strip leading and trailing hyphens. Example: `python3 texttools.py slugify --text "Hello World! This is Great"` prints `hello-world-this-is-great`.
- `squeeze` — collapse all whitespace runs (including newlines) to single spaces and trim. Example: `python3 texttools.py squeeze --text "too    many     spaces here"` prints `too many spaces here`.
- `dedupe` — treat the input as lines and remove duplicate lines, keeping first occurrence order. Example: `python3 texttools.py dedupe --file lines.txt`.
- `wordcount` — print the word count, the character count (including spaces), and the line count. Example: `python3 texttools.py wordcount --text "one two three"` prints `Words: 3`, `Characters: 13`, `Lines: 1`.

## Requirements

- Python 3
- Standard library only, nothing to install

## Usage

```bash
python3 texttools.py slugify --text "Hello World! This is Great"
python3 texttools.py wordcount --text "one two three"
python3 texttools.py dedupe --file lines.txt
python3 texttools.py squeeze --text "too    many     spaces here"
```

Run `python3 texttools.py --help`, or `python3 texttools.py <subcommand> --help`, for full usage. A missing input file exits with code 2 and a clear error message.

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Muhammad Ahsan Anwar.
