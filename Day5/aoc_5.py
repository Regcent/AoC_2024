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
    rules_raw, updates_raw = raw_data.split("\n\n")
    rules = dict()
    for rule in rules_raw.split("\n"):
        a, b = [int(i) for i in rule.split("|")]
        if a not in rules:
            rules[a] = [b]
        else:
            rules[a].append(b)
    updates = list()
    for update in updates_raw.split("\n"):
        updates.append([int(i) for i in update.split(",")])
    result = part_1(rules, updates)
    total = 0
    for update in result["ok"]:
        total += update[len(update) // 2]
    print(f"Part 1: {total}")
    part_2(rules, result["nok"])
    return 0

def part_1(rules: dict, updates: list) -> dict:
    result = {"ok": [], "nok": []}
    for update in updates:
        seen = []
        okay = True
        for page in update:
            if page in rules:
                for other in seen:
                    if other in rules[page]:
                        okay = False
                        break
                if not okay:
                    break
            seen.append(page)
        if okay:
            result["ok"].append(update)
        else:
            result["nok"].append(update)
    return result

def part_2(rules: dict, updates: list) -> None:
    total = 0
    for update in updates:
        quicksort_update(rules, update, 0, len(update) - 1)
        total += update[len(update) // 2]
    print(f"Part 2: {total}")

def quicksort_update(rules: dict, update: list, beg: int, end: int) -> list:
    if beg < end:
        pi = partition(rules, update, beg, end)
        quicksort_update(rules, update, beg, pi - 1)
        quicksort_update(rules, update, pi + 1, end)

def partition(rules: dict, update: list, beg: int, end: int) -> int:
    pivot = update[end]
    i = beg - 1
    for j in range(beg, end):
        if update[j] in rules:
            if pivot in rules[update[j]]:
                i += 1
                swap(update, i, j)
    swap(update, i + 1, end)
    return i + 1

def swap(update: list, i: int, j: int):
    update[i], update[j] = update[j], update[i]
    
if __name__ == "__main__":
    print(run_script("input.txt"))