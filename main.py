"""
 This program simulates gravity acting on a ball.

 The ball starts off with a random velocity in the x
 direction, and 0 velocity in the y direction.

 With each tick in time, gravity increases the y velocity
 so that the ball is falling faster toward the ground.

 Try playing around with the GRAVITY_ACCELERATION constant
 to see what the ball bounces like with stronger and weaker
 gravitational force!
"""
import platform
import sys
#
import tkinter
from tkinter import *
import random
import time

from settings import Settings

settings = Settings(2.0 / 3.0)
print(f'{settings=}')

BALL_DIAMETER = settings.scaled_height * 0.10  # 50
STARTING_Y = 50
STARTING_X = 50
GRAVITY_ACCELERATION = 4
ANIMATION_DELAY = 0.050


def center_window(window):
    window.update_idletasks()
    print(f'{window.winfo_width()=}, {window.winfo_height()=}')
    print(f'{window.winfo_screenwidth()=}, {window.winfo_screenheight()=}')
    width = settings.scaled_width  # window.winfo_width()
    height = settings.scaled_height  # window.winfo_height()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    print(f'{screen_width=}, {screen_height=}')
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window_geometry = f'{width}x{height}+{x}+{y}'
    print(f'{window_geometry=}')
    window.geometry(window_geometry)


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_tkinter_version() -> str:
    return f'{tkinter.TkVersion}'


root: tkinter.Tk = Tk()
# print(f'{type(root)=}')
title = f'Gravity Simulation using Python {get_python_version()} and Tkinter {get_tkinter_version()}'
root.title(title)
center_window(root)
screen = Canvas(root, width = settings.scaled_width, height = settings.scaled_height, background = "white")
screen.pack()

# Create Ball
ball = screen.create_oval(STARTING_X, STARTING_Y,
                          STARTING_X + BALL_DIAMETER, STARTING_Y + BALL_DIAMETER, fill = "black")

# Initializes the velocity for the ball
velocity_x = random.uniform(1, 5)
velocity_y = 0


def check_for_bounce():
    """If the ball is going off the screen, this function bounces the ball back into the canvas."""
    global velocity_x, velocity_y
    # Returns x1, y1, x2, y2
    ball_pos = screen.coords(ball)
    if ball_pos[2] >= settings.scaled_width:
        velocity_x *= -1
        screen.coords(ball, settings.scaled_width - BALL_DIAMETER, ball_pos[1],
                      settings.scaled_width, ball_pos[3])
    if ball_pos[0] <= 0:
        velocity_x *= -1
        screen.coords(ball, 0, ball_pos[1],
                      BALL_DIAMETER, ball_pos[3])
    if ball_pos[3] >= settings.scaled_height:
        velocity_y = -1 * abs(velocity_y)
        screen.coords(ball, ball_pos[0], settings.scaled_height - BALL_DIAMETER,
                      ball_pos[2], settings.scaled_height)

    if ball_pos[1] <= 0:
        velocity_y *= -1
        screen.coords(ball, ball_pos[0], 0,
                      ball_pos[2], BALL_DIAMETER)
    screen.update()


# Represents one moment in time passing. Moves the ball
# according to the current velocity, and adds the gravity
# acceleration to the y velocity.

def move_ball():
    global velocity_x, velocity_y
    screen.move(ball, velocity_x, velocity_y)
    check_for_bounce()
    velocity_y += GRAVITY_ACCELERATION


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_tkinter_version() -> str:
    return f'{tkinter.TkVersion}'


def main():
    msg = f'Python version: {get_python_version()} on {platform.system()} {platform.release()}'
    print(msg)

    msg = f'Tkinter version: {get_tkinter_version()}'
    print(msg)

    while True:
        move_ball()
        screen.update()
        time.sleep(ANIMATION_DELAY)

    mainloop()


if __name__ == '__main__':
    main()
