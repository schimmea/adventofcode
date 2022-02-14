import re
from typing import Tuple, List

import numpy as np
from load_input_utils import load_input


def transform_input(inp: str) -> Tuple[List[int], np.ndarray]:
    inp_list = inp.split("\n")
    pulls = inp_list.pop(0).split(",")
    pulls = [int(x) for x in pulls]
    boards = np.array([re.findall(r"\d+", line) for line in inp_list if line != ""], dtype=int)
    boards = np.reshape(boards, (-1, 5, 5))
    return pulls, boards


def play_bingo(pulls: List[int], boards: np.ndarray) -> None:
    board_masks = np.zeros_like(boards, dtype=bool)
    for pull in pulls:
        board_masks[boards == pull] = 1
        vertical_winners = np.where(board_masks.sum(1) == 5)[0]
        horizontal_winners = np.where(board_masks.sum(2) == 5)[0]
        for winner in np.union1d(vertical_winners, horizontal_winners):
            print(f"Board {winner} wins.")
            score = calculate_score(boards[winner], board_masks[winner], pull)
            print(f"Score:", score)
            return


def calculate_score(board: np.ndarray, mask: np.ndarray, last_pull: int) -> int:
    return np.sum(board * np.invert(mask)) * last_pull


def main():
    inp = load_input.as_string()
    pulls, boards = transform_input(inp)
    play_bingo(pulls, boards)


if __name__ == "__main__":
    main()
