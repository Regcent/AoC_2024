import time
from typing import Union
from copy import deepcopy

### Use Linked List and create nodes with ids / length and id = - 1 for freespace
class Block:
    
    def __init__(self, id, length, prev):
        self.id = id
        self.length = length
        self.prev = prev
        self.next = None

    def __str__(self):
        if self.id == -1:
            return "." * self.length
        else:
            return f"{self.id}" * self.length

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
    first, last = parse_data(raw_data)
    part_1(first, last)
    first, last = parse_data(raw_data)
    part_2(first, last)

def parse_data(raw_data: str) -> list:
    first = Block(0, int(raw_data[0]), None)
    curr_id = 1
    free = True
    prev = first
    for char in raw_data[1:]:
        if not free:
            new = Block(curr_id, int(char), prev)
            if prev:
                prev.next = new
            curr_id += 1
            free = True
        else:
            new = Block(-1, int(char), prev)
            if prev:
                prev.next = new
            free = False
        prev = new
    last = new
    if last.id == -1:
        last = last.prev
        last.next = None
    return first, last

def debug_print(first: Block):
    curr = first
    while curr:
        print(str(curr), end="")
        curr = curr.next
    print()

def part_1(first: Block, last: Block):
    curr = first
    end = last
    while curr != end:
        if curr.id != -1:
            curr = curr.next
            continue
        end = last
        while curr != end:
            if end.id == -1:
                end = end.prev
                continue
            if end.length > curr.length:
                curr.id = end.id
                end.length -= curr.length
                break
            elif end.length == curr.length:
                curr.id = end.id
                free(end)
                break
            else:
                curr.id = end.id
                insert = Block(-1, curr.length - end.length, curr)
                insert.next = curr.next
                curr.length = end.length
                curr.next = insert
                free(end)
                end = end.prev
                if curr == end:
                    break
                curr = insert
    print(f"Part 1: {calculate_checksum(first)}")

def part_2(first: Block, last: Block):
    curr = last
    begin = first
    max_id = last.id
    already_moved = set()
    while curr != first:
        if curr.id == -1 or curr.id in already_moved:
            curr = curr.prev
            continue
        begin = first
        while curr != first:
            if curr == begin:
                curr = curr.prev
                break
            if begin.id != -1:
                if begin.next:
                    begin = begin.next
                    continue
                else:
                    already_moved.add(curr.id)
                    break
            if curr.length > begin.length:
                begin = begin.next
                continue
            elif begin.length == curr.length:
                begin.id = curr.id
                already_moved.add(curr.id)
                free(curr)
                curr = curr.prev
                break
            else:
                begin.id = curr.id
                already_moved.add(curr.id)
                insert = Block(-1, begin.length - curr.length, begin)
                begin.next.prev = insert
                insert.next = begin.next
                begin.next = insert
                begin.length = curr.length
                free(curr)
                break
    print(f"Part 2: {calculate_checksum(first)}")

def calculate_checksum(first: Block):
    curr = first
    checksum = 0
    curr_idx = 0
    while curr:
        if curr.id == -1:
            curr_idx += curr.length
        else:
            for i in range(curr.length):
                checksum += curr_idx * curr.id
                curr_idx += 1
        curr = curr.next
    return checksum

def free(block: Block):
    block.id = -1
    curr = block.next
    while curr:
        if curr.id != -1:
            curr.prev = block
            block.next = curr
            break
        block.length += curr.length
        curr = curr.next
    curr = block.prev
    while curr:
        if curr.id != -1:
            block.prev = curr
            curr.next = block
            break
        block.length += curr.length
        curr = curr.prev
    if not block.next:
        block.prev.next = None

if __name__ == "__main__":
    print(run_script("input.txt"))