import random

# Set up maze dimensions
ROWS = 80
COLS = 80

# Function to initialize the maze with walls
def initialize_maze():
    maze = [[1] * COLS for _ in range(ROWS)]
    return maze

# Recursive Backtracking Algorithm to generate the maze
def generate_maze(maze, row, col):
    maze[row][col] = 0  # Mark the current cell as open

    # Define the order in which directions will be checked
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    random.shuffle(directions)

    for dr, dc in directions:
        new_row, new_col = row + 2 * dr, col + 2 * dc
        if 0 <= new_row < ROWS and 0 <= new_col < COLS and maze[new_row][new_col] == 1:
            maze[row + dr][col + dc] = 0  # Mark the cell between the current and next cell as open
            generate_maze(maze, new_row, new_col)

# Function to print the maze
def print_maze(maze):
    for row in maze:
        print(' '.join(['#' if cell == 1 else ' ' for cell in row]))

# Main function to generate and print the maze
def main():
    maze = initialize_maze()
    generate_maze(maze, 1, 1)
    print_maze(maze)

if __name__ == "__main__":
    main()