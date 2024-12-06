def get_position(maze, direction):
    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char in '^v<>':
                return (i, j)
    return None

def get_direction(maze):
    for row in maze:
        for char in row:
            if char in '^v<>':
                return char
    return None

def assign_char(maze, position, char):
    row, col = position
    maze[row] = maze[row][:col] + char + maze[row][col + 1:]

def check_forward(maze, direction):
    pos = get_position(maze, direction)
    if pos[0] > len(maze) - 1 or pos[1] > len(maze[0]) - 1:
        return False
    if direction == '^':
        if get_char(maze, (pos[0] - 1, pos[1])) == '#':
            return False
    elif direction == 'v':
        if get_char(maze, (pos[0] + 1, pos[1])) == '#':
            return False
    elif direction == '<':
        if get_char(maze, (pos[0], pos[1] - 1)) == '#':
            return False
    elif direction == '>':
        if get_char(maze, (pos[0], pos[1] + 1)) == '#':
            return False
    return True

def get_char(maze, position):
    row, col = position
    return maze[row][col]

def turn_right(direction):
    if direction == '^':
        return '>'
    elif direction == '>':
        return 'v'
    elif direction == 'v':
        return '<'
    elif direction == '<':
        return '^'

def patrol(maze):
    direction = get_direction(maze)
    pos = get_position(maze, direction)
    visited_positions = set()
    visited_positions.add(pos)

    while True:
        try:
            if not check_forward(maze, direction):
                direction = turn_right(direction)
                assign_char(maze, pos, direction)
            else:
                assign_char(maze, pos, 'X')
                if direction == '^':
                    pos = (pos[0] - 1, pos[1])
                elif direction == 'v':
                    pos = (pos[0] + 1, pos[1])
                elif direction == '<':
                    pos = (pos[0], pos[1] - 1)
                elif direction == '>':
                    pos = (pos[0], pos[1] + 1)
                if pos[0] < 0 or pos[0] >= len(maze) or pos[1] < 0 or pos[1] >= len(maze[0]):
                    break
                visited_positions.add(pos)
                assign_char(maze, pos, direction)
        except:
            break

    return visited_positions

def print_maze(maze):
    for row in maze:
        print(row)

file_name = 'day_6/01_ex.txt'

with open(file_name) as f:
    maze = [line.strip() for line in f.readlines()]

visited_positions = patrol(maze)
print_maze(maze)
print(f"Number of distinct positions visited: {len(visited_positions)}")