from typing import List


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
    def day_5_format(cls) -> List[List[List[int]]]:
        inp = []
        with open("input.txt") as file:
            while line := file.readline().rstrip():
                line = [[int(num) for num in x.split(",")] for x in line.split(" -> ")]
                inp.append(line)
        return inp
    
    @classmethod
    def one_line_int_list(cls) -> List[int]:
        with open("input.txt") as file:
            inp = [int(x) for x in file.readline().split(",")]
        return inp
