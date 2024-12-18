import time
from typing import Union
from enum import Enum
from copy import deepcopy

class Type(Enum):
    ROBOT = 1
    FREE = 2
    BOX = 3
    WALL = 4
    BOX_LEFT = 5
    BOX_RIGHT = 6

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
    vis, moves = raw_data.split("\n\n")
    grid = []
    y = 0
    for line in vis.split("\n"):
        row = []
        for x in range(len(line)):
            if line[x] == "#":
                row.append(Type.WALL)
            elif line[x] == ".":
                row.append(Type.FREE)
            elif line[x] == "O":
                row.append(Type.BOX)
            elif line[x] == "@":
                row.append(Type.ROBOT)
                robot = (x, y)
            else: 
                raise Exception(f"Problem {line[x]}")
        grid.append(deepcopy(row))
        y += 1
    part_1(grid, robot, moves)
    grid = []
    y = 0
    for line in vis.split("\n"):
        row = []
        for x in range(len(line)):
            if line[x] == "#":
                row.append(Type.WALL)
                row.append(Type.WALL)
            elif line[x] == ".":
                row.append(Type.FREE)
                row.append(Type.FREE)
            elif line[x] == "O":
                row.append(Type.BOX_LEFT)
                row.append(Type.BOX_RIGHT)
            elif line[x] == "@":
                row.append(Type.ROBOT)
                row.append(Type.FREE)
                robot = (2*x, y)
            else: 
                raise Exception(f"Problem {line[x]}")
        grid.append(deepcopy(row))
        y += 1
    part_2(grid, robot, moves)
    return 0

def part_1(grid: list, robot: tuple, moves: str) -> None:
    moves = moves.replace("\n", "")
    for move in moves:
        if move == "^":
            robot = resolve_move_up(grid, robot)
        elif move == ">":
            robot = resolve_move_right(grid, robot)
        elif move == "<":
            robot = resolve_move_left(grid, robot)
        elif move == "v":
            robot = resolve_move_down(grid, robot)
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == Type.BOX:
                total += 100 * y + x
    print(f"Part 1: {total}")


def part_2(grid: list, robot: tuple, moves: str) -> None:
    moves = moves.replace("\n", "")
    for move in moves:
        if move == "^":
            robot = resolve_move_up_2(grid, robot)
        elif move == ">":
            robot = resolve_move_right_2(grid, robot)
        elif move == "<":
            robot = resolve_move_left_2(grid, robot)
        elif move == "v":
            robot = resolve_move_down_2(grid, robot)
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == Type.BOX_LEFT:
                total += 100 * y + x
    print(f"Part 2: {total}")

def resolve_move_up(grid: list, robot: tuple) -> tuple:
    r_x = robot[0]
    r_y = robot[1]
    offset = 1
    while grid[r_y - offset][r_x] == Type.BOX:
        offset += 1
    if offset == 1:
        if grid[r_y - 1][r_x] == Type.FREE:
            grid[r_y][r_x] = Type.FREE
            grid[r_y - 1][r_x] = Type.ROBOT
            return (r_x, r_y - 1)
        elif grid[r_y - 1][r_x] == Type.WALL:
            return (r_x, r_y)
        else: 
            raise Exception("Issue offset 1")
    else:
        if grid[r_y - offset][r_x] == Type.FREE:
            grid[r_y][r_x] = Type.FREE
            grid[r_y - offset][r_x] = Type.BOX
            grid[r_y - 1][r_x] = Type.ROBOT
            return (r_x, r_y - 1)
        elif grid[r_y - offset][r_x] == Type.WALL:
            return (r_x, r_y)
        else: 
            raise Exception("Issue offset 1")

def resolve_move_down(grid: list, robot: tuple) -> tuple:
    r_x = robot[0]
    r_y = robot[1]
    offset = 1
    while grid[r_y + offset][r_x] == Type.BOX:
        offset += 1
    if offset == 1:
        if grid[r_y + 1][r_x] == Type.FREE:
            grid[r_y][r_x] = Type.FREE
            grid[r_y + 1][r_x] = Type.ROBOT
            return (r_x, r_y + 1)
        elif grid[r_y + 1][r_x] == Type.WALL:
            return (r_x, r_y)
        else:
            raise Exception("Issue offset 1")
    else:
        if grid[r_y + offset][r_x] == Type.FREE:
            grid[r_y][r_x] = Type.FREE
            grid[r_y + offset][r_x] = Type.BOX
            grid[r_y + 1][r_x] = Type.ROBOT
            return (r_x, r_y + 1)
        elif grid[r_y + offset][r_x] == Type.WALL:
            return (r_x, r_y)
        else:
            raise Exception("Issue offset 1")

def resolve_move_left(grid: list, robot: tuple) -> tuple:
    r_x = robot[0]
    r_y = robot[1]
    offset = 1
    while grid[r_y][r_x - offset] == Type.BOX:
        offset += 1
    if offset == 1:
        if grid[r_y][r_x - 1] == Type.FREE:
            grid[r_y][r_x] = Type.FREE
            grid[r_y][r_x - 1] = Type.ROBOT
            return (r_x - 1, r_y)
        elif grid[r_y][r_x - 1] == Type.WALL:
            return (r_x, r_y)
        else: 
            raise Exception("Issue offset 1")
    else:
        if grid[r_y][r_x - offset] == Type.FREE:
            grid[r_y][r_x] = Type.FREE
            grid[r_y][r_x - offset] = Type.BOX
            grid[r_y][r_x - 1] = Type.ROBOT
            return (r_x - 1, r_y)
        elif grid[r_y][r_x - offset] == Type.WALL:
            return (r_x, r_y)
        else: 
            raise Exception("Issue offset 1")

def resolve_move_right(grid: list, robot: tuple) -> tuple:
    r_x = robot[0]
    r_y = robot[1]
    offset = 1
    while grid[r_y][r_x + offset] == Type.BOX:
        offset += 1
    if offset == 1:
        if grid[r_y][r_x + 1] == Type.FREE:
            grid[r_y][r_x] = Type.FREE
            grid[r_y][r_x + 1] = Type.ROBOT
            return (r_x + 1, r_y)
        elif grid[r_y][r_x + 1] == Type.WALL:
            return (r_x, r_y)
        else: 
            raise Exception("Issue offset 1")
    else:
        if grid[r_y][r_x + offset] == Type.FREE:
            grid[r_y][r_x] = Type.FREE
            grid[r_y][r_x + offset] = Type.BOX
            grid[r_y][r_x + 1] = Type.ROBOT
            return (r_x + 1, r_y)
        elif grid[r_y][r_x + offset] == Type.WALL:
            return (r_x, r_y)
        else: 
            raise Exception("Issue offset 1")


def resolve_move_up_2(grid: list, robot: tuple) -> tuple:
    r_x = robot[0]
    r_y = robot[1]
    boxes = [robot]
    next_check = set([robot])
    while next_check:
        new = set()
        for i in range(len(next_check)):
            (x, y) = next_check.pop()
            if grid[y - 1][x] == Type.WALL:
                return (r_x, r_y)
            elif grid[y - 1][x] == Type.BOX_LEFT:
                new.add((x, y - 1))
                new.add((x + 1, y - 1))
            elif grid[y - 1][x] == Type.BOX_RIGHT:
                new.add((x - 1, y - 1))
                new.add((x, y - 1))
            else:
                continue
        next_check = deepcopy(new)
        for pos in new:
            boxes.append(pos)
    for (x, y) in boxes[::-1]:
        grid[y - 1][x] = grid[y][x]
        grid[y][x] = Type.FREE
    return (r_x, r_y - 1)

def resolve_move_down_2(grid: list, robot: tuple) -> tuple:
    r_x = robot[0]
    r_y = robot[1]
    boxes = [robot]
    next_check = set([robot])
    while next_check:
        new = set()
        for i in range(len(next_check)):
            (x, y) = next_check.pop()
            if grid[y + 1][x] == Type.WALL:
                return (r_x, r_y)
            elif grid[y + 1][x] == Type.BOX_LEFT:
                new.add((x, y + 1))
                new.add((x + 1, y + 1))
            elif grid[y + 1][x] == Type.BOX_RIGHT:
                new.add((x - 1, y + 1))
                new.add((x, y + 1))
            else:
                continue
        next_check = deepcopy(new)
        for pos in new:
            boxes.append(pos)
    for (x, y) in boxes[::-1]:
        grid[y + 1][x] = grid[y][x]
        grid[y][x] = Type.FREE
    return (r_x, r_y + 1)

def resolve_move_left_2(grid: list, robot: tuple) -> tuple:
    r_x = robot[0]
    r_y = robot[1]
    boxes = [robot]
    next_check = set([robot])
    while next_check:
        new = set()
        for i in range(len(next_check)):
            (x, y) = next_check.pop()
            if grid[y][x - 1] == Type.WALL:
                return (r_x, r_y)
            elif grid[y][x - 1] == Type.BOX_RIGHT:
                new.add((x - 2, y))
                boxes.append((x - 1, y))
            else:
                continue
        next_check = deepcopy(new)
        for pos in new:
            boxes.append(pos)
    for (x, y) in boxes[::-1]:
        grid[y][x - 1] = grid[y][x]
        grid[y][x] = Type.FREE
    return (r_x - 1, r_y)

def resolve_move_right_2(grid: list, robot: tuple) -> tuple:
    r_x = robot[0]
    r_y = robot[1]
    boxes = [robot]
    next_check = set([robot])
    while next_check:
        new = set()
        for i in range(len(next_check)):
            (x, y) = next_check.pop()
            if grid[y][x + 1] == Type.WALL:
                return (r_x, r_y)
            elif grid[y][x + 1] == Type.BOX_LEFT:
                new.add((x + 2, y))
                boxes.append((x + 1, y))
            else:
                continue
        next_check = deepcopy(new)
        for pos in new:
            boxes.append(pos)
    for (x, y) in boxes[::-1]:
        grid[y][x + 1] = grid[y][x]
        grid[y][x] = Type.FREE
    return (r_x + 1, r_y)

def debug_print(grid: list):
    final = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == Type.WALL:
                final.append("#")
            elif grid[y][x] == Type.FREE:
                final.append(".")
            elif grid[y][x] == Type.ROBOT:
                final.append("@")
            elif grid[y][x] == Type.BOX_LEFT:
                final.append("[")
            elif grid[y][x] == Type.BOX_RIGHT:
                final.append("]")
            else:
                final.append("O")
        final.append("\n")
    print("".join(final))

if __name__ == "__main__":
    print(run_script("input.txt"))