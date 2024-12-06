import sys, time

def get_position(maze, char):
    for i, row in enumerate(maze):
        if char in row:
            return (i, row.index(char)) 

def get_char(maze, position):
    return maze[position[0]][position[1]]

def count_char(maze, char):
    count = 0
    for row in maze:
        count += row.count(char)
    return count

def get_direction(maze):
    for row in maze:
        if '^' in row:
            return '^'
        if 'v' in row:
            return 'v'
        if '<' in row:
            return '<'
        if '>' in row:
            return '>'

def assign_char(maze, position, char):
    for i, row in enumerate(maze):
        if i == position[0]:
            row = list(row)
            row[position[1]] = char
            maze[i] = ''.join(row)
            
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

def turn_right(maze):
    direction = get_direction(maze)
    if direction == '^':
        assign_char(maze, get_position(maze, '^'), '>')
    elif direction == 'v':
        assign_char(maze, get_position(maze, 'v'), '<')
    elif direction == '<':
        assign_char(maze, get_position(maze, '<'), '^')
    elif direction == '>':
        assign_char(maze, get_position(maze, '>'), 'v')
    
def go_forward(maze, will_print=True):
    not_x = True
    end_loop = False
    while True:
        if will_print:
            print_maze(maze)
        direction = get_direction(maze)
        pos = get_position(maze, direction)
        try:
            if direction == '^' and check_forward(maze, '^'):
                assign_char(maze, pos, '.' if not_x else 'X')
                pos = (pos[0] - 1, pos[1])
                assign_char(maze, pos, '^')
            elif direction == 'v' and check_forward(maze, 'v'):
                assign_char(maze, pos, '.' if not_x else 'X')
                pos = (pos[0] + 1, pos[1])
                assign_char(maze, pos, 'v')
            elif direction == '<' and check_forward(maze, '<'):
                assign_char(maze, pos, '.' if not_x else 'X')
                pos = (pos[0], pos[1] - 1)
                assign_char(maze, pos, '<')
            elif direction == '>' and check_forward(maze, '>'):
                assign_char(maze, pos, '.' if not_x else 'X')
                pos = (pos[0], pos[1] + 1)
                assign_char(maze, pos, '>')
            else:
                turn_right(maze)
        except IndexError:
            direction = get_direction(maze)
            pos = get_position(maze, direction)
            assign_char(maze, pos, '.' if not_x else 'X')
            end_loop = True
            
        time.sleep(0.5)
        if will_print:
            clear_last_lines(len(maze))
        if end_loop:
            print_maze(maze)
            break
    
def print_maze(maze):
    for row in maze:
        print(row)
        
def clear_last_lines(x):
    for _ in range(x):
        sys.stdout.write("\033[F")  
        sys.stdout.write("\033[K")  
        
def main():
    with open('day_6/01_ex.txt') as f:
        maze = f.read().splitlines()
    go_forward(maze, will_print=True)
    num_of_x = count_char(maze, 'X')
    print(f'Number of X: {num_of_x}')

main()