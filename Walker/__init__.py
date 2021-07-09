from time import sleep
from autopy import bitmap
from .BetterMouse import BetterMouse
import os

bm = bitmap.capture_screen()
cd = os.getcwd()
bm.save(cd + "\\imgs\\test.png")
