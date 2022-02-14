import numpy as np

from load_input_utils import load_input
from day3.solution1 import to_int_array, to_binary_str


def get_meta_mask(a: np.ndarray, inverse=False, tie_value=0) -> np.ndarray:
    threshold = len(a) / 2
    if (col_sum := a.sum()) > threshold:
        mode = 1 if not inverse else 0
    elif col_sum < threshold:
        mode = 0 if not inverse else 1
    else:
        mode = tie_value
    return np.where(a == mode)
    

def iterative_mode_match(a: np.ndarray, inverse=False, tie_value=0) -> str:
    mask = np.arange(len(a))
    position = 0
    while len(mask) > 1:
        meta_mask = get_meta_mask(a[mask, position], inverse=inverse, tie_value=tie_value)
        mask = mask[meta_mask]
        position += 1
    solution = a[mask].flatten()
    return to_binary_str(solution)


def calculate_life_support(inp: list) -> int:
    a = to_int_array(inp)
    oxygen = iterative_mode_match(a, inverse=False, tie_value=1)
    co2 = iterative_mode_match(a, inverse=True, tie_value=0)
    return int(oxygen, 2) * int(co2, 2)


def main():
    inp = load_input.as_string_list()
    print(calculate_life_support(inp))


if __name__ == "__main__":
    main()
