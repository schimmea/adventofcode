from typing import List, Any

import numpy as np
from load_input_utils import load_input


def simulate_fish(inp: List[int], days: int) -> int:
    zero_to_six_counts = np.zeros(7, dtype=np.longlong)
    existing_timers, counts = np.unique(inp, return_counts=True)
    zero_to_six_counts[existing_timers] = counts
    seven_eight_counts = np.zeros(2, dtype=np.longlong)
    for day in range(days):
        num_births = zero_to_six_counts[0]
        zero_to_six_counts = np.roll(zero_to_six_counts, -1)
        zero_to_six_counts[-1] += seven_eight_counts[0]
        seven_eight_counts = np.roll(seven_eight_counts, -1)
        seven_eight_counts[-1] = num_births
    return zero_to_six_counts.sum() + seven_eight_counts.sum()


def main():
    input_list = load_input.one_line_int_list()
    print(simulate_fish(input_list, 80))
    
    
if __name__ == "__main__":
    main()
