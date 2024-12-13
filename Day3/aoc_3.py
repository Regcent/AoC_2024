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
    part_1(raw_data)
    return 0

def part_1(raw_data: str) -> None:
    i = 0
    count = 0
    while i < len(raw_data):
        if raw_data[i] == "m" and raw_data[i + 1] == "u" and raw_data[i + 2] == "l":
            j = i + 3
            while j < len(raw_data):
                if raw_data[j] == ")":
                    break
                if raw_data[j] == "m":
                    i = j  
                j += 1  
            count += find_result(raw_data[i:j+1])
            i = j
        i += 1
    print(f"Part 1: {count}")

def find_result(segment: str) -> int:
    print(segment)
    if not segment.startswith("mul(") or not segment.endswith(")"):
        return 0
    numbers = segment[4:-1].split(",")
    if numbers[0] != numbers[0].strip():
        return 0
    if len(numbers) != 2:
        return 0
    if numbers[1] != numbers[1].strip():
        return 0
    if not numbers[0].isnumeric():
        return 0
    if not numbers[1].isnumeric():
        return 0
    return int(numbers[0]) * int(numbers[1])

if __name__ == "__main__":
    print(run_script("input.txt"))