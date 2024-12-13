import time
from typing import Union
from copy import deepcopy

### Use Linked List and create nodes with ids / length and id = - 1 for freespace
class Block:
    
    def __init__(self, id, length):
        self.id = id
        self.length = length
        self.prev = prev
        self.next = next


def run_script(filepath: str) -> Union[int, str, float, bool]:
    with open(filepath, "r") as f:
        raw_data = f.read()
    return main_function(raw_data)

def main_function(raw_data: str) -> Union[int, str, float, bool]:
    start_time = time.time()
    q
    result = your_script(raw_data)

    elapsed_time = time.time() - start_time
    print(f"Time elapsed : {elapsed_time}s")
    return result

def your_script(raw_data: str) -> Union[int, str, float, bool]:
    """
    Time to code! Write your code here to solve today's problem
    """
    files = list()
    freespace = list()
    curr_id = 0
    free = False
    for char in raw_data:
        if not free:
            files.append((curr_id, int(char)))
            curr_id += 1
            free = True
        else:
            freespace.append(int(char))
            free = False
    part_1(deepcopy(files), deepcopy(freespace))
    return 0

def part_1(files: list, freespace: list):
    checksum = 0
    curr_idx = 0
    final = ""
    while files:
        (id, length) = files.pop(0)
        for i in range(length):
            checksum += curr_idx * id
            curr_idx += 1
            final += str(id)
        available = freespace.pop(0)
        stop = False
        while not stop and files:
            (id, length)= files[-1]
            if length > available:
                diff = available
                files[-1] = (id, length - available)
                stop = True
            else:
                diff = length
                files.pop()
                available -= length
            for i in range(diff):
                checksum += curr_idx * id
                curr_idx += 1
                final += str(id)
    print(f"Part 1: {checksum}")

def part_2(files: list, freespace: list):
    checksum = 0
    curr_idx = 0
    final = ""
    already_placed = set()
    last_id = -1
    while files:
        if last_id + 1 not in already_placed:
            (id, length) = files.pop(0)
            for i in range(length):
                checksum += curr_idx * id
                curr_idx += 1
                final += str(id)
                already_placed.add(id)
        last_id += 1
        available = freespace.pop(0)
        j = 1
        while True:
            if j >= len(files):
                final += "." * available
                break
            (id, length)= files[-j]
            if length > available:
                j += 1
                continue
            files.pop(-j)
            available -= length
            for k in range(length):
                print(f"Moving {id}")
                checksum += curr_idx * id
                curr_idx += 1
                final += str(id)
                j = 1
                already_placed.add(id)
                print("Reset")
            if available == 0:
                print("No more space")
                break
    print(final)
    print(f"Part 2: {checksum}")

if __name__ == "__main__":
    print(run_script("example.txt"))