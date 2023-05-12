"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

# Libraries
from random import randrange
from turtle import *

from freegames import square, vector

# Variables
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors_value = randrange(1, 6)
snake_value = randrange(1, 6)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


# When we initialize the game, this will define the color of our food depending on the variable "colors_value", which is random.
def food_change():
    if colors_value == 1:
        square(food.x, food.y, 9, 'green')  # Green food!
    elif colors_value == 2:
        square(food.x, food.y, 9, 'blue')  # Blue food!
    elif colors_value == 3:
        square(food.x, food.y, 9, 'orange')  # Orange food!
    elif colors_value == 4:
        square(food.x, food.y, 9, 'purple')  # Purple food!
    elif colors_value == 5:
        square(food.x, food.y, 9, 'pink')  # Pink food!

# When we initialize the game, this will define the color of our food depending on the variable "snake_value", which is random.
def snake_change(body):
    if snake_value == 1:
        square(body.x, body.y, 9, 'coral')  # Coral snake!
    elif snake_value == 2:
        square(body.x, body.y, 9, 'black')  # Black snake!
    elif snake_value == 3:
        square(body.x, body.y, 9, 'teal')  # Teal snake!
    elif snake_value == 4:
        square(body.x, body.y, 9, 'tan')  # Tan snake!
    elif snake_value == 5:
        square(body.x, body.y, 9, 'hotpink')  # Hot pink snake!


# Will define our game space, which is 200 x 200.
def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    # This will end the game when the snake hits a wall.
    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    # This will create new food on the map.
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    # Defining the body of our snake, in position and in color.
    for body in snake:
        snake_change(body)

    # Defining the food in our map, in position and in color.
    food_change()
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
