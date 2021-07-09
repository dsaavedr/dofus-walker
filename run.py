# Start script for walking
# TODO: deal with delay between map-changes, walking and loading.
# TODO: add 'move' method to walker package.

from Walker import BetterMouse
from autopy import bitmap
import os
from threading import Timer

Bitmap = bitmap.Bitmap

mouse = BetterMouse()
# mouse.moveTo(400, 400)

left = Bitmap.open(os.getcwd() + "\\imgs\\arrow-left.png")
up = Bitmap.open(os.getcwd() + "\\imgs\\arrow-up.png")
right = Bitmap.open(os.getcwd() + "\\imgs\\arrow-right.png")
down = Bitmap.open(os.getcwd() + "\\imgs\\arrow-down.png")
screenSize = bitmap.capture_screen().bounds[1]


def move(needle, dir=0, tolerance=0.4):
    if dir == 0:
        mouse.moveTo(270, 100)
    elif dir == 1:
        mouse.moveTo(screenSize[0]/2, 15)
    elif dir == 2:
        mouse.moveTo(screenSize[0]-270, 100)
    elif dir == 3:
        mouse.moveTo(screenSize[0]/2, screenSize[1] - 130)

    screen = bitmap.capture_screen(((0, 0), (400, screenSize[1])))
    pos = screen.find_bitmap(needle, tolerance)
    if (pos):
        print(f"Found at: {pos}")
        # mouse.moveTo(pos[0], pos[1])
        mouse.click()
    else:
        print("Bitmap not found")
        if (tolerance < 0.8):
            print("Increasing tolerance by 0.1")
            move(needle, dir, tolerance + 0.1)


# move(left)
# move(up, 1, 0.6)
# move(up, 1, 0.6)
move(down, 3)
move(left)
move(up, 1)
move(right, 2)
