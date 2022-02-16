from itertools import chain
from typing import List

import numpy as np


class load_input:
    @classmethod
    def as_string(cls) -> str:
        with open("input.txt", "r") as file:
            inp = file.read()
        return inp
    
    @classmethod
    def as_string_list(cls) -> List[str]:
        inp = []
        with open("input.txt", "r") as file:
            while line := file.readline().rstrip():
                inp.append(line)
        return inp
    
    @classmethod
    def as_int_list(cls) -> List[int]:
        inp = []
        with open("input.txt", "r") as file:
            while line := file.readline().rstrip():
                inp.append(int(line))
        return inp
    
    @classmethod
    def day_5_format(cls) -> np.ndarray:
        inp = []
        with open("input.txt") as file:
            while line := file.readline().rstrip():
                line_lists = [coords.split(",") for coords in line.split(" -> ")]
                inp.append([*line_lists[0], *line_lists[1]])
        return np.array(inp, dtype=int)
    
    @classmethod
    def one_line_int_list(cls) -> List[int]:
        with open("input.txt") as file:
            inp = [int(x) for x in file.readline().split(",")]
        return inp
