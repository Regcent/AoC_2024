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
    grid = raw_data.split("\n")
    antennas = dict()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != ".":
                if grid[y][x] not in antennas:
                    antennas[grid[y][x]] = list()
                antennas[grid[y][x]].append((x, y))
    part_1(antennas, len(grid), len(grid[0]))
    part_2(antennas, len(grid), len(grid[0]))
    return 0

def part_1(antennas: dict, max_y: int, max_x: int):
    antinodes = set()
    for key in antennas:
        for i in range(len(antennas[key]) - 1):
            for j in range(i + 1, len(antennas[key])):
                a1 = antennas[key][i]
                a2 = antennas[key][j]
                an1 = (a1[0] + (a2[0] - a1[0]) * 2, a1[1] + (a2[1] - a1[1]) * 2)
                an2 = (a2[0] + (a1[0] - a2[0]) * 2, a2[1] + (a1[1] - a2[1]) * 2)
                if an1[0] < max_x and an1[1] < max_y and an1[0] >= 0 and an1[1] >= 0:
                    antinodes.add(an1)
                if an2[0] < max_x and an2[1] < max_y and an2[0] >= 0 and an2[1] >= 0:
                    antinodes.add(an2)
    print(f"Part 1: {len(antinodes)}")

def part_2(antennas: dict, max_y: int, max_x: int):
    antinodes = set()
    for key in antennas:
        for i in range(len(antennas[key]) - 1):
            for j in range(i + 1, len(antennas[key])):
                a1 = antennas[key][i]
                a2 = antennas[key][j]
                diff = (a1[0] - a2[0], a1[1] - a2[1])
                antinodes.add(a1)
                new = a1
                while True:
                    new = (new[0] - diff[0], new[1] - diff[1])
                    if new[0] < max_x and new[1] < max_y and new[0] >= 0 and new[1] >= 0:
                        antinodes.add(new)
                    else:
                        break
                new = a1
                while True:
                    new = (new[0] + diff[0], new[1] + diff[1])
                    if new[0] < max_x and new[1] < max_y and new[0] >= 0 and new[1] >= 0:
                        antinodes.add(new)
                    else:
                        break        
    print(f"Part 2: {len(antinodes)}")

if __name__ == "__main__":
    print(run_script("input.txt"))