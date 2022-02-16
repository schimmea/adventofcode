from load_input_utils import load_input
import numpy as np


def gaussian(inp: np.ndarray) -> np.ndarray:
    return inp * (inp + 1) / 2


def calculate_fuel_cost(inp: np.array, position: int) -> float:
    distances = np.abs(inp - position)
    fuel_cost = gaussian(distances)
    return fuel_cost.sum()


def find_best_fuel_cost(inp: list) -> int:
    a = np.array(inp)
    best_fuel_cost = np.inf
    for pos in range(max(a)):
        if (fuel_cost := calculate_fuel_cost(a, pos)) < best_fuel_cost:
            best_fuel_cost = fuel_cost
    return int(best_fuel_cost)


def main():
    input_list = load_input.one_line_int_list()
    print(find_best_fuel_cost(input_list))
    
    
if __name__ == "__main__":
    main()
