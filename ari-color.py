import curses
from window import Window

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.use_default_colors()
    
    win = Window(stdscr)
    
    while True:
        win.draw()
        ch = stdscr.getch()
        result = win.handle_input(ch)
        if result == "quit":
            break

curses.wrapper(main)
