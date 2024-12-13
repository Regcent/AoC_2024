import time
from typing import Union
from copy import deepcopy

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
    equations = raw_data.split("\n")
    count_1 = 0
    count_2 = 0
    for equation in equations:
        target, numbers = equation.split(":")
        target = int(target)
        numbers = [int(i) for i in numbers.split()]
        if check(numbers, numbers[0], 0, target):
            count_1 += target
            count_2 += target
        else:
            if check_2(numbers, numbers[0], 0, target):
                count_2 += target
    print(f"Part 1: {count_1}")
    print(f"Part 2: {count_2}")

def check(numbers: list, curr: int, idx: int, target: int) -> bool:
    if curr > target:
        return False
    if idx == len(numbers) - 1:
        return curr == target
    return check(numbers, curr * numbers[idx + 1], idx + 1, target) or check(numbers, curr + numbers[idx + 1], idx + 1, target)

def check_2(numbers: list, curr: int, idx: int, target: int) -> bool:
    if curr > target:
        return False
    if idx == len(numbers) - 1:
        return curr == target
    return check_2(numbers, curr * numbers[idx + 1], idx + 1, target) or check_2(numbers, curr + numbers[idx + 1], idx + 1, target) or check_2(numbers, conc(curr, numbers[idx + 1]), idx + 1, target)

def conc(a: int, b: int) -> int:
    offset = 10
    while offset <= b:
        offset *= 10
    return offset * a + b

if __name__ == "__main__":
    print(run_script("input.txt"))