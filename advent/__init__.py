import numpy as np


def fuel_required(mass:float) -> float:
    return np.floor(mass / 3) - 2