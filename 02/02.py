import numpy as np


def process_intcode(intcode):
    indices = np.arange(0, len(intcode), 4)
    for i in indices:
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
    # preprocess
    intcode[1] = 12
    intcode[2] = 2
    result = process_intcode(intcode)
    print(result)