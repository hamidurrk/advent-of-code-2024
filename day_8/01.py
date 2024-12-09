def parse_map(input_map):
    """
    Parse the input map to extract positions and frequencies of antennas.

    Args:
        input_map (list[str]): The map of the antennas as a list of strings.

    Returns:
        dict: A dictionary mapping each frequency to a list of (x, y) positions.
    """
    antennas = {}
    for y, row in enumerate(input_map):
        for x, char in enumerate(row):
            if char.isalnum():
                antennas.setdefault(char, []).append((x, y))
    return antennas

def calculate_antinodes(antennas, map_size):
    """Calculate antinodes based on antenna positions and frequencies."""
    antinodes = set()
    for freq, positions in antennas.items():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                print(x1, y1, x2, y2)
                
                # Calculate potential antinode positions
                
                mid_row1 = x1 - (x2 - x1)
                mid_col1 = y1 - (y2 - y1)
                mid_row2 = x2 + (x2 - x1)
                mid_col2 = y2 + (y2 - y1)
                # Check bounds for antinode positions
                if 0 <= mid_row1 < map_size[0] and 0 <= mid_col1 < map_size[1]:
                    print(mid_row1, mid_col1)
                    antinodes.add((mid_row1, mid_col1))
                if 0 <= mid_row2 < map_size[0] and 0 <= mid_col2 < map_size[1]:
                    print(mid_row2, mid_col2)
                    antinodes.add((mid_row2, mid_col2))

    return antinodes
def count_unique_antinodes(input_map):
    """Main function to count unique antinodes on the map."""
    antennas = parse_map(input_map)
    map_size = (len(input_map), len(input_map[0]))
    antinodes = calculate_antinodes(antennas, map_size)
    print(antinodes)

    return len(antinodes)

with open('day_8/01_ex.txt') as f:
    input_map = f.read().splitlines()

# Calculate and print the number of unique antinode locations
result = count_unique_antinodes(input_map)
print("Number of unique antinode locations:", result)

    
# print_new_map(input_map)