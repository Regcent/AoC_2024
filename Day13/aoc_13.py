import time
from typing import Union
import re

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
    machines = raw_data.split("\n\n")
    total = 0
    for machine in machines:
        total += solve(machine)
    print(f"Part 1: {total}")
    total = 0
    for machine in machines:
        total += solve_tweak(machine)
    print(f"Part 2: {total}")

def solve(machine: str) -> int:
    possibilities = []
    a_x, a_y, b_x, b_y, p_x, p_y = [int(i) for i in re.findall(r"\d+", machine)]
    for a in range(100):
        if (p_x - a_x * a) % b_x == 0:
            if a_y * a + b_y * ((p_x - a_x * a) / b_x) == p_y:
                possibilities.append((a, (p_x - a_x * a) / b_x))
    if len(possibilities) == 0:
        return 0
    if len(possibilities) > 1:
        candidate = -1
        cost = 400
        for i in range(len(possibilities)):
            if 3 * possibilities[i][0] + possibilities[i][1] < cost:
                candidate = i
                cost = 3 * possibilities[i][0] + possibilities[i][1]
        return cost
    else:
        return  3 * possibilities[0][0] + possibilities[0][1]

def solve_tweak(machine: str) -> int:
    possibilities = []
    a_x, a_y, b_x, b_y, p_x, p_y = [int(i) for i in re.findall(r"\d+", machine)]
    for a in range(100):
        if (p_x - a_x * a) % b_x == 0:
            if a_y * a + b_y * ((p_x - a_x * a) / b_x) == p_y:
                possibilities.append((a, (p_x - a_x * a) / b_x))
    if len(possibilities) == 0:
        return 0
    if len(possibilities) > 1:
        candidate = -1
        cost = 400
        for i in range(len(possibilities)):
            if 3 * possibilities[i][0] + possibilities[i][1] < cost:
                candidate = i
                cost = 3 * possibilities[i][0] + possibilities[i][1]
        return cost
    else:
        return  3 * possibilities[0][0] + possibilities[0][1]

if __name__ == "__main__":
    print(run_script("input.txt"))