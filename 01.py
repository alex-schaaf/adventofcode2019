import numpy as np
from advent import mass_fuel_requirements, mass_fuel_recursive


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        sum_fuel = [
            mass_fuel_requirements(
                int(mass.rstrip())
            ) for mass in f.readlines()
        ]

    with open("input.txt", "r") as f: 
        sum_fuel_recursive = [
            mass_fuel_recursive(
                int(mass.rstrip())
            ) for mass in f.readlines()
        ]

    print(
        f"{int(sum(sum_fuel))}, recursive: {int(sum(sum_fuel_recursive))}"
    )