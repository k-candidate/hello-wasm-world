import time
import numpy as np

start_time_range_sum = time.time()

total = 0
for i in range(10000):
    total += i

# print(f"The total is: {total}")
end_time_range_sum = time.time()
elapsed_time_range_sum = end_time_range_sum - start_time_range_sum
print(f"Elapsed time for range sum: {elapsed_time_range_sum:.6f} seconds")

start_time_np = time.time()
np.random.seed(42)
matrix1 = np.random.rand(20000,20000)
matrix2 = np.random.rand(20000,20000)
result_matrix = matrix1 + matrix2
end_time_np = time.time()
elapsed_time_np = end_time_np - start_time_np
# print("Shape of the resulting matrix:", result_matrix.shape)
print(f"Elapsed time for np: {elapsed_time_np:.6f} seconds")

with open("pystone.py") as file:
    exec(file.read())
