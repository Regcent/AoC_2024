import time
from typing import Union
from copy import deepcopy
from enum import Enum
from queue import PriorityQueue

class Dir(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

    def __lt__(self, b):
        return self.value < b.value

def run_script(filepath: str) -> Union[int, str, float, bool]:
    with open(filepath, "r") as f:
        raw_data = f.read()
    return main_function(raw_data)

def main_function(raw_data: str) -> Union[int, str, float, bool]:
    start_time = time.time()
    
    result = your_script(raw_data)

    elapsed_time = time.time() - start_time
    print(f"Time elapsed : {elapsed_time}s")
    return result

def your_script(raw_data: str) -> Union[int, str, float, bool]:
    """
    Time to code! Write your code here to solve today's problem
    """
    print("Coucou")
    lines = raw_data.split("\n")
    grid = []
    for y in range(len(lines)):
        row = []
        for x in range(len(lines[y])):
            if lines[y][x] == ".":
                row.append(True)
            elif lines[y][x] == "S":
                row.append(True)
                start = (x, y, Dir.EAST)
            elif lines[y][x] == "E":
                row.append(True)
                end = (x, y)
            else:
                row.append(False)
        grid.append(deepcopy(row))
    print(f"Part 1: {part_1(grid, start, end)}")
    return 0

def part_1(grid: list, start: tuple, end: tuple) -> None:
    pq = PriorityQueue()
    pq.put((0, start))
    explored = set()
    explored.add((start[0], start[1]))
    while True:
        curr = pq.get()
        score = curr[0]
        (x, y, direction) = curr[1]
        explored.add((x, y))
        if (x, y) == end:
            return score
        if direction == Dir.NORTH:
            if grid[y - 1][x] and (x, y - 1) not in explored:
                pq.put((score + 1, (x, y - 1, Dir.NORTH)))
            if grid[y][x + 1] and (x + 1, y) not in explored:
                pq.put((score + 1001, (x + 1, y, Dir.EAST)))
            if grid[y][x - 1] and (x - 1, y) not in explored:
                pq.put((score + 1001, (x - 1, y, Dir.WEST)))
        if direction == Dir.EAST:
            if grid[y][x + 1] and (x + 1, y) not in explored:
                pq.put((score + 1, (x + 1, y, Dir.EAST)))
            if grid[y - 1][x] and (x, y - 1) not in explored:
                pq.put((score + 1001, (x, y - 1, Dir.NORTH)))
            if grid[y + 1][x] and (x, y + 1) not in explored:
                pq.put((score + 1001, (x, y + 1, Dir.SOUTH)))
        if direction == Dir.SOUTH:
            if grid[y + 1][x] and (x, y + 1) not in explored:
                pq.put((score + 1, (x, y + 1, Dir.SOUTH)))
            if grid[y][x + 1] and (x + 1, y) not in explored:
                pq.put((score + 1001, (x + 1, y, Dir.EAST)))
            if grid[y][x - 1] and (x - 1, y) not in explored:
                pq.put((score + 1001, (x - 1, y, Dir.WEST)))
        if direction == Dir.WEST:
            if grid[y][x - 1] and (x - 1, y) not in explored:
                pq.put((score + 1, (x - 1, y, Dir.WEST)))
            if grid[y - 1][x] and (x, y - 1) not in explored:
                pq.put((score + 1001, (x, y - 1, Dir.NORTH)))
            if grid[y + 1][x] and (x, y + 1) not in explored:
                pq.put((score + 1001, (x, y + 1, Dir.SOUTH)))

if __name__ == "__main__":
    print(run_script("input.txt"))