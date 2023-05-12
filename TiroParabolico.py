"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.
"""

# Libraries
from random import randrange
from turtle import *

from freegames import vector

# Variables
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []


def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 400) / 25


def inside(xy):
    """Return True if xy within screen."""
    # Our screen is 200 x 200, so in order to make our vanish effect to make an infinite game, we just add 20 more at x.
    return -220 < xy.x < 220 and -200 < xy.y < 200


def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')  # Will create a blue ball for targets.

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')  # Will create a red ball for bullets.

    update()


def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 2

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # When target isn't at the screen, reappear the target on the other side instead of ending.
    for target in targets:
        if not inside(target):
            target.x = 220

    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
