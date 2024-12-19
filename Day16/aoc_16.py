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
    finish_nodes = solve(grid, start, end)
    print(f"Part 1: {finish_nodes[0][0]}")
    spots = set()
    for node in finish_nodes:
        for pos in node[2]:
            spots.add(pos)
    print(f"Part 2: {len(spots)}")
    return 0

def solve(grid: list, start: tuple, end: tuple) -> None:
    pq = PriorityQueue()
    pq.put((0, start, [(start[0], start[1])]))
    explored = dict()
    finish_nodes = []
    min_score = 1000000
    while pq.qsize():
        curr = pq.get()
        score = curr[0]
        if score > min_score:
            continue
        (x, y, direction) = curr[1]
        if curr[1] not in explored:
            explored[curr[1]] = score
        elif explored[curr[1]] < score:
            continue
        if (x, y) == end:
            if score < min_score:
                print("Problem if it appears more than once")
                min_score = score
            finish_nodes.append(curr)
            continue
        if direction == Dir.NORTH:
            if grid[y - 1][x]:
                if check(explored, (x, y - 1, Dir.NORTH),  score + 1):
                    pq.put((score + 1, (x, y - 1, Dir.NORTH), deepcopy(curr[2]) + [(x, y - 1)]))
            if check(explored, (x, y, Dir.EAST), score + 1000):
                pq.put((score + 1000, (x, y, Dir.EAST), deepcopy(curr[2])))
            if check(explored, (x, y, Dir.WEST), score + 1000):
                pq.put((score + 1000, (x, y, Dir.WEST), deepcopy(curr[2])))
        if direction == Dir.EAST:
            if grid[y][x + 1]:
                if check(explored,(x + 1, y, Dir.EAST), score + 1):
                    pq.put((score + 1, (x + 1, y, Dir.EAST), deepcopy(curr[2]) + [(x + 1, y)]))
            if check(explored, (x, y, Dir.NORTH), score + 1000):
                pq.put((score + 1000, (x, y, Dir.NORTH), deepcopy(curr[2])))
            if check(explored, (x, y, Dir.SOUTH), score + 1000):
                pq.put((score + 1000, (x, y, Dir.SOUTH), deepcopy(curr[2])))
        if direction == Dir.SOUTH:
            if grid[y + 1][x]:
                if check(explored, (x, y + 1, Dir.SOUTH),  score + 1):
                    pq.put((score + 1, (x, y + 1, Dir.SOUTH), deepcopy(curr[2]) + [(x, y + 1)]))
            if check(explored, (x, y, Dir.EAST), score + 1000):
                pq.put((score + 1000, (x, y, Dir.EAST), deepcopy(curr[2])))
            if check(explored, (x, y, Dir.WEST), score + 1000):
                pq.put((score + 1000, (x, y, Dir.WEST), deepcopy(curr[2])))
        if direction == Dir.WEST:
            if grid[y][x - 1]:
                if check(explored,(x - 1, y, Dir.WEST), score + 1):
                    pq.put((score + 1, (x - 1, y, Dir.WEST), deepcopy(curr[2]) + [(x - 1, y)]))
            if check(explored, (x, y, Dir.NORTH), score + 1000):
                pq.put((score + 1000, (x, y, Dir.NORTH), deepcopy(curr[2])))
            if check(explored, (x, y, Dir.SOUTH), score + 1000):
                pq.put((score + 1000, (x, y, Dir.SOUTH), deepcopy(curr[2])))
    return finish_nodes

def check(explored: dict, new: tuple, new_score: int) -> None:
    if new in explored:
        if new_score > explored[new]:
            return False
        else:
            print("Change needed")
    return True

if __name__ == "__main__":
    print(run_script("input.txt"))