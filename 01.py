import numpy as np
from advent import fuel_required


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        sum_fuel = [
            fuel_required(
                int(mass.rstrip())
            ) for mass in f.readlines()
        ]
    print(int(sum(sum_fuel)))