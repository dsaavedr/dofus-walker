from autopy import mouse
from time import sleep


class BetterMouse():
    vel = 1
    slp = 0.001

    def __init__(self):
        self.update()

    def moveTo(self, x, y):
        # Copy curr coordinates
        nx = self.locX
        ny = self.locY
        # Get slope of straight line
        dx = x - nx
        dy = y - ny

        s = dy
        if dx != 0:
            s = round(abs(dy/dx), 2)
        print(f"Moving in straight line with slope: {s}")
        c = 0
        while self.locX != x:
            if dx > 0:
                if dy > 0:
                    nx += self.vel
                    ny += s * self.vel
                    mouse.move(nx, ny)
                else:
                    nx += self.vel
                    ny -= s * self.vel
                    mouse.move(nx, ny)
            else:
                if dy > 0:
                    nx -= self.vel
                    ny += s * self.vel
                    mouse.move(nx, ny)
                else:
                    nx -= self.vel
                    ny -= s * self.vel
                    mouse.move(nx, ny)
            c += 1
            if c % 10 == 0:
                sleep(self.slp)
            self.update()
        print("Done!")
        print(s)
        print(self.location())

    def location(self):
        return mouse.location()

    def move(self, x, y):
        return mouse.move(x, y)

    def update(self):
        x, y = self.location()
        self.locX = x
        self.locY = y
