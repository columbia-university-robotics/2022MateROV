import numpy as np


def vectorDrive(input_vector):
    A = np.array(
        [[1, -1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1], [1, -1, 0, 1, 0, -1], [1, 1, 0, 0, 0, -1], [0, 0, 1, 1, -1, 0],
         [0, 0, 1, 1, 1, 0]])
    t = A @ input_vector

    W = 0  # now normalize by finding maximum component
    for i in range(len(t)):
        W = max(W, abs(t[i]))

    if W > 1:  # normalization needed
        print('normalizing')
        for i in range(len(t)):
            t[i] = t[i] / W

    return t