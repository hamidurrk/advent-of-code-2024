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
    """
    Calculate antinode locations based on antenna positions and frequencies.

    Args:
        antennas (dict): A dictionary of frequencies and their antenna positions.
        map_size (tuple): Size of the map as (rows, columns).

    Returns:
        set: A set of unique (x, y) antinode positions.
    """
    antinodes = set()

    for freq, positions in antennas.items():
        n = len(positions)

        # Add all antennas themselves as antinodes if there's more than one of the same frequency
        if n > 1:
            antinodes.update(positions)

        # Find all other antinode positions along lines formed by each pair of antennas
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                # Iterate along the line between the two antennas
                dx, dy = x2 - x1, y2 - y1
                gcd = abs(__import__('math').gcd(dx, dy))  # Normalize step
                dx //= gcd
                dy //= gcd

                # Generate antinodes in both directions
                x, y = x1, y1
                while 0 <= x < map_size[1] and 0 <= y < map_size[0]:
                    antinodes.add((x, y))
                    x -= dx
                    y -= dy

                x, y = x2, y2
                while 0 <= x < map_size[1] and 0 <= y < map_size[0]:
                    antinodes.add((x, y))
                    x += dx
                    y += dy

    return antinodes

def count_unique_antinodes(input_map):
    """
    Count the number of unique antinode locations on the map.

    Args:
        input_map (list[str]): The map of the antennas as a list of strings.

    Returns:
        int: The number of unique antinode locations.
    """
    antennas = parse_map(input_map)
    map_size = (len(input_map), len(input_map[0]))
    antinodes = calculate_antinodes(antennas, map_size)
    return len(antinodes)

# Load the input map
with open('day_8/01.txt') as f:
    input_map = f.read().splitlines()

# Calculate and print the number of unique antinode locations
result = count_unique_antinodes(input_map)
print("Number of unique antinode locations:", result)
