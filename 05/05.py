from copy import copy

with open("05/input.txt", "r") as f:
    program = [int(i) for i in f.read().split(",")]


def add(program:list, loc1:int, loc2:int) -> int:
    return program[loc1] + program[loc2]


def multiply(program:list, loc1:int, loc2:int) -> int:
    return program[loc1] * program[loc2]


def input_at(program:list, loc1:int) -> int:
    simulated_input = 1  # alternative to user input
    return simulated_input


def output_from(program:list, loc1:int) -> int:
    return program[loc1]


def parse_program(program:list) -> list:
    pointer = 0
    while True:        
        instruction1 = str(program[pointer]).zfill(5)
        opcode = int(instruction1[-2:])
        pm3, pm2, pm1 = [int(pm) for pm in instruction1[:-2]]

        loc1 = program[pointer + 1] if pm1 == 0 else pointer + 1
        loc2 = program[pointer + 2] if pm2 == 0 else pointer + 2
        loc3 = program[pointer + 3]

        if opcode == 1:
            program[loc3] = add(program, loc1, loc2)
            pointer += 4
        elif opcode == 2:
            program[loc3] = multiply(program, loc1, loc2)
            pointer += 4
        elif opcode == 3:
            program[program[pointer + 1]] = 1
            pointer += 2
        elif opcode == 4:
            print(output_from(program, loc1))
            pointer += 2
        elif opcode == 99:
            break
    
    return program


parse_program(program)