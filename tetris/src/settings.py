from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

S_WIDTH = 800

S_HEIGHT = 700

PLAY_WIDTH = 300  # meaning 300 // 10 = 30 width per block

PLAY_HEIGHT = 600  # meaning 600 // 20 = 30 height per block

BLOCK_SIZE = 30

TOP_LEFT_X = (S_WIDTH - PLAY_WIDTH) // 2

TOP_LEFT_Y = S_HEIGHT - PLAY_HEIGHT
