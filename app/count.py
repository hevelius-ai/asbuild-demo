"""Count the words in a text file: words are separated by any whitespace."""


def count_words(path):
    with open(path, encoding="utf-8") as fh:
        return len(fh.read().split())
