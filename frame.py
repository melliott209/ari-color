import os, random, curses
from image import Image

class Frame():

    def __init__(self):
        self.new_image()


    def new_image(self):
        self.image = Image("./img/" + self.random_path())
        self.width: int = self.image.width + 3
        self.height: int = self.image.height + 2
        self.x: int = int((curses.COLS / 2) - (self.width / 2))
        self.y: int = 0
        self.image_x: int = self.x + 1
        self.image_y: int = self.y + 1


    def random_path(self):
        return random.choice(os.listdir("./img/"))


    def reveal(self) -> None:
        self.image.reveal_line()


    def is_complete(self) -> bool:
        return self.image.is_complete()


    def draw(self, stdscr) -> None:
        # Draw border
        stdscr.addstr(self.y, self.x, "@" + "="*(self.width-1) + "@")
        stdscr.addstr(self.height, self.x, "@" + "="*(self.width-1) + "@")
        for y in range(self.y+1, self.height):
            stdscr.addch(y, self.x, "|")
            stdscr.addch(y, self.x + self.width, "|")
        # Draw revealed lines
        for idx, line in enumerate(self.image.revealed):
            if line != "":
                stdscr.addstr(self.image_y + idx, self.image_x, line)
