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
    l1 = list()
    l2 = list()
    for line in raw_data.split("\n"):
        a, b = line.split()
        l1.append(int(a))
        l2.append(int(b))
    l1.sort()
    l2.sort()
    print(f"Part 1: {sum([abs(l1[i] - l2[i]) for i in range(len(l1))])}")
    print(f"Part 2: {sum([l1[i] * l2.count(l1[i]) for i in range(len(l1))])}")

if __name__ == "__main__":
    print(run_script("input.txt"))