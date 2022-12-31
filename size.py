"""For testing algorithms used for manipulating ASCII art .txt files"""

import sys

def left_padding(string: str) -> int:
    """Return the number of spaces before the first character."""
    if string.isspace():
        return 0
    pad: int = 0
    for char in string:
        if char == ' ':
            pad += 1
        else:
            break
    return pad

with open(sys.argv[1], 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    height = len(lines)
    longest = max(lines, key=len)
    idx = lines.index(longest)
    print(f"Longest line is line {idx}")
    max_length = len(longest)
    print("@" + "="*(max_length-1) + "@")
    for line in lines:
        line = line + (max_length - len(line)) * " "
        line = "|" + line.replace("\n", "") + "|"
        print(line)
    print("@" + "="*(max_length-1) + "@")
    print(f"Optimal Width: {max_length}\nOptimal Height: {height}")
