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
    border = []
    segments_v = dict()
    segments_h = dict()
    to_check = [next_case]
    print(f"Checking {grid[next_case[1]][next_case[0]]}")
    counted = set()
    counted.add(next_case)
    while to_check:
        curr = to_check.pop(0)
        area += 1
        x = curr[0]
        y = curr[1]
        explored[y].add(x)
        for neighbor in [(x-1, y), (x+1, y)]:
            # Add same neighbors to "counted" to avoid issues - other neighbors count as perimeter
            if neighbor in counted:
                continue
            if neighbor[0] < 0 or neighbor[0] > max_x:
                border.append(neighbor)
                if (x, neighbor[0]) not in segments_h:
                    segments_h[(x, neighbor[0])] = [y]
                else:
                    segments_h[(x, neighbor[0])].append(y)
                continue
            if grid[curr[1]][curr[0]] == grid[neighbor[1]][neighbor[0]]:
                to_check.append(neighbor)
                counted.add(neighbor)
            else:
                border.append(neighbor)
                if (x, neighbor[0]) not in segments_h:
                    segments_h[(x, neighbor[0])] = [y]
                else:
                    segments_h[(x, neighbor[0])].append(y)
        for neighbor in [(x, y-1), (x, y+1)]:
            # Add same neighbors to "counted" to avoid issues - other neighbors count as perimeter
            if neighbor in counted:
                continue
            if neighbor[1] < 0 or neighbor[1] > max_y:
                border.append(neighbor)
                if (y, neighbor[1]) not in segments_v:
                    segments_v[(y, neighbor[1])] = [x]
                else:
                    segments_v[(y, neighbor[1])].append(x)
                continue
            if grid[curr[1]][curr[0]] == grid[neighbor[1]][neighbor[0]]:
                to_check.append(neighbor)
                counted.add(neighbor)
            else:
                border.append(neighbor)
                if (y, neighbor[1]) not in segments_v:
                    segments_v[(y, neighbor[1])] = [x]
                else:
                    segments_v[(y, neighbor[1])].append(x)
    sides = count_sides(segments_h, segments_v)
    print(area, len(border), sides)
    return area, len(border), sides

def find_next_case(explored: dict, max_x: int) -> tuple:
    for key in explored:
        if len(explored[key]) < max_x + 1:
            for i in range(max_x + 1):
                if i not in explored[key]:
                    return (i, key)
    return None

def count_sides(segments_h: dict, segments_v: dict) -> int:
    sides = 0
    for y in segments_h:
        sides += 1
        if len(segments_h[y]) > 1:
            segments_h[y].sort()
            for i in range(len(segments_h[y]) - 1):
                if segments_h[y][i + 1] - segments_h[y][i] != 1:
                    sides += 1
    for x in segments_v:
        sides += 1
        if len(segments_v[x]) > 1:
            segments_v[x].sort()
            for i in range(len(segments_v[x]) - 1):
                if segments_v[x][i + 1] - segments_v[x][i] != 1:
                    sides += 1
    print(segments_h, segments_v)
    return sides

if __name__ == "__main__":
    print(run_script("input.txt"))