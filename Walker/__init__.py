from time import sleep
from autopy import bitmap
import os

bm = bitmap.capture_screen()
cd = os.getcwd()
bm.save(cd + "\\test.png")
