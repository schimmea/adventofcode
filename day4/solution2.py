from load_input_utils import load_input
import numpy as np
from day4.solution1 import transform_input, calculate_score


def lose_bingo(pulls, boards):
    board_masks = np.ones_like(boards, dtype=bool)
    for pull in reversed(pulls):
        board_masks[boards == pull] = 0
        vertical_losers = np.where(board_masks.sum(1).max(1) < 5)[0]
        horizontal_losers = np.where(board_masks.sum(2).max(1) < 5)[0]
        for loser in np.intersect1d(vertical_losers, horizontal_losers):
            print(f"Board {loser} loses.")
            board_masks[loser] += boards[loser] == pull
            score = calculate_score(boards[loser], board_masks[loser], pull)
            print(f"Score:", score)
            return


def main():
    inp = load_input.as_string()
    pulls, boards = transform_input(inp)
    lose_bingo(pulls, boards)


if __name__ == "__main__":
    main()
