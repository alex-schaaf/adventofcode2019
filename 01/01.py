import numpy as np
from copy import copy


def mass_fuel_requirements(mass:float) -> float:
    fuel = np.floor(mass / 3) - 2
    if fuel < 0:
        fuel = 0
    return fuel


def mass_fuel_recursive(mass:float):
    fuel = mass_fuel_requirements(mass)
    additional_fuel = copy(fuel)
    while additional_fuel > 0:
        additional_fuel = mass_fuel_requirements(additional_fuel)
        fuel += additional_fuel
    return fuel


if __name__ == "__main__":
    with open("01/input.txt", "r") as f:
        sum_fuel = [
            mass_fuel_requirements(
                int(mass.rstrip())
            ) for mass in f.readlines()
        ]

    with open("01/input.txt", "r") as f: 
        sum_fuel_recursive = [
            mass_fuel_recursive(
                int(mass.rstrip())
            ) for mass in f.readlines()
        ]

    print(
        f"{int(sum(sum_fuel))}, recursive: {int(sum(sum_fuel_recursive))}"
    )