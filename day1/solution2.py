from typing import List, Iterator
import numpy as np
from load_input_utils import load_input
from day1.solution1 import num_increases


def sliding_window_sums(inp: List[int], n: int = 3) -> np.ndarray:
    out = np.cumsum(inp, dtype=int)
    out[n:] = out[n:] - out[:-n]
    return out[n - 1:]


def main():
    input_list = load_input.as_int_list()
    sliding_window = sliding_window_sums(input_list)
    print(num_increases(sliding_window))
    
    
if __name__ == "__main__":
    main()
