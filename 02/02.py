import numpy as np
from copy import copy


def process_intcode(intcode):
    for i in range(0, len(intcode), 4):
        opcode = intcode[i]
        if opcode == 99:
            return intcode
        elif opcode == 1 or opcode == 2:
            val1_loc = intcode[i+1]
            val2_loc = intcode[i+2]
            storage_loc = intcode[i+3]
            if opcode == 1:
                intcode[storage_loc] = intcode[val1_loc] + intcode[val2_loc]
            elif opcode == 2:
                intcode[storage_loc] = intcode[val1_loc] * intcode[val2_loc]
        else:
            break
    return intcode


if __name__ == "__main__":
    with open("02/input.txt", "r") as f:
        intcode = [int(value) for value in f.readline().split(",")]

    # part 1
    intcode1 = copy(intcode)
    intcode1[1] = 12
    intcode1[2] = 2
    result = process_intcode(intcode1)
    print(f"Result #1: {result[0]}")

    # part 2
    for noun in range(99):
        for verb in range(99):
            intcode_ = copy(intcode)
            intcode_[1] = noun
            intcode_[2] = verb
            result_ = process_intcode(intcode_)

            if result_[0] == 19690720:
                print(f"Result #2:\n100 * {noun} + {verb} = {100 * noun + verb}")
                break