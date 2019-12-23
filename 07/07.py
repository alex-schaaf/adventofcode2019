from itertools import permutations
from copy import copy


def parse(program:list, input_instructions:list) -> list:
    pointer = 0
    input_pointer = 0
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
            # program[program[pointer + 1]] = int(input("Input <int>: "))
            program[program[pointer + 1]] = input_instructions[input_pointer]
            pointer += 2
            input_pointer += 1
        elif opcode == 4:
            # print(program[loc1])
            return program[loc1]
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


with open("07/input.txt", "r") as f:
    program = [int(i) for i in f.read().split(",")]

thruster_signals = []
for phase_settings in permutations(range(5), 5):
    input_signal = 0
    for amplifier in range(5):
        input_signal = parse(
            copy(program), 
            input_instructions=(phase_settings[amplifier], input_signal)
        )
    thruster_signals.append(input_signal)

print(f"Result #1: {max(thruster_signals)}")
