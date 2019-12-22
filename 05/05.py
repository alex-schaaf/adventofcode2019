from copy import copy

with open("05/input.txt", "r") as f:
    program = [int(i) for i in f.read().split(",")]


def parse_program(program:list) -> list:
    pointer = 0
    while True:        
        instruction1 = str(program[pointer]).zfill(5)
        opcode = int(instruction1[-2:])
        pm3, pm2, pm1 = [int(pm) for pm in instruction1[:-2]]

        try:
            loc1 = program[pointer + 1] if pm1 == 0 else pointer + 1
            loc2 = program[pointer + 2] if pm2 == 0 else pointer + 2
            loc3 = program[pointer + 3]
        except IndexError:
            break

        if opcode == 1:
            program[loc3] = program[loc1] + program[loc2]
            pointer += 4
        elif opcode == 2:
            program[loc3] = program[loc1] * program[loc2]
            pointer += 4
        elif opcode == 3:
            program[program[pointer + 1]] = int(input("Input <int>: "))
            pointer += 2
        elif opcode == 4:
            print(program[loc1])
            pointer += 2
        elif opcode == 5:
            if program[loc1] != 0:
                pointer = program[loc2]
            else:
                pointer += 3
        elif opcode == 6:
            if program[loc1] == 0:
                pointer = program[loc2]
            else:
                pointer += 3
        elif opcode == 7:
            if program[loc1] < program[loc2]:
                program[loc3] = 1
            else:
                program[loc3] = 0
            pointer += 4
        elif opcode == 8:
            if program[loc1] == program[loc2]:
                program[loc3] = 1
            else:
                program[loc3] = 0
            pointer += 4
        elif opcode == 99:
            break
    
    return program


parse_program(copy(program))
parse_program(copy(program))