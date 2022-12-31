import curses
from frame import Frame

class Window:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.frame = Frame()
        self.drawing = False


    def prompt_new(self):
        prompt_1 = "space: start a new picture"
        prompt_2 = "    q: quit"
        self.stdscr.addstr(curses.LINES-3, 0, prompt_1)
        self.stdscr.addstr(curses.LINES-2, 0, prompt_2)


    def handle_input(self, c):
        if self.frame.is_complete():
            self.drawing = False
        if not self.drawing:
            if c == ord("q"):
                return "quit"
            elif c == ord(" "):
                self.frame.new_image()
                self.drawing = True
                return "continue"
            else:
                return "continue"
        else:
            self.frame.reveal()
            return "continue"


    def draw(self):
        self.stdscr.clear()
        self.frame.draw(self.stdscr)
        if not self.drawing:
            self.prompt_new()
        self.stdscr.refresh()
