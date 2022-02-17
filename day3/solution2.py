import numpy as np

from load_input_utils import load_input
from day3.solution1 import to_int_array, to_binary_str, binary_column_modes


def iterative_mode_match(a: np.ndarray, invert=False) -> str:
    """Iterate over all bit positions and determine column-wise mode. Drop all numbers that are not mode."""
    out = a.copy()
    for position in range(out.shape[1]):
        modes = binary_column_modes(out)
        modes = 1 - modes if invert else modes
        mask = out[:, position] == modes[position]
        out = out[mask]
        if len(out) == 1:
            break
    return to_binary_str(out[0])


def calculate_life_support(inp: list) -> int:
    a = to_int_array(inp)
    oxygen = iterative_mode_match(a)
    co2 = iterative_mode_match(a, invert=True)
    return int(oxygen, 2) * int(co2, 2)


def main():
    inp = load_input.as_string_list()
    print(calculate_life_support(inp))


if __name__ == "__main__":
    main()
