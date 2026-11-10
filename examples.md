# TextTools — Examples

Real output captured from actual runs of `texttools.py`.

## slugify

```bash
python3 texttools.py slugify --text "Hello World! This is Great"
```

Output:

```
hello-world-this-is-great
```

## wordcount

```bash
python3 texttools.py wordcount --text "one two three"
```

Output:

```
Words: 3
Characters: 13
Lines: 1
```

## dedupe (from a file)

The file `lines.txt` contains:

```
apple
banana
apple
cherry
banana
```

Command:

```bash
python3 texttools.py dedupe --file lines.txt
```

Output:

```
apple
banana
cherry
```

## squeeze

```bash
python3 texttools.py squeeze --text "too    many     spaces here"
```

Output:

```
too many spaces here
```
