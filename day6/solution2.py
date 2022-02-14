from day6.solution1 import simulate_fish
from load_input_utils import load_input


def main():
    inp = load_input.one_line_int_list()
    print(simulate_fish(inp, 256))
    

if __name__ == "__main__":
    main()
