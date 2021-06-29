from pygame import display
from src import settings
from src.components import Menu

if __name__ == '__main__':
    win = display.set_mode((settings.S_WIDTH, settings.S_HEIGHT))
    display.set_caption('Tetris')
    Menu(win).run()
