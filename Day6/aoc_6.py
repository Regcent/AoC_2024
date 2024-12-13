import time
from typing import Union
from enum import Enum
from copy import deepcopy

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

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
    obstacles_v = dict()
    obstacles_h = dict()
    start_pos = (-1, -1)
    start_dir = Direction.UP
    grid = raw_data.split("\n")
    for x in range(len(grid[0])):
        obstacles_v[x] = [-1, len(grid)]
    for y in range(len(grid)):
        obstacles_h[y] =[-1, len(grid[y])]
        for x in range(len(grid[y])):
            if grid[y][x] == ".":
                continue
            if grid[y][x] == "#":
                obstacles_v[x].append(y)
                obstacles_h[y].append(x)
            if grid[y][x] == "^":
                start_pos = (x, y)
    path = part_1(start_pos, start_dir, obstacles_h, obstacles_v)
    part_2(path, obstacles_h, obstacles_v)
    return 0

def resolve(start_pos: tuple, start_dir: Direction, obstacles_h: dict, obstacles_v: dict, extra: tuple = (-1, -1), past: set = set(), step: bool = False):
    current = start_pos
    current_dir = start_dir
    explored = set()
    exit = False
    cycle = False
    path = list()
    while not exit and not cycle:
        #print(past, exit, cycle)
        if step:
            input("step")
        if current_dir == Direction.UP or current_dir == Direction.DOWN:
            obstacles = deepcopy(obstacles_v[current[0]])
            if extra[0] == current[0]:
                obstacles.append(extra[1])
            path_v, exit = find_path_v(current, current_dir, obstacles)
            for pos in path_v[1:]:
                if pos in past:
                    cycle = True
                    break
                path.append(pos)
                past.add(pos)
                explored.add((pos[0], pos[1]))
            current = path_v[-1]
            if current_dir == Direction.UP:
                current_dir = Direction.RIGHT
            else:
                current_dir = Direction.LEFT
        else:
            obstacles = deepcopy(obstacles_h[current[1]])
            if extra[1] == current[1]:
                obstacles.append(extra[0])
            path_h, exit = find_path_h(current, current_dir, obstacles)
            for pos in path_h[1:]:
                if pos in past:
                    cycle = True
                    break
                path.append(pos)
                past.add(pos)
                explored.add((pos[0], pos[1]))
            current = path_h[-1]
            if current_dir == Direction.LEFT:
                current_dir = Direction.UP
            else:
                current_dir = Direction.DOWN
    return exit, cycle, explored, path
                
def part_1(start_pos: tuple, start_dir: Direction, obstacles_h: dict, obstacles_v: dict):
    """ current = start_pos
    current_dir = start_dir
    path = list()
    explored = set()
    exit = False
    while not exit:
        if current_dir == Direction.UP or current_dir == Direction.DOWN:
            path_v, exit = find_path_v(current, current_dir, obstacles_v[current[0]])
            for pos in path_v:
                path.append(pos)
                explored.add((pos[0], pos[1]))
            current = path_v[-1]
            if current_dir == Direction.UP:
                current_dir = Direction.RIGHT
            else:
                current_dir = Direction.LEFT
        else:
            path_h, exit = find_path_h(current, current_dir, obstacles_h[current[1]])
            for pos in path_h:
                path.append(pos)
                explored.add((pos[0], pos[1]))
            current = path_h[-1]
            if current_dir == Direction.LEFT:
                current_dir = Direction.UP
            else:
                current_dir = Direction.DOWN"""
    exit, cycle, explored, path = resolve(start_pos, start_dir, obstacles_h, obstacles_v)
    print(f"Part 1: {len(explored)}")
    return path

def part_2(path: list, obstacles_h: dict, obstacles_v: dict):
    count = 0
    tested = set()
    past = set()
    for i in range(len(path) - 1):
        elem = path[i]
        past.add(elem)
        next = path[i + 1]
        if (next[0], next[1]) in tested:
            continue
        tested.add((next[0], next[1]))
        _, cycle, _, _ = resolve((elem[0], elem[1]), elem[2], obstacles_h, obstacles_v, (next[0], next[1]), deepcopy(past), False)
        if cycle:
            count += 1
    print(f"Part 2: {count}")
    
def find_path_v(current: tuple, current_dir: Direction, obstacles: list):
    potential = []
    if current_dir == Direction.UP:
        for obstacle in obstacles:
            if obstacle < current[1]:
                potential.append(obstacle)
        final = max(potential)
        return [(current[0], y, Direction.UP) for y in range(current[1], final, -1)], final == min(obstacles)
    else:
        for obstacle in obstacles:
            if obstacle > current[1]:
                potential.append(obstacle)
        final = min(potential)
        return [(current[0], y, Direction.DOWN) for y in range(current[1], final)], final == max(obstacles)

def find_path_h(current: tuple, current_dir: Direction, obstacles: list):
    potential = []
    if current_dir == Direction.LEFT:
        for obstacle in obstacles:
            if obstacle < current[0]:
                potential.append(obstacle)
        final = max(potential)
        return [(x, current[1], Direction.LEFT) for x in range(current[0], final, -1)], final == min(obstacles)
    else:
        for obstacle in obstacles:
            if obstacle > current[0]:
                potential.append(obstacle)
        final = min(potential)
        return [(x, current[1], Direction.RIGHT) for x in range(current[0], final)], final == max(obstacles)

if __name__ == "__main__":
    print(run_script("input.txt"))