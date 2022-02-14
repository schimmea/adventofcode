from typing import List

from load_input_utils import load_input


def parse_instructions(inp: List[str]) -> int:
    horizontal = 0
    depth = 0
    for instruction in inp:
        key, value = instruction.split(" ")
        value = int(value)
        if key == "forward":
            horizontal += value
        elif key == "up":
            depth -= value
        elif key == "down":
            depth += value
    return horizontal * depth


def main():
    input_list = load_input.as_string_list()
    print(parse_instructions(input_list))
    
    
if __name__ == "__main__":
    main()
