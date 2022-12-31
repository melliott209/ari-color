"""Contains the Image class."""

import random

class Image():

    """A 2D ASCII image loaded from a text file."""

    def __init__(self, img_path):

        """Initialize the image using the given path."""

        self.lines: list[str] = self.load_image(img_path)
        self.height: int = len(self.lines)
        self.width: int = len(max(self.lines, key=len))
        self.revealed: list[str] = [""] * self.height
        self.indexes: list[int] = list(range(self.height))
        random.shuffle(self.indexes)
        self.idx: int = 0
        for i, line in enumerate(self.lines):
            self.lines[i] = line.rstrip() + " " * (self.width - len(line))


    def load_image(self, path: str) -> list[str]:

        """Load the lines of a text file."""

        with open(path, 'r', encoding='UTF-8') as file:
            return file.readlines()


    def reveal_line(self) -> None:

        """Get a random line of the image, that hasn't been retrieved before."""

        cur_idx = self.indexes[self.idx]
        string: str = self.lines[cur_idx]
        self.revealed[cur_idx] = string
        self.idx += 1


    def is_complete(self) -> bool:

        """Checks whether all of the lines of the image have been accessed."""

        return self.idx == self.height
