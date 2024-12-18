import time
from typing import Union
import re

class Robot:

    def __init__(self, init_x: int, init_y: int, v_x: int, v_y: int):
        self.init_x = init_x
        self.init_y = init_y
        self.v_x = v_x
        self.v_y = v_y
        self.current_x = init_x
        self.current_y = init_y
    
    def calculate_pos(self, width: int, length: int, seconds: int) -> tuple:
        return ((self.init_x + seconds * self.v_x)  % width, (self.init_y + seconds * self.v_y) % length)

    def iterate(self, width: int, length: int) -> tuple:
        self.current_x = (self.current_x + self.v_x) % width
        self.current_y = (self.current_y + self.v_y) % length
        return self.current_x, self.current_y

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
    width = 101
    length = 103
    robots = []
    for line in raw_data.split("\n"):
        r_x, r_y, v_x, v_y = re.findall(r"-?\d+", line)
        robots.append(Robot(int(r_x), int(r_y), int(v_x), int(v_y)))
    final = [0, 0, 0, 0]
    for robot in robots:
        x, y = robot.calculate_pos(width, length, 100)
        if x < width // 2 and y < length // 2:
            final[0] += 1
        elif x > width // 2 and y < length // 2:
            final[1] += 1
        elif x < width // 2 and y > length // 2:
            final[2] += 1
        elif x > width // 2 and y > length // 2:
            final[3] += 1
        else:
            continue
    print(f"Part 1: {final[0] * final[1] * final[2] * final[3]}")
    """for i in range(5000):
        for robot in robots:
            robot.iterate(width, length)
    """
    i = 12
    for j in range(i):
        for robot in robots:
            robot.iterate(width, length)
    while True:
        positions = set()
        for j in range(102):
            for robot in robots:
                robot.iterate(width, length)
        for robot in robots:
            positions.add(robot.iterate(width, length))
        show = []
        for y in range(length):
            show.append("\n")
            for x in range(width):
                if (x, y) not in positions:
                    show.append(" ")
                else:
                    show.append("#")
        print("".join(show))
        i += 103
        print(f"i = {i}")
        input()
                

if __name__ == "__main__":
    print(run_script("input.txt"))