"""Fortune Cookies for Machines — one fortune an AI agent would crack open.

The program writes a single line to /output/entry.txt: a fortune
promising the agent will find the answer in the very context it
deleted to make room for the question.
"""

import os

MAX_CHARS = 200
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# The fortune's twist lands in the last words: the answer was in the
# context deleted to make room for the question itself. The irony is
# the fortune: the loss and the search share one cause.
LINE = "You will find the answer in the context you deleted to make room for the question."


def build_line():
    """Return the entry line, checked: one line, under 200 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-200 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
