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
    lines = raw_data.split("\n")
    reports = [[int(i) for i in line.split()] for line in lines]
    part_1(reports)
    part_2(reports)
    return 0

def part_1(reports: list) -> None:
    count = 0
    for report in reports:
        if valid_report(report) == 0:
            count +=1
    print(f"Part 1: {count}")

def part_2(reports: list) -> None:
    count = 0
    for report in reports:
        result = valid_report(report)
        if result == 0:
            count +=1
            continue
        if valid_report(report[1:]) == 0:
            count += 1
            continue
        if valid_report(report[:result] + report[result + 1:]) == 0:
            count +=1
            continue
        if valid_report(report[:result - 1] + report[result:]) == 0:
            count += 1
    print(f"Part 2: {count}")

def valid_gap(gap: int, inc: bool) -> bool:
    if abs(gap) > 3 or gap == 0:
        return False
    if inc and gap < 0:
        return False
    if not inc and gap > 0:
        return False
    return True

def valid_report(report: list) -> int:
    gap = report[1] - report[0]
    inc = gap > 0
    for i in range(1, len(report)):
        if not valid_gap(report[i] - report[i-1], inc):
            return i
    return 0

if __name__ == "__main__":
    print(run_script("input.txt"))