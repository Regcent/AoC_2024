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
    rocks = dict()
    for number in raw_data.split():
        rocks[int(number)] = 1
    transition = {0: [1]}
    for i in range(25):
        rocks = blink(rocks, transition)
    print(f"Part 1: {count_rocks(rocks)}")    
    for i in range(50):
        rocks = blink(rocks, transition)
    print(f"Part 2: {count_rocks(rocks)}")
    
def blink(rocks: dict, transition: dict) -> dict:
    new = dict()
    for number in rocks:
        if number not in transition:
            find_transition(transition, number)
        for other in transition[number]:
            if other not in new:
                new[other] = 0
            new[other] += rocks[number]
    return new

def find_transition(transition: dict, number: int) -> None:
    if len(str(number)) % 2 == 0:
        div = len(str(number)) // 2
        transition[number] = [int(str(number)[div:]), int(str(number)[:div])]
    else:
        transition[number] = [number * 2024]

def count_rocks(rocks: dict) -> int:
    return sum([rocks[number] for number in rocks])

if __name__ == "__main__":
    print(run_script("input.txt"))