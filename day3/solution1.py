from typing import List, Tuple
from scipy.stats import mode
import numpy as np

from load_input_utils import load_input


def to_int_array(inp: List[str]) -> np.ndarray:
    return np.array([list(binary) for binary in inp], dtype=int)


def to_binary_str(a: np.ndarray) -> str:
    if (d := len(a.shape)) > 1:
        raise ValueError(f"Array needs to be 1D! Got {d}D.")
    return "".join(a.astype(str))


def calculate_consumption(inp: List[str]) -> int:
    a = to_int_array(inp)
    modes = mode(a)[0][0]
    gamma = to_binary_str(modes)
    epsilon = to_binary_str(1 - modes)
    return int(gamma, 2) * int(epsilon, 2)


def main():
    inp = load_input.as_string_list()
    print(calculate_consumption(inp))
    
    
if __name__ == "__main__":
    main()
