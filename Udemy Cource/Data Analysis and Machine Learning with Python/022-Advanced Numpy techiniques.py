# %%
import numpy as np
import matplotlib.pyplot as plt

array_1 = np.array([1, 2, 3])
array_2 = np.array([4, 5, 6])

print(f"Array 1 : \n {array_1}")
print(f"Array 2 : \n {array_2}")


# %%
# Connected Array

connected_array = np.c_[array_1, array_2]
print(f"Connected Array : \n {connected_array}")


# %% 
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sum_array = np.sum(array)
print(f"Sum Array : \n {sum_array}")


# %%
sum_along_first_axis = np.sum(array, axis= 0)
print(f"Sum along first axis is : {sum_along_first_axis}")


# %%
array = np.array([ [1, 2, 3] , [4, 5, 6]])

transposed_array = array.transpose()
print(f"Transposed array using 'transpse' method : \n {transposed_array}")

transposed_array_T = array.T
print(f"Transposed array using 'T' attribute : \n {transposed_array_T}")


# %%
np.random.seed(0)

uniform_numbers = np.random.uniform(0, 1, 100)
normal_numbers = np.random.normal(0, 1, 100)

plt.hist(uniform_numbers, bins= 20, alpha= 0.5, label= "Uniform Distribution")
plt.hist(normal_numbers, bins= 20, alpha= 0.5, label= "Normal Distribution")

plt.legend()
plt.show()