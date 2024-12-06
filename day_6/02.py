import time

MAX_COUNT = 1000
DIRECTIONS = ['^', 'v', '<', '>']
MOVES = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}
TURN = {
    '^': '>',
    'v': '<',
    '<': '^',
    '>': 'v'
}


def read_input(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]


def find_start_position(data):
    for r, row in enumerate(data):
        for c, cell in enumerate(row):
            if cell in DIRECTIONS:
                return (r, c), cell
    return None, None


def move(data, start_position, start_direction):
    visited = []
    current_position = list(start_position)
    current_direction = start_direction

    while True:
        if current_position[0] < 0 or current_position[1] < 0 or \
           current_position[0] >= len(data) or current_position[1] >= len(data[0]):
            break

        visited.append(tuple(current_position))
        move_delta = MOVES[current_direction]
        next_position = [current_position[0] + move_delta[0], current_position[1] + move_delta[1]]

        if 0 <= next_position[0] < len(data) and 0 <= next_position[1] < len(data[0]) and \
           data[next_position[0]][next_position[1]] == '#':
            current_direction = TURN[current_direction]
        else:
            current_position = next_position

    return visited


def count_paradoxes(data, visited, start_position, start_direction):
    paradox_count = 0
    paradox_positions = []

    for obstacle in visited:
        grid_copy = [row[:] for row in data]
        grid_copy[obstacle[0]][obstacle[1]] = '#'

        visited_states = set()
        current_position = list(start_position)
        current_direction = start_direction
        count = 0

        while True:
            if current_position[0] < 0 or current_position[1] < 0 or \
               current_position[0] >= len(grid_copy) or current_position[1] >= len(grid_copy[0]):
                break

            state = (current_position[0], current_position[1], current_direction)
            if state in visited_states:
                count += 1
                if count > MAX_COUNT:
                    paradox_count += 1
                    paradox_positions.append(obstacle)
                    break
            else:
                visited_states.add(state)

            move_delta = MOVES[current_direction]
            next_position = [current_position[0] + move_delta[0], current_position[1] + move_delta[1]]

            if 0 <= next_position[0] < len(grid_copy) and 0 <= next_position[1] < len(grid_copy[0]) and \
               grid_copy[next_position[0]][next_position[1]] == '#':
                current_direction = TURN[current_direction]
            else:
                current_position = next_position

    return paradox_count, paradox_positions


def main():
    data = read_input('day_6/01.txt')
    start_position, start_direction = find_start_position(data)

    if not start_position or not start_direction:
        print("No starting point or direction found.")
        return

    visited = move(data, start_position, start_direction)
    visited = list(set(visited))  
    
    start_time = time.time()
    paradox_count, paradox_positions = count_paradoxes(data, visited, start_position, start_direction)
    end_time = time.time()

    print(f'Time taken: {(end_time - start_time):.4f} seconds.')
    print(f'There are {paradox_count} ways to get paradoxes.')


if __name__ == "__main__":
    main()
