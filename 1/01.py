import numpy as np


def fuel_required(mass:float) -> float:
    return np.floor(mass / 3) - 2


if __name__ == "__main__":
    with open("1/input.txt", "r") as f:
        sum_fuel = [
            fuel_required(
                int(mass.rstrip())
            ) for mass in f.readlines()
        ]
    print(int(sum(sum_fuel)))