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
    grid = raw_data.split("\n")
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != "X":
                continue
            count = 0
            count += check_r(grid, x, y)
            count += check_tr(grid, x, y)
            count += check_t(grid, x, y)
            count += check_tl(grid, x, y)
            count += check_l(grid, x, y)
            count += check_bl(grid, x, y)
            count += check_b(grid, x, y)
            count += check_br(grid, x, y)
            total += count
    print(f"Part 1: {total}")
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != "A":
                continue
            count = 0
            #count += check_plus(grid, x, y)
            count += check_cross(grid, x, y)
            total += count
    print(f"Part 2: {total}")

def check_r(grid: list, x: int, y: int):
    if len(grid[y]) - x - 3 <= 0:
        return 0
    if grid[y][x+1] != "M":
        return 0
    if grid[y][x+2] != "A":
        return 0
    if grid[y][x+3] != "S":
        return 0
    return 1

def check_tr(grid: list, x: int, y: int):
    if len(grid[y]) - x - 3 <= 0 or y - 3 < 0 :
        return 0
    if grid[y-1][x+1] != "M":
        return 0
    if grid[y-2][x+2] != "A":
        return 0
    if grid[y-3][x+3] != "S":
        return 0
    return 1

def check_t(grid: list, x: int, y: int):
    if y - 3 < 0:
        return 0
    if grid[y-1][x] != "M":
        return 0
    if grid[y-2][x] != "A":
        return 0
    if grid[y-3][x] != "S":
        return 0
    return 1

def check_tl(grid: list, x: int, y: int):
    if x - 3 < 0 or y - 3 < 0 :
        return 0
    if grid[y-1][x-1] != "M":
        return 0
    if grid[y-2][x-2] != "A":
        return 0
    if grid[y-3][x-3] != "S":
        return 0
    return 1

def check_l(grid: list, x: int, y: int):
    if x - 3 < 0:
        return 0
    if grid[y][x-1] != "M":
        return 0
    if grid[y][x-2] != "A":
        return 0
    if grid[y][x-3] != "S":
        return 0
    return 1

def check_bl(grid: list, x: int, y: int):
    if x - 3 < 0 or len(grid) - y - 3 <= 0 :
        return 0
    if grid[y+1][x-1] != "M":
        return 0
    if grid[y+2][x-2] != "A":
        return 0
    if grid[y+3][x-3] != "S":
        return 0
    return 1

def check_b(grid: list, x: int, y: int):
    if len(grid) - y - 3 <= 0:
        return 0
    if grid[y+1][x] != "M":
        return 0
    if grid[y+2][x] != "A":
        return 0
    if grid[y+3][x] != "S":
        return 0
    return 1

def check_br(grid: list, x: int, y: int):
    if len(grid) - x - 3 <= 0 or len(grid) - y - 3 <= 0 :
        return 0
    if grid[y+1][x+1] != "M":
        return 0
    if grid[y+2][x+2] != "A":
        return 0
    if grid[y+3][x+3] != "S":
        return 0
    return 1

def check_plus(grid: list, x: int, y: int):
    if x == 0 or x == len(grid[y]) - 1 or y == 0 or y == len(grid) - 1:
        return 0
    neighbors = grid[y-1][x] + grid[y][x+1] + grid[y+1][x] + grid[y][x-1]
    neighbors += neighbors
    if "MMSS" in neighbors:
        return 1
    return 0

def check_cross(grid: list, x: int, y: int):
    if x == 0 or x == len(grid[y]) - 1 or y == 0 or y == len(grid) - 1:
        return 0
    neighbors = grid[y-1][x-1] + grid[y-1][x+1] + grid[y+1][x+1] + grid[y+1][x-1]
    neighbors += neighbors
    if "MMSS" in neighbors:
        return 1
    return 0

if __name__ == "__main__":
    print(run_script("input.txt"))