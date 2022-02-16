from typing import List

from load_input_utils import load_input
import numpy as np


def get_overlaps(inp: np.ndarray) -> None:
    max_ix = np.max(inp) + 1
    field_map = np.zeros((max_ix, max_ix), dtype=int)
    for vent in inp:
        x1, y1, x2, y2 = vent
        x_range = range(x1, x2 + 1) if x2 > x1 else range(x1, x2 - 1, -1)
        y_range = range(y1, y2 + 1) if y2 > y1 else range(y1, y2 - 1, -1)
        if x1 != x2 and y1 != y2:
            # Use the fact that it's always 45 degrees -> abs(x2-x1) == abs(y2-y1).
            # This means that the two ranges are always the same size.
            for xp, yp in zip(x_range, y_range):
                field_map[xp, yp] += 1
        else:
            field_map[x_range, y_range] += 1
    print(np.sum(field_map >= 2))


def main():
    input_list = load_input.day_5_format()
    get_overlaps(input_list)


if __name__ == "__main__":
    main()
