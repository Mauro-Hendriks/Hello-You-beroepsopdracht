from microbit import *
from random import randint

SCENE_WIDTH = 4
INITIAL_DELAY = 500

POSSIBLE_ROADSIDE_ROWS = [
    [
        False,
        False,
        True,
        True,
        True,
    ],
    [
        True,
        False,
        False,
        True,
        True,
    ],
    [
        True,
        True,
        False,
        False,
        True,
    ],
    [
        True,
        True,
        True,
        False,
        False,
    ],
]

roadside_row_indices = None
car_x = None
time_of_last_advance = None
time_of_last_move = None
time_of_last_speedup = None
delay = None


def init():
    global roadside_row_indices
    global car_x
    global time_of_last_advance
    global time_of_last_move, time_of_last_speedup, delay
    roadside_row_indices = [2, 2, 2, 2, 2]
    car_x = 2
    time_of_last_advance = None
    time_of_last_move = None
    time_of_last_speedup = None
    delay = INITIAL_DELAY
    button_a.was_pressed()
    button_b.was_pressed()


def did_detect_collision_while_drawing_scene():
    has_collided = False
    car_y = 3
    display.set_pixel(car_x, car_y, 9)
    sleep(20)
    display.set_pixel(car_x, car_y, 5)
    for y, state_index in enumerate(roadside_row_indices):
        row = POSSIBLE_ROADSIDE_ROWS[state_index]
        for x, px in enumerate(row):
            if x == car_x and y == car_y:
                has_collided = px
            else:
                display.set_pixel(x, y, 6 if px else 0)
    return has_collided


def roadside_row_indices_by_scrolling():
    next_state_index = roadside_row_indices[0] + randint(-1, 1)
    if next_state_index == -1 or next_state_index == len(POSSIBLE_ROADSIDE_ROWS):
        return roadside_row_indices
    new_roadside = roadside_row_indices[:-1]
    new_roadside.insert(0, next_state_index)
    return new_roadside


def car_x_by_detecting_inputs():
    direction = 0
    if button_a.was_pressed():
        direction -= 1
    if button_b.was_pressed():
        direction += 1
    return max(min(car_x + direction, SCENE_WIDTH), 0)


init()

while True:

    now = running_time()
    if time_of_last_advance == None:
        time_of_last_advance = now
    if time_of_last_move == None:
        time_of_last_move = now
    if time_of_last_speedup == None:
        time_of_last_speedup = now

    if now - time_of_last_move >= 100:
        car_x = car_x_by_detecting_inputs()
        time_of_last_move = now
    if now - time_of_last_advance >= delay:
        roadside_row_indices = roadside_row_indices_by_scrolling()
        time_of_last_advance = now
    if now - time_of_last_speedup >= 1000:
        delay -= 10
        time_of_last_speedup = now
    collided = did_detect_collision_while_drawing_scene()
    if collided:
        score = INITIAL_DELAY - delay
        display.scroll("Game Over", delay=100, wait=True, loop=False)
        display.scroll(str(score), delay=150, wait=True, loop=False)
        init()
