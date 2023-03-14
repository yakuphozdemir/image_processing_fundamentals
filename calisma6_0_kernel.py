import numpy as np

def kernel(x):
    kernel = np.ones(shape=(5,5),dtype=np.uint8)

    print(kernel)

    i = 0
    j = 0
    while True:
        while j < kernel.shape[1]:
            kernel[i][j] = x
            j+=1
        j = 0
        i += 1
        if i >= kernel.shape[0]:
            break
        
    print(kernel)