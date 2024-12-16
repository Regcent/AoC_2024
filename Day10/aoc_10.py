import time
from typing import Union

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
    raw_grid = raw_data.split("\n")
    zeros = list()
    grid = list()
    for y in range(len(raw_grid)):
        row = list()
        for x in range(len(raw_grid[y])):
            row.append(int(raw_grid[y][x]))
            if raw_grid[y][x] == "0":
                zeros.append((x, y))
        grid.append(row)
    part_1(grid, zeros)
    part_2(grid, zeros)
    return 0

def part_1(grid: list, zeros: list):
    total = 0
    for zero in zeros:
        total += calculate_score(zero, grid)
    print(f"Part 1: {total}")

def calculate_score(zero: tuple, grid: list) -> int:
    current = [zero]
    explored = set()
    explored.add(zero)
    score = 0
    while current:
        pos = current.pop(0)
        if grid[pos[1]][pos[0]] == 9:
            score += 1
        for neighbor in neighbors(pos[0], pos[1], len(grid[0]) - 1, len(grid) - 1):
            if neighbor in explored:
                continue
            if grid[pos[1]][pos[0]] + 1 == grid[neighbor[1]][neighbor[0]]:
                current.append(neighbor)
                explored.add(neighbor)
    return score

def part_2(grid: list, zeros: list):
    total = 0
    for zero in zeros:
        total += calculate_rating(zero, grid)
    print(f"Part 2: {total}")

def calculate_rating(zero: tuple, grid: list) -> int:
    current = [zero]
    score = 0
    while current:
        pos = current.pop(0)
        if grid[pos[1]][pos[0]] == 9:
            score += 1
        for neighbor in neighbors(pos[0], pos[1], len(grid[0]) - 1, len(grid) - 1):
            if grid[pos[1]][pos[0]] + 1 == grid[neighbor[1]][neighbor[0]]:
                current.append(neighbor)
    return score

def neighbors(x: int, y: int, max_x: int, max_y: int)-> list:
    neighbors = list()
    if x > 0:
        neighbors.append((x - 1,y))
    if x < max_x:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < max_y:
        neighbors.append((x, y + 1))
    return neighbors

if __name__ == "__main__":
    print(run_script("input.txt"))