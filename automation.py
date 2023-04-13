animations = {}

directions = [
    'up',
    'down',
    'left',
    'right'
]

states = [
    '',
    'idle',
    'hoe',
    'axe',
    'water'
]

for state in states:
    for direction in directions:
        newstate = direction + (f'_{state}' if state else '')
        animations[newstate] = []

print(animations)