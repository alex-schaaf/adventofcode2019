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

