from typing import List, Tuple
import numpy as np

from load_input_utils import load_input


def to_int_array(inp: List[str]) -> np.ndarray:
    """
    Splits the binary numbers into integer 0s and 1s and puts them into an array.
    Useful for calculating column-wise mode.
    """
    return np.array([list(binary) for binary in inp], dtype=int)


def to_binary_str(a: np.ndarray) -> str:
    """Turns 1D int array back into a string binary."""
    return "".join(a.astype(str))


def binary_column_modes(a: np.ndarray) -> np.ndarray:
    colsums = a.sum(0)
    modes = colsums > len(a) / 2
    ties = colsums == len(a) / 2
    modes[ties] = 1
    return modes.astype(int)


def calculate_consumption(inp: List[str]) -> int:
    a = to_int_array(inp)
    modes = binary_column_modes(a)
    gamma = to_binary_str(modes)
    epsilon = to_binary_str(1 - modes)
    return int(gamma, 2) * int(epsilon, 2)


def main():
    inp = load_input.as_string_list()
    print(calculate_consumption(inp))
    
    
if __name__ == "__main__":
    main()
