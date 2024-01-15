import numpy as np


# Function to move the drones
def move_drone(drone_pos, direction, steps):
    new_pos = drone_pos.copy()
    if direction.lower().startswith('u'):
        new_pos[1] += steps
    elif direction.lower().startswith('d'):
        new_pos[1] -= steps
    elif direction.lower().startswith('l'):
        new_pos[0] -= steps
    elif direction.lower().startswith('r'):
        new_pos[0] += steps
    return new_pos


# Generate a list of all positions for the animation for each drone
def generate_path(start, instructions, res):
    drone_positions = [drone_pos for drone_pos, _ in start]
    all_positions = []
    for i in range(len(drone_positions)):
        positions = [drone_positions[i]]
        for instruction in instructions[i]:
            direction, steps = instruction
            for _ in range(steps*res):
                drone_positions[i] = move_drone(drone_positions[i], direction, 1/res)
                positions.append(drone_positions[i].copy())
        all_positions.append(positions)

    return all_positions


def sample(start, res):
    # Define the instructions
    instructions = [
        [('', 0)] + [('right', 20)] * 3 + [('up', 20)] * 4 + [('left', 20)] + [('down', 20)] * 2,
        [('', 0)] + [('left', 20)] * 3 + [('down', 20)] * 4 + [('right', 20)] + [('up', 20)] * 2
    ]

    return generate_path(start, instructions, res)


def my20x20path(start, res):
    instructions = [
        'rrrurrurrurrrurrrurrrrurrdldlllldllldllldrdlluldllrrrrrrurrurrrurrrruddllldllldlllrrrrrrrrrull                 ',
        'dluldluldluurulldluldllurulluulrrdrurddrrrrrddrrrulluulllllurrrrrrrddlu                                        ',
        'llldlllldllluuuuuuulddddddddrlluuuuuuuuurrrdddddddrurrrrurrrruuuulllllluulllrddddddrrrurrrruulllllluuddddrurrrr',
        'dddrrurddruurdddldrruuurddrrluululullllldddrdrddrrrdddddddddlldlldllururrurruuuuuuullluu                       ',

    ]

    return generate_path(start, [[('', 0)] + [(i, 1) for i in instruction] for instruction in instructions], res)


def basic_algo(grid_size, start, res):
    instructions = [
        ('u' * grid_size + 'r' + 'd' * grid_size + 'r') * (grid_size // (2 * len(start))) + 'u' * grid_size,
        ('d' * grid_size + 'r' + 'u' * grid_size + 'r') * (grid_size // (2 * len(start))) + 'd' * grid_size
        # ('d' * grid_size + 'r' + 'u' * grid_size + 'r') * (grid_size // (2 * len(start))) + 'd' * (grid_size // 2) + ' ' * ((grid_size + 1) // 2),
        # ('u' * grid_size + 'l' + 'd' * grid_size + 'l') * (grid_size // (2 * len(start))) + 'u' * (grid_size // 2) + ' ' * ((grid_size + 1) // 2)

    ] * 2

    return generate_path(start, [[('', 0)] + [(i, 1) for i in instruction] for instruction in instructions], res)

def paper_algo(probabilities, start, res):
    return

def other_algo(probabiltiies, start, res):
    return