import numpy as np

def count_xmas_occurrences(grid):
    matrix = np.array(grid)
    rows, cols = matrix.shape

    submatrices = []
    count = 0
    for r in range(rows - 2):
        for c in range(cols - 2):
            submatrix = matrix[r:r+3, c:c+3]
            submatrices.append(submatrix)

    for i, submatrix in enumerate(submatrices):
        submatrix = np.delete(submatrix, (1, 3, 5, 7))
        if np.array_equal(submatrix, np.array(['M', 'S', 'A', 'M', 'S'])) or np.array_equal(submatrix, np.array(['S', 'M', 'A', 'S', 'M'])) or np.array_equal(submatrix, np.array(['S', 'S', 'A', 'M', 'M']))  or np.array_equal(submatrix, np.array(['M', 'M', 'A', 'S', 'S'])):
            print(f"Submatrix {i+1}:\n{submatrix}\n")
            count += 1
    print(count)

file_name = 'day_4/01.txt'

with open(file_name) as f:
    grid = [[x for x in line.strip()] for line in f.readlines()]
count_xmas_occurrences(grid)
