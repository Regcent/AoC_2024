import time
from typing import Union

#Perimeter = Different neighbors count, area = count of spots zith it
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
    grid = raw_data.split("\n")
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1
    explored = dict.fromkeys(range(max_y + 1))
    for key in explored:
        explored[key] = set()
    next_case = find_next_case(explored, max_x)
    total_1 = 0
    total_2 = 0
    while next_case:
        area, perimeter, sides = find_price(grid, explored, next_case, max_x, max_y)
        next_case = find_next_case(explored, max_x)
        total_1 += area * perimeter
        total_2 += area * sides
    print(f"Part 1: {total_1}")
    print(f"Part 2: {total_2}")

def find_price(grid: list, explored: dict, next_case: tuple, max_x: int, max_y: int) -> int:
    perimeter = 0
    area = 0
    sides = 0
    to_check = [next_case]
    print(f"Checking {grid[next_case[1]][next_case[0]]}")
    counted = set()
    counted.add(next_case)
    while to_check:
        curr = to_check.pop(0)
        area += 1
        explored[curr[1]].add(curr[0])
        neigh = neighbors(curr[0], curr[1], max_x, max_y)
        perimeter += 4 - len(neigh) # Automatically add the "empty" neighbors as perimeter
        for neighbor in neigh:
            # Add same neighbors to "counted" to avoid issues - other neighbors count as perimeter
            if neighbor in counted:
                continue
            if grid[curr[1]][curr[0]] == grid[neighbor[1]][neighbor[0]]:
                to_check.append(neighbor)
                counted.add(neighbor)
            else:
                perimeter += 1
    print(perimeter, area)
    return perimeter * area

def find_next_case(explored: dict, max_x: int) -> tuple:
    for key in explored:
        if len(explored[key]) < max_x + 1:
            for i in range(max_x + 1):
                if i not in explored[key]:
                    return (i, key)
    return None

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