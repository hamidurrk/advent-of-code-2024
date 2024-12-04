def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    count = 0

    for r in range(rows):
        for c in range(cols - word_len + 1):
            if grid[r][c:c + word_len] == word:
                count += 1
            if grid[r][c:c + word_len][::-1] == word:
                count += 1

    for c in range(cols):
        for r in range(rows - word_len + 1):
            vertical_word = ''.join(grid[r + i][c] for i in range(word_len))
            if vertical_word == word:
                count += 1
            if vertical_word[::-1] == word:
                count += 1

    for r in range(rows - word_len + 1):
        for c in range(cols - word_len + 1):
            diagonal_word = ''.join(grid[r + i][c + i] for i in range(word_len))
            if diagonal_word == word:
                count += 1
            if diagonal_word[::-1] == word:
                count += 1

    for r in range(rows - word_len + 1):
        for c in range(word_len - 1, cols):
            diagonal_word = ''.join(grid[r + i][c - i] for i in range(word_len))
            if diagonal_word == word:
                count += 1
            if diagonal_word[::-1] == word:
                count += 1

    return count

file_name = 'day_4/01.txt'

with open(file_name) as f:
    grid = [line.strip() for line in f.readlines()]
word = "XMAS"
count = count_word_occurrences(grid, word)

print(f"Occurrences of the word '{word}': {count}")