from typing import Iterable

from load_input_utils import load_input


def num_increases(inp: Iterable[int]) -> int:
    increases = [1 for a, b in zip(inp, inp[1:]) if b > a]
    return len(increases)


def main():
    input_list = load_input.as_int_list()
    print(num_increases(input_list))


if __name__ == "__main__":
    main()
