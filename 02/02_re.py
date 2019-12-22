from copy import copy

with open("02/input.txt", "r") as f:
    program = [int(i) for i in f.read().split(",")]


def parse_opcode(opcode:int):
    def add(program:list, loc1:int, loc2:int) -> int:
        return program[loc1] + program[loc2]

    def multiply(program:list, loc1:int, loc2:int) -> int:
        return program[loc1] * program[loc2]

    if opcode == 1:
        return add
    elif opcode == 2:
        return multiply
    elif opcode == 99:
        return None


def parse_program(program:list, storage:list):
    for pointer in range(0, len(program), 4):
        opcode = program[pointer]
        operation = parse_opcode(opcode)
        if operation:
            result = operation(
                program, program[pointer + 1], program[pointer + 2]
            )
            storage[program[pointer + 3]] = result
        else:
            return storage


program1 = copy(program)
program1[1] = 12
program1[2] = 2
result1 = parse_program(program1, program1)[0]
print(f"Result #1: {result1}")


for noun in range(99):
    for verb in range(99):
        program2 = copy(program)
        program2[1] = noun
        program2[2] = verb
        result = parse_program(program2, program2)
        if program2[0] == 19690720:
            print(f"Result #2: {100 * noun + verb}")
            break