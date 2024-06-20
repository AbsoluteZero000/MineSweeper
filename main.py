import random

class MineSweeper:
    def __init__(self, x, y, bombs):
        self.x = x
        self.y = y
        self.bombs = bombs
        self.ms_map = [['N' for _ in range(x)] for _ in range(y)]
        for i in range(bombs):
            while True:
                rand_x = random.randint(0, x-1)
                rand_y = random.randint(0, y-1)
                if self.ms_map[rand_y][rand_x] != 'B':
                    self.ms_map[rand_y][rand_x] = 'B'
                    break
        for i in range(x):
            for j in range(y):
                if(self.ms_map[i][j] != 'B'):
                    self.ms_map[i][j] = self.countBombs(i,j)

    def countBombs(self, x, y):
        count = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if i >= 0 and i < self.x and j >= 0 and j < self.y and self.ms_map[i][j] == 'B':
                    count += 1
        return count

    def printMap(self):
        for i in self.ms_map:
            for j in i:
                print(j, end=' ')
            print()

x = int(input("enter the width of the map (min 5): "))
y = int(input("enter the height of the map (min 5): "))
bombs = int(input("enter the number of bombs (min 1): "))
ms = MineSweeper(x, y, bombs)

ms.printMap()
