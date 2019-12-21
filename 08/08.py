import numpy as np


def decode(data:str, img_shp:tuple) -> np.ndarray:
    n_layers = len(data) // (img_shp[0] * img_shp[1])
    data_numeric = np.array([int(i) for i in data])
    return data_numeric.reshape(n_layers, img_shp[1], img_shp[0])


with open("08/input.txt", "r") as f:
    data = f.readline().rstrip()
    
img_shp = (25, 6)
img = decode(data, img_shp)

fewest_0_layer = np.argmin(
    np.count_nonzero(
        img.reshape(img.shape[0], img.shape[1] * img.shape[2]
    ) == 0, axis=1)
)

answer1 = np.count_nonzero(img[fewest_0_layer] == 1) \
        * np.count_nonzero(img[fewest_0_layer] == 2)

print(f"Answer #1: {answer1}")