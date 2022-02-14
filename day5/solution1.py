from typing import List

import numpy as np
from load_input_utils import load_input


def get_overlaps(inp: List[List[List[int]]]) -> None:
    max_ix = np.array(inp).max() + 1
    field_map = np.zeros((max_ix, max_ix), dtype=int)
    for vent in inp:
        x1, y1 = vent[0][0], vent[0][1]
        x2, y2 = vent[1][0], vent[1][1]
        if not x1 == x2 and not y1 == y2:
            continue
        x_range = range(min(x1, x2), max(x1, x2) + 1)
        y_range = range(min(y1, y2), max(y1, y2) + 1)
        field_map[x_range, y_range] += 1
    print(np.sum(field_map >= 2))


def main():
    inp = load_input.day_5_format()
    get_overlaps(inp)
    

if __name__ == "__main__":
    main()
