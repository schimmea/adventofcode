from typing import List

from load_input_utils import load_input
import numpy as np


def get_fuel_cost(inp: List[int]) -> int:
    best_alignment = int(np.median(inp))
    fuel_cost = 0
    for pos in inp:
        fuel_cost += abs(best_alignment - pos)
    return fuel_cost


def main():
    input_list = load_input.one_line_int_list()
    print(get_fuel_cost(input_list))
    
    
if __name__ == "__main__":
    main()
