import numpy as np

def exponential_filter(data, alpha):
    filtered_data = np.zeros_like(data)
    filtered_data[0] = data[0]
    for i in range(1, len(data)):
        filtered_data[i] = alpha * data[i] + (1 - alpha) * filtered_data[i-1]
    return filtered_data

data = [1, 3, 5, 7, 9]
print(exponential_filter(data, 0.9))

