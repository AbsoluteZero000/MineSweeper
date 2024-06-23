import random

class MineSweeper:
    def __init__(self, width, height, num_bombs):
        self.width = width
        self.height = height
        self.num_bombs = num_bombs
        self.grid = [[' ' for _ in range(width)] for _ in range(height)]
        self.player_grid = [['X' for _ in range(width)] for _ in range(height)]

    def _place_bombs(self, x, y):
        placed_bombs = 0
        while placed_bombs < self.num_bombs:
            rand_x = random.randint(0, self.width - 1)
            rand_y = random.randint(0, self.height - 1)
            if self.grid[rand_y][rand_x] != 'B' and (rand_x != x and rand_y != y):
                self.grid[rand_y][rand_x] = 'B'
                placed_bombs += 1

    def _calculate_adjacent_bombs(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[y][x] != 'B':
                    self.grid[y][x] = self._count_adjacent_bombs(x, y)

    def _count_adjacent_bombs(self, x, y):
        count = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.grid[ny][nx] == 'B':
                    count += 1
        return count

    def _reveal_adjacent_cells(self, x, y):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.player_grid[ny][nx] == 'X' and self.grid[ny][nx] != 'B':
                    self.player_grid[ny][nx] = self.grid[ny][nx]
                    if self.grid[ny][nx] == 0:
                        self._reveal_adjacent_cells(nx, ny)

    def display_grid(self):
        for row in self.player_grid:
            print(' '.join(str(cell) for cell in row))
    def display_final_map(self):
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))
    def _win(self):
        cnt = 0
        for row in self.player_grid:
            if 'X' in row:
                cnt+=1
        return cnt == self.num_bombs
    def game_loop(self):
        self.display_grid()

        x = get_valid_input("Enter the x-coordinate: ", 0, self.width - 1)
        y = get_valid_input("Enter the y-coordinate: ", 0, self.height - 1)
        self._place_bombs(x, y)
        self._calculate_adjacent_bombs()
        self._reveal_adjacent_cells(x, y)
        self.display_grid()


        while True:
            x = get_valid_input("Enter the x-coordinate: ", 0, self.width - 1)
            y = get_valid_input("Enter the y-coordinate: ", 0, self.height - 1)

            if self.grid[y][x] == 'B':
                print("YOU LOSE!")
                self.display_final_map()
                return
            self._reveal_adjacent_cells(x, y)
            self.display_grid()
            if(self._win()):
                print("YOU WIN!")
                self.display_final_map()
                return

def get_valid_input(prompt, min_value, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                print(f"Please enter a value greater than or equal to {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Please enter a value less than or equal to {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

width = get_valid_input("Enter the width of the map (min 5): ", 5)
height = get_valid_input("Enter the height of the map (min 5): ", 5)
num_bombs = get_valid_input(f"Enter the number of bombs (min 1, max({width*height-1}): ", 1)
ms = MineSweeper(width, height, num_bombs)

ms.game_loop()
