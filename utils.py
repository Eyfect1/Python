from random import randint as rand

def probability_check(chance_value, max_chance):
    return rand(0, max_chance) <= chance_value

def get_random_cell(width, height):
    return (rand(0, height - 1), rand(0, width - 1))

def get_adjacent_cell(x_pos, y_pos):
    movement_options = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = rand(0, 3)
    dx, dy = movement_options[direction]
    return (x_pos + dx, y_pos + dy)