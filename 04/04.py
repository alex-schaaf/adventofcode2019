from itertools import product
import numpy as np

puzzle_input = [int(n) for n in "245182-790572".split("-")]


def check_increasing(number:str):
    for i in range(5):
        if number[i] > number[i + 1]:
            return False
    return True


def check_double_digit(number:str):
    for i in range(5):
        if number[i] == number[i + 1]:
            return True
    return False


def check_at_least_1_double(number:str):
    counters = [0 for i in range(10)]
    for i in range(5):
        if number[i] == number[i + 1]:
            counters[int(number[i])] += 1
    for i in counters:
        if i == 1:
            return True
    return False


def check(numbers:list, test):
    return [number for number in numbers if test(number)]


if __name__ == "__main__":
    possibilities = np.array(list(product(range(10), repeat=6)))
    possibilities = possibilities[puzzle_input[0]:puzzle_input[1]]
    possibilities = possibilities[np.argwhere(
        np.count_nonzero(np.diff(possibilities, axis=1), axis=1) < 5)][:, 0, :]
    possibilities = possibilities[np.sum(
        np.diff(possibilities) >= 0, axis=1) == 5]
    print(
        f"Answer #1: {possibilities.shape[0]}"
    )

    possibilities = [str(i).zfill(6) for i in range(puzzle_input[0], 
                                                    puzzle_input[1])]
    print(
        f"Answer #2: {len(check(check(check(possibilities, check_increasing), check_double_digit), check_at_least_1_double))}"
    )